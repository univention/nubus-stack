# CI Utilities

This directory contains tooling to support our CI setup and deploy Nubus into a
prepared environment.


## Deployment

The idea is to deploy into a new namespace which is based on the name of the
branch or a tag. The Ingress objects will then be configured based on this
namespace.

```
helmfile -n your-namespace template
helmfile -n your-namespace apply
helmfile -n your-namespace -e local apply
```


## Environment variables

- `REVIEW_PREFIX` - allows to override the prefix in use. This will be used to
  construct domains, e.g. `{{ REVIEW_PREFIX }}.portal.reviewBaseDomain`.

- `CHART_VERSION` - allows to set the chart version to deploy.

- `MASTER_PASSWORD` - has to be provided as a seed for the password derivation.


## Dependencies and requirements

The requirements can be met via the setup in
<https://git.knut.univention.de/univention/customers/dataport/upx/nubus-ci-base>.


### Certificates

A wildcard certificate has to be available via the name `certificates-ci-tls`
and it should have the following pattern:

- `reviewBaseDomain`
- `*.reviewBaseDomain`
- `*.id.reviewBaseDomain`
- `*.portal.reviewBaseDomain`
- `*.test.reviewBaseDomain`

The deployment will assume the certificate to be prepared in a secret within the
central CI namespace, e.g. `nubus-ci`, and try to deploy a copy into the target
namespace. This way there is no certificate request needed for a deployment and
we avoid bumping into rate limits.
