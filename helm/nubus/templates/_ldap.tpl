{{/*
LDAP admin credentials user credentials name
*/}}
{{- define "nubus.ldap.auth.cnAdmin.password.name" -}}

{{- if .Values.global.ldap.auth.cnAdmin.password.name -}}
  {{- .Values.global.ldap.auth.cnAdmin.password.name -}}
{{- else -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-ldap-server-credentials" $namePrefix -}}
{{- end -}}
{{- end -}}
