{{- /*
SPDX-FileCopyrightText: 2024 Univention GmbH
SPDX-License-Identifier: AGPL-3.0-only
*/}}
{{- define "nubusTemplates.masterPassword" -}}
{{- .Values.global.nubusMasterPassword | default (randAlphaNum 10 | sha1sum) -}}
{{- end -}}

{{- define "nubusTemplates.credentials.ldap.users.admin.password" -}}
{{- $nubusMasterPassword := include "nubusTemplates.masterPassword" . -}}
{{- (coalesce .Values.global.credentialOverride.defaultUsers.defaultAdminPassword (print (derivePassword 1 "long" $nubusMasterPassword "nubus" "nubus-admin") | sha1sum) )  -}}
{{- end -}}

{{- define "nubusTemplates.credentials.ldap.users.idp.password" -}}
{{- $nubusMasterPassword := include "nubusTemplates.masterPassword" . -}}
{{- (coalesce .Values.global.credentialOverride.defaultUsers.defaultUserPassword (print (derivePassword 1 "long" $nubusMasterPassword "nubus" "nubus-user") | sha1sum) )  -}}
{{- end -}}

{{- define "nubusTemplates.credentials.ldap.users.readonly.password" -}}
{{- $nubusMasterPassword := include "nubusTemplates.masterPassword" . -}}
{{- print (derivePassword 1 "long" $nubusMasterPassword "ldap-server" "ldap-readonly") | sha1sum  -}}
{{- end -}}

{{- define "nubusTemplates.connections.ldap.primary.host" -}}
{{- printf "%s-ldap-server-primary" .Release.Name -}}
{{- end -}}

{{- define "nubusTemplates.connections.ldap.secondary.host" -}}
{{- printf "%s-ldap-server-secondary" .Release.Name -}}
{{- end -}}

{{- define "nubusTemplates.connections.objectStorage.host" -}}
{{- if .Values.global.objectStorage.connection.host -}}
{{- tpl .Values.global.objectStorage.connection.host . -}}
{{- else -}}
{{- printf "%s-minio" .Release.Name -}}
{{- end -}}
{{- end -}}

{{- define "nubusTemplates.connections.objectStorage.port" -}}
{{- if .Values.global.objectStorage.connection.port -}}
{{- tpl .Values.global.objectStorage.connection.port . -}}
{{- else -}}
9000
{{- end -}}
{{- end -}}

{{- define "nubusTemplates.connections.objectStorage.protocol" -}}
{{- if .Values.global.objectStorage.connection.protocol -}}
{{- tpl .Values.global.objectStorage.connection.protocol . -}}
{{- else -}}
http
{{- end -}}
{{- end -}}

{{- define "nubusTemplates.connections.objectStorage.endpoint" -}}
{{- if .Values.global.objectStorage.connection.endpoint -}}
{{- tpl .Values.global.objectStorage.connection.endpoint . -}}
{{- else -}}
{{- $protocol := include "nubusTemplates.connections.objectStorage.protocol" . -}}
{{- $host := include "nubusTemplates.connections.objectStorage.host" . -}}
{{- $port := include "nubusTemplates.connections.objectStorage.port" . -}}
{{- printf "%s://%s:%s" $protocol $host $port -}}
{{- end -}}
{{- end -}}
