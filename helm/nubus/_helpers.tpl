{{- define "nubus.extraSecrets" -}}
{{- range .Values.nubusSecrets }}
---
kind: "Secret"
apiVersion: "v1"
type: {{ .type | default "Opaque" | quote }}
metadata:
  name: {{ .name | quote }}
  namespace: {{ include "common.names.namespace" $ | quote }}
  labels:
    {{- include "common.labels.standard" $ | nindent 4 }}
    {{- if $.Values.additionalLabels }}
    {{- include "common.tplvalues.render" ( dict "value" $.Values.additionalLabels "context" $ ) | nindent 4 }}
    {{- end }}
  {{- if $.Values.additionalAnnotations }}
  annotations: {{- include "common.tplvalues.render" ( dict "value" $.Values.additionalAnnotations "context" $ ) | nindent 4 }}
  {{- end }}
{{- if .data }}
data:
{{- range $k, $v := .data }}
  {{ $k }}: {{ $v | quote }}
{{- end }}
{{- end }}
{{- if .stringData }}
stringData:
{{- range $k, $v := .stringData }}
  {{ $k }}: {{ $v | quote }}
{{- end }}
{{- end }}
{{- end }}
{{- end -}}
