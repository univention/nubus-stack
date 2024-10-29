{{/*
Provisioning register consumers selfservice consumer secret
*/}}
{{- define "nubus.provisioning.selfserviceConsumer.auth.existingSecret.name" -}}
{{- $namePrefix := default .Release.Name .Values.global.releaseNameOverride | trunc 63 | trimSuffix "-" -}}
{{- printf "%s-selfservice-listener-credentials" $namePrefix -}}
{{- end -}}
