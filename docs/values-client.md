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
