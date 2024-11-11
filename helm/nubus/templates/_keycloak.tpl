{{/*
Keycloak secrets
*/}}
{{- define "nubus.keycloak.postgresql.auth.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-keycloak-postgresql-credentials" $namePrefix -}}
{{- end -}}

{{- define "nubus.keycloak.auth.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-keycloak-credentials" $namePrefix -}}
{{- end -}}

{{- define "nubus.keycloak.ldap.auth.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-keycloak-bootstrap-ldap-credentials" $namePrefix -}}
{{- end -}}

{{- define "nubus.keycloak.ldap.auth.bindDn" -}}
{{- $baseDn := include "nubusTemplates.ldapServer.ldap.baseDn" . -}}
{{ printf "uid=%s,cn=users,%s" "readonly" $baseDn }}
{{- end -}}

{{- define "nubus.keycloak-extensions.postgresql.auth.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-keycloak-extensions-postgresql-credentials" $namePrefix -}}
{{- end -}}

{{- define "nubus.keycloak-extensions.smtp.auth.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-keycloak-extensions-smtp-credentials" $namePrefix -}}
{{- end -}}
