{{- /*
SPDX-FileCopyrightText: 2024-2025 Univention GmbH
SPDX-License-Identifier: AGPL-3.0-only
*/}}
{{- define "nubusTemplates.masterPassword" -}}
{{- .Values.global.secrets.masterPassword | default (randAlphaNum 10 | sha1sum) -}}
{{- end -}}

{{- /* The bundled PostgreSQL and MinIO derive their credentials from the seed, so they need generation. */ -}}
{{- define "nubusTemplates.requireGeneratedPasswords" -}}
{{- if not (include "nubus-common.secrets.generatePasswords" .) -}}
{{- fail "The bundled PostgreSQL and MinIO are for demo deployments and need global.secrets.generatePasswords=true. Disable them and configure external services." -}}
{{- end -}}
{{- end -}}

{{- define "nubusTemplates.credentials.administrator.password" -}}
{{- $nubusMasterPassword := include "nubusTemplates.masterPassword" . -}}
{{- print (derivePassword 1 "long" $nubusMasterPassword "nubus" "nubus-administrator") | sha1sum -}}
{{- end -}}

{{- define "nubusTemplates.connections.ldap.primary.host" -}}
{{- printf "%s-ldap-server-primary" .Release.Name -}}
{{- end -}}

{{- define "nubusTemplates.connections.ldap.secondary.host" -}}
{{- printf "%s-ldap-server-secondary" .Release.Name -}}
{{- end -}}

{{- define "nubusTemplates.connections.postgres.host" -}}
{{ tpl (coalesce .Values.global.postgresql.connection.host (printf "%s-postgresql" .Release.Name ) ) . }}
{{- end -}}

{{- define "nubusTemplates.connections.postgres.port" -}}
{{ tpl (coalesce .Values.global.postgresql.connection.port "5432") . }}
{{- end -}}

{{- define "nubusTemplates.enablePlainUmcLogin" -}}
{{- if .Values.global.enablePlainUmcLogin -}}
{{- .Values.global.enablePlainUmcLogin -}}
{{- else -}}
false
{{- end -}}
{{- end -}}

{{- define "nubus.keycloak.ldap.auth.bindDn" -}}
{{- $baseDn := include "nubusTemplates.ldapServer.ldap.baseDn" . -}}
{{ printf "uid=%s,cn=users,%s" "readonly" $baseDn }}
{{- end -}}
