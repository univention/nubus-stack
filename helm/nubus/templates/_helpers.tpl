{{- /*
SPDX-FileCopyrightText: 2024 Univention GmbH
SPDX-License-Identifier: AGPL-3.0-only
*/}}
{{- define "nubusTemplates.masterPassword" -}}
{{- .Values.global.nubusMasterPassword | default (randAlphaNum 10 | sha1sum) -}}
{{- end -}}

{{- define "nubusTemplates.credentials.ldap.users.admin.password" -}}
{{- $nubusMasterPassword := include "nubusTemplates.masterPassword" . -}}
{{- print (derivePassword 1 "long" $nubusMasterPassword "nubus" "nubus-admin") | sha1sum  -}}
{{- end -}}

{{- define "nubusTemplates.credentials.ldap.users.idp.password" -}}
{{- $nubusMasterPassword := include "nubusTemplates.masterPassword" . -}}
{{- print (derivePassword 1 "long" $nubusMasterPassword "nubus" "nubus-user") | sha1sum  -}}
{{- end -}}

{{- define "nubusTemplates.credentials.ldap.users.readonly.password" -}}
{{- $nubusMasterPassword := include "nubusTemplates.masterPassword" . -}}
{{- print (derivePassword 1 "long" $nubusMasterPassword "nubus" "readonly") | sha1sum  -}}
{{- end -}}

{{- define "nubusTemplates.connections.ldap.primary.host" -}}
{{- printf "%s-ldap-server-primary" .Release.Name -}}
{{- end -}}

{{- define "nubusTemplates.connections.ldap.secondary.host" -}}
{{- printf "%s-ldap-server-secondary" .Release.Name -}}
{{- end -}}
