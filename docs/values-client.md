# Client access configuration

## Overview of common keys

- `keycloak`: Client access for Keycloak.
- `ldap`: Client access for LDAP.
- `nats`: NATS related configuration, mainly around the `provisioning` sub-chart.
- `objectStorage`: Client access for S3.
- `postgresql`: Client access for PostgreSQL.
- `provisioningApi`: Client access into the Provisioning API.
- `udm`: Client access for the UDM Rest API.

## Usage pattern

```yaml
# If the sub-chart does support global configuration for this key
global:
  {clientKey}:
    connection:
      # ...
    auth:
      # ...

# Typical usage in local values, this has precedence over "global"
{subChartName}:
  {clientKey}:
    connection:
      # ...
    auth:
      # ...

# Server chart (if present) does not have the "{clientKey}" level
{serverChartName}:
  auth:
    # ...
```

Be aware: The umbrella chart does in some cases add further elements into
`global.{clientKey}.auth` in order to be able to pass values into the
sub-charts. Those are not part of a common "API" like contract between the
umbrella chart and its sub-charts.

## Password and `Secret` configuration

We aim to adhere to a structure which is inspired by
[Bitnami's `common` chart](https://github.com/bitnami/charts/tree/main/bitnami/common#existingsecret).

With this structure we want to support the following use cases:

- Provide plain values.
- Provide an existing Kubernetes `Secret`.

Charts which provide the server-side of a component also support a third use
case which allows to provide no configuration at all. In this case a random
value will be generated and used so that also evaluation deployments are secure
by default.

### Full example

The full structure looks as follows for a case where both `username` and
`password` can be configured through a Kubernetes `Secret`:

```yaml
{clientKey}:
  auth:
    username: "username-value"
    password: "password-value"
    existingSecret:
      name: "existing-secret-name"
      keyMapping:
        username: "custom_username_key_value"
        password: "custom_password_key_value"
```

### Example providing plain values

The following example shows the configuration of the username and password as
regular values:

```yaml
smtp:
  auth:
    username: "example-smtp-username"
    password: "example-smtp-password"
```

A chart which is configured in this way will deploy its own `Secret` object to
hold the information about the password to use.

### Example using an existing Kubernetes `Secret`

The following example shows the configuration via an existing Kubernetes
`Secret`:

```yaml
smtp:
  auth:
    username: "example-username"
    existingSecret:
      name: "existing-secret-name"
```

The chart will expect that the `Secret` has been created already by the user.

The keys to use from the existing `Secret` can be customized via additional
parameters in `keyMapping` as shown above.


### Client configuration regarding PostgreSQL

The Nubus chart does offer to deploy a bundled sub-chart called `postgresql`
which is using the Bitnami chart. The secret configuration for this sub-chart is
not following the pattern from above. Compare the
[values.yaml file](https://github.com/bitnami/charts/blob/1bacd1a01f6b799e0dd908ebe86f3fcbcb5084a6/bitnami/postgresql/values.yaml#L135).

The following excerpt shows the relevant subset:

```yaml
auth:
  postgresPassword: ""
  username: ""
  password: ""
  existingSecret: ""
  secretKeys:
    adminPasswordKey: postgres-password
    userPasswordKey: password
```

This means the values inside of `postgresql.*` follow the pattern of this
sub-chart.

Our own sub-charts use the structure as documented above to configure the client
side access to PostgreSQL:

```yaml
postgresql:
  connection:
    # ...
  auth:
    username: "username-to-use"
    database: "database-to-use"
    existingSecret:
      name: "existing-secret-to-use"
      keyMapping:
        # ...
```
