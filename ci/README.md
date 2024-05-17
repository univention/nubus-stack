# CI Utilities

This directory contains tooling to support our CI setup.

## Deployment

Example commands:

```
helmfile template
helmfile apply
helmfile -e local apply
```

## Certificates

A wildcard certificate has to be available via the name `certificates-ci-tls`
and it should have the following pattern:

- `reviewBaseDomain`
- `*.reviewBaseDomain`
- `*.id.reviewBaseDomain`
- `*.portal.reviewBaseDomain`
- `*.test.reviewBaseDomain`
