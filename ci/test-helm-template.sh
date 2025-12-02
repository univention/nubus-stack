#!/bin/bash
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

# Test script to validate that helm template works with required value combinations
# This ensures that prod-values.yaml + example.yaml and demo-values.yaml + example.yaml
# provide all required values for successful template rendering.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHART_DIR="${SCRIPT_DIR}/../helm/nubus"
MASTER_PASSWORD="${MASTER_PASSWORD:-nubus-test-password}"

echo "Testing Helm chart template rendering..."
echo "Chart directory: ${CHART_DIR}"

# Check if Chart.lock exists, if not build dependencies
if [ ! -f "${CHART_DIR}/Chart.lock" ] || [ ! -d "${CHART_DIR}/charts" ]; then
    echo "Building Helm chart dependencies..."
    helm dependency build "${CHART_DIR}"
fi

# Test 1: prod-values.yaml + example.yaml
echo ""
echo "Test 1: Validating prod-values.yaml + example.yaml combination..."
if helm template nubus "${CHART_DIR}" \
    --values "${CHART_DIR}/prod-values.yaml" \
    --values "${CHART_DIR}/example.yaml" \
    --set global.secrets.masterPassword="${MASTER_PASSWORD}" \
    > /dev/null; then
    echo "✓ prod-values.yaml + example.yaml: SUCCESS"
else
    echo "✗ prod-values.yaml + example.yaml: FAILED"
    exit 1
fi

# Test 2: demo-values.yaml + example.yaml
echo ""
echo "Test 2: Validating demo-values.yaml + example.yaml combination..."
if helm template nubus "${CHART_DIR}" \
    --values "${CHART_DIR}/demo-values.yaml" \
    --values "${CHART_DIR}/example.yaml" \
    --set global.secrets.masterPassword="${MASTER_PASSWORD}" \
    > /dev/null; then
    echo "✓ demo-values.yaml + example.yaml: SUCCESS"
else
    echo "✗ demo-values.yaml + example.yaml: FAILED"
    exit 1
fi

echo ""
echo "All Helm template tests passed!"
