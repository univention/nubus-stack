{{/*
Provisioning register consumers portal consumer json secret
*/}}
{{- define "nubus.provisioning.registerConsumer.auth.portalConsumer.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-provisioning-register-consumers-json-secrets" $namePrefix -}}
{{- end -}}

{{/*
Provisioning register consumers selfservice consumer json secret
*/}}
{{- define "nubus.provisioning.registerConsumer.auth.selfserviceConsumer.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-provisioning-register-consumers-json-secrets" $namePrefix -}}
{{- end -}}
