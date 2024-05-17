# CI Utilities

This directory contains tooling to support our CI setup.

## Certificates

Currently using the openDesk chart with the following command:

```
helm -n jbornhold-tmp upgrade --install certificates oci://registry.opencode.de/bmi/opendesk/components/platform-development/charts/opendesk-certificates/opendesk-certificates --values ./values-certificates.yaml
```
