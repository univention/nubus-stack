#!/bin/bash
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH


# Configuration
KEYCLOAK_BASE_URL="${KEYCLOAK_BASE_URL}"
REALM="${REALM:-nubus}"
KC_ADMIN_USERNAME="${KC_ADMIN_USERNAME}"
KC_ADMIN_PASSWORD="${KC_ADMIN_PASSWORD}"
CLIENT_ID="${CLIENT_ID:-scim-client}"
AUDIENCE="${AUDIENCE:-scim-api-access}"

# Debug mode
DEBUG=true

# Function to debug output
debug_log() {
    if [ "$DEBUG" = true ]; then
        echo "[DEBUG] $1" >&2
    fi
}

# Function to get admin access token
get_admin_token() {
    echo "Getting admin access token..." >&2
    debug_log "Attempting to authenticate with: ${KEYCLOAK_BASE_URL}/realms/master/protocol/openid-connect/token"

    local response
    response=$(curl -s -w "HTTP_STATUS:%{http_code}" -X POST \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "username=${KC_ADMIN_USERNAME}" \
        -d "password=${KC_ADMIN_PASSWORD}" \
        -d "grant_type=password" \
        -d "client_id=admin-cli" \
        "${KEYCLOAK_BASE_URL}/realms/master/protocol/openid-connect/token")

    local http_status=$(echo "$response" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
    local body=$(echo "$response" | sed 's/HTTP_STATUS:[0-9]*$//')

    debug_log "HTTP Status: $http_status"

    if [ "$http_status" -ne 200 ]; then
        echo "Error: Failed to get admin token. HTTP Status: $http_status" >&2
        echo "Response: $body" >&2
        return 1
    fi

    local token=$(echo "$body" | jq -r '.access_token // empty')
    if [ -z "$token" ]; then
        echo "Error: No access token in response" >&2
        echo "Response: $body" >&2
        return 1
    fi

    echo "$token"
}

# Function to create the client
create_client() {
    local admin_token="$1"

    echo "Creating SCIM client..." >&2
    debug_log "Using admin token: ${admin_token:0:20}..."

    # Test the admin API endpoint first
    debug_log "Testing admin API accessibility..."
    local test_response
    test_response=$(curl -s -w "HTTP_STATUS:%{http_code}" -X GET \
        -H "Authorization: Bearer ${admin_token}" \
        -H "Accept: application/json" \
        "${KEYCLOAK_BASE_URL}/admin/realms/${REALM}")

    local test_http_status=$(echo "$test_response" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
    local test_body=$(echo "$test_response" | sed 's/HTTP_STATUS:[0-9]*$//')

    debug_log "Test API HTTP Status: $test_http_status"

    if [ "$test_http_status" -ne 200 ]; then
        echo "Error: Cannot access admin API. HTTP Status: $test_http_status" >&2
        echo "Response: $test_body" >&2
        return 1
    fi

    # Create client JSON payload with more conservative settings
    cat > client_payload.json << EOF
{
  "clientId": "${CLIENT_ID}",
  "name": "SCIM Server Client",
  "description": "Client for SCIM server authentication",
  "enabled": true,
  "clientAuthenticatorType": "client-secret",
  "standardFlowEnabled": false,
  "implicitFlowEnabled": false,
  "directAccessGrantsEnabled": false,
  "serviceAccountsEnabled": true,
  "publicClient": false,
  "protocol": "openid-connect",
  "fullScopeAllowed": true,
  "attributes": {
    "oauth2.device.authorization.grant.enabled": "false",
    "oidc.ciba.grant.enabled": "false"
  }
}
EOF

    # Create the client
    debug_log "Creating client at: ${KEYCLOAK_BASE_URL}/admin/realms/${REALM}/clients"
    local response
    response=$(curl -s -w "HTTP_STATUS:%{http_code}" -X POST \
        -H "Authorization: Bearer ${admin_token}" \
        -H "Content-Type: application/json" \
        -H "Accept: application/json" \
        -d @client_payload.json \
        "${KEYCLOAK_BASE_URL}/admin/realms/${REALM}/clients")

    local http_status=$(echo "$response" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
    local body=$(echo "$response" | sed 's/HTTP_STATUS:[0-9]*$//')

    debug_log "Create client HTTP Status: $http_status"

    # Clean up
    rm client_payload.json

    if [ "$http_status" -eq 201 ]; then
        echo "Client created successfully!" >&2
        return 0
    elif [ "$http_status" -eq 409 ]; then
        echo "Client already exists, continuing..." >&2
        return 0
    else
        echo "Error: Failed to create client. HTTP Status: $http_status" >&2
        echo "Response: $body" >&2
        return 1
    fi
}

# Function to add audience mapper to client
add_audience_mapper() {
    local admin_token="$1"
    local client_uuid="$2"

    echo "Adding audience mapper to client..." >&2
    debug_log "Adding audience mapper to client UUID: $client_uuid"

    # Create mapper JSON payload
    cat > mapper_payload.json << EOF
{
  "name": "scim-audience-mapper",
  "protocol": "openid-connect",
  "protocolMapper": "oidc-audience-mapper",
  "consentRequired": false,
  "config": {
    "id.token.claim": "false",
    "lightweight.claim": "false",
    "access.token.claim": "true",
    "introspection.token.claim": "true",
    "included.custom.audience": "${AUDIENCE}"
  }
}
EOF

    # Add the mapper
    local response
    response=$(curl -s -w "HTTP_STATUS:%{http_code}" -X POST \
        -H "Authorization: Bearer ${admin_token}" \
        -H "Content-Type: application/json" \
        -H "Accept: application/json" \
        -d @mapper_payload.json \
        "${KEYCLOAK_BASE_URL}/admin/realms/${REALM}/clients/${client_uuid}/protocol-mappers/models")

    local http_status=$(echo "$response" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
    local body=$(echo "$response" | sed 's/HTTP_STATUS:[0-9]*$//')

    debug_log "Add mapper HTTP Status: $http_status"

    # Clean up
    rm mapper_payload.json

    if [ "$http_status" -eq 201 ]; then
        echo "Audience mapper added successfully!" >&2
        return 0
    elif [ "$http_status" -eq 409 ]; then
        echo "Audience mapper already exists, continuing..." >&2
        return 0
    else
        echo "Warning: Failed to add audience mapper. HTTP Status: $http_status" >&2
        echo "Response: $body" >&2
        return 0  # Don't fail the whole script for this
    fi
}

# Function to get client secret
get_client_secret() {
    local admin_token="$1"

    echo "Getting client secret..." >&2
    debug_log "Fetching client UUID for: ${CLIENT_ID}"

    # Get client UUID
    local response
    response=$(curl -s -w "HTTP_STATUS:%{http_code}" -X GET \
        -H "Authorization: Bearer ${admin_token}" \
        -H "Accept: application/json" \
        "${KEYCLOAK_BASE_URL}/admin/realms/${REALM}/clients?clientId=${CLIENT_ID}")

    local http_status=$(echo "$response" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
    local body=$(echo "$response" | sed 's/HTTP_STATUS:[0-9]*$//')

    debug_log "Get client HTTP Status: $http_status"

    if [ "$http_status" -ne 200 ]; then
        echo "Error: Failed to get client information. HTTP Status: $http_status" >&2
        echo "Response: $body" >&2
        return 1
    fi

    local client_uuid
    client_uuid=$(echo "$body" | jq -r '.[0].id // empty')

    if [ -z "$client_uuid" ]; then
        echo "Error: Could not find client UUID" >&2
        echo "Response: $body" >&2
        return 1
    fi

    debug_log "Client UUID: $client_uuid"

    # Add audience mapper (try to add it, but don't fail if it doesn't work)
    add_audience_mapper "$admin_token" "$client_uuid"

    # Get client secret
    local secret_response
    secret_response=$(curl -s -w "HTTP_STATUS:%{http_code}" -X GET \
        -H "Authorization: Bearer ${admin_token}" \
        -H "Accept: application/json" \
        "${KEYCLOAK_BASE_URL}/admin/realms/${REALM}/clients/${client_uuid}/client-secret")

    local secret_http_status=$(echo "$secret_response" | grep -o "HTTP_STATUS:[0-9]*" | cut -d: -f2)
    local secret_body=$(echo "$secret_response" | sed 's/HTTP_STATUS:[0-9]*$//')

    debug_log "Get secret HTTP Status: $secret_http_status"

    if [ "$secret_http_status" -ne 200 ]; then
        echo "Error: Failed to get client secret. HTTP Status: $secret_http_status" >&2
        echo "Response: $secret_body" >&2
        return 1
    fi

    local client_secret
    client_secret=$(echo "$secret_body" | jq -r '.value // empty')

    if [ -z "$client_secret" ]; then
        echo "Error: Could not extract client secret" >&2
        echo "Response: $secret_body" >&2
        return 1
    fi

    echo "CLIENT_SECRET=${client_secret}" > scim-client.env
    echo "SCIM client secret stored in scim-client.env" >&2
}

# Main execution
main() {
    echo "Creating SCIM client in Keycloak..." >&2

    # Validate configuration
    if [ -z "${KC_ADMIN_PASSWORD}" ] || [ -z "${KC_ADMIN_USERNAME}" ] || [ -z "${KEYCLOAK_BASE_URL}" ]; then
        echo "Error: Please set KC_ADMIN_PASSWORD, KC_ADMIN_USERNAME, and KEYCLOAK_BASE_URL environment variables" >&2
        exit 1
    fi

    # Get admin token
    admin_token=$(get_admin_token)
    local token_result=$?

    if [ $token_result -ne 0 ] || [ -z "$admin_token" ] || [ "$admin_token" = "null" ]; then
        echo "Error: Could not obtain admin token. Check your credentials and Keycloak URL." >&2
        exit 1
    fi

    debug_log "Successfully obtained admin token"

    # Create client
    if ! create_client "$admin_token"; then
        echo "Error: Failed to create client" >&2
        exit 1
    fi

    # Get client secret
    if ! get_client_secret "$admin_token"; then
        echo "Error: Failed to get client secret" >&2
        exit 1
    fi
}

# Check if jq is installed
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed. Please install jq first." >&2
    exit 1
fi

# Check if curl is installed
if ! command -v curl &> /dev/null; then
    echo "Error: curl is required but not installed. Please install curl first." >&2
    exit 1
fi

# Run main function
main
