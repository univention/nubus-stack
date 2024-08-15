# CI Utilities

This directory contains tooling to support our CI setup and deploy Nubus into a
prepared environment.


## Approach

A small Helmfile is used as a wrapper for the deployment. It does deploy two things:

1. `certificates` is a utility Helm chart which is used to deploy a copy of the
   prepared wildcard certificate. This way it is avoided that a new deployment
   does hit Letsencrypt. This avoids running into rate limits.

2. `maildev` is a utility which provides a stub SMTP server with a web interface
   and API. The end-to-end tests use it to check that components which send
   emails work as expected.

3. `nubus` is the Nubus chart itself.

A CI job `deploy-gaia` does deploy this setup into the Gaia cluster. It uses a
namespace based on the branch name for the deployment and configured a subdomain
prefix also based on the branch name:

- Namespace: `ci-{$CI_COMMIT_REF_SLUG}`, e.g. `ci-example`
- Subdomain: `${CI_COMMIT_REF_SLUG}`, e.g. `example`

The full domain of the deployment is based on the value `reviewBaseDomain` and
based on the following patterns:

- Portal: `{REVIEW_PREFIX}.portal.{reviewBaseDomain}`, e.g.
  `jbornhold-ci-deploy.portal.review.gaia.open-desk.cloud`.
- Keycloak: `{REVIEW_PREFIX}.id.{reviewBaseDomain}`, e.g.
  `jbornhold-ci-deploy.id.review.gaia.open-desk.cloud`.
- Additional tooling for tests and development
  - Maildev: `{REVIEW_PREFIX}-maildev.test.{reviewBaseDomain}`, e.g.
    `jbornhold-ci-deploy-maildev.test.review.gaia.open-desk.cloud`.

The `REVIEW_PREFIX` being the leftmost part of the domains should help to ensure
that we have the best possible support for wildcard certificates during testing.


## Manual usage

### Deployment

The idea is to deploy into a new namespace which is based on the name of the
branch or a tag. The Ingress objects will then be configured based on this
namespace.

Copy `gaia-values.yaml.gotmpl` to `local-values.yaml.gotmpl` if you want to
tweak settings for deployments, e.g. when using a different target cluster.

```
helmfile -n your-namespace template
helmfile -n your-namespace apply
helmfile -n your-namespace -e local apply
```

### Environment variables

- `REVIEW_PREFIX` - allows to override the prefix in use. This will be used to
  construct domains, e.g. `{{ REVIEW_PREFIX }}.portal.reviewBaseDomain`. The
  target namespace will be used by default.

- `CHART_VERSION` - allows to set the chart version to deploy. By default the
  latest available version will be deployed.

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
