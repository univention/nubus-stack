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
