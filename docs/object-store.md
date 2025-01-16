# S3 compatible object store

The components `portal-server` and `portal-consumer` store state in an S3
compatible object store like MinIO. By default a bundled instance is deployed
with the umbrella chart.


## Using an external object store

### Bucket and policy configuration

One bucket has to be provided which will hold the portal related data. The data
consists of internal state and assets like icons, logos and background images of
the portal configuration. The recommended setup is as follows:

One bucket is required, e.g. `portal-data`. The sub-path `portal-assets` has to
be made available for anonymous download so that assets like icons can be
accessed.

Two accounts for access should be created and associated with respective policies:

- The `portal-consumer` does require write access.

- The `portal-server` does only require read access.

The following example shows a working provisioning configuration of the minio
chart to set up a respective store:

```yaml
provisioning:
  enabled: true
  extraCommands:
    - "mc anonymous set download provisioning/portal-data/portal-assets"
  buckets:
    - name: "portal-data"
      versioning: false
      withLock: false
  policies:
    - name: "portal-data-read"
      statements:
        - resources:
            - "arn:aws:s3:::portal-data"
            - "arn:aws:s3:::portal-data/*"
          effect: "Allow"
          actions:
            - "s3:GetBucketLocation"
            - "s3:GetObject"
    - name: "portal-data-readwrite"
      statements:
        - resources:
            - "arn:aws:s3:::portal-data"
            - "arn:aws:s3:::portal-data/*"
          effect: "Allow"
          actions:
            - "s3:*"
  users:
    - username: portal-server
      password: {{ .Values.devSecrets.userPassword | quote }}
      disabled: false
      policies:
        - portal-data-read
    - username: portal-consumer
      password: {{ .Values.devSecrets.userPassword | quote }}
      disabled: false
      policies:
        - portal-data-readwrite
```

### Configuration to use the external object store

Two adjustments are needed:

1. Disable the bundled minio subchart.

2. Configure `portal-server` and `portal-consumer` to use the external store.

The following example is aligned with the example above. Access key IDs and the
related secrets would have to be replaced to make it work:

```yaml
minio:
  enabled: false

nubusPortalConsumer:
  objectStorage:
    auth:
      # Configure this with the access key id and secret for the portal consumer
      accessKey: "READ_WRITE_ACCESS_KEY"
      secretKey: "SECRET"
    endpoint: "https://api.external-store.example"
    bucketName: "portal-data"

nubusPortalServer:
  objectStorage:
    auth:
      # Configure this with the access key id and secret for the portal server
      accessKey: "READ_ONLY_ACCESS_KEY"
      secretKey: "SECRET"
    endpoint: "https://api.external-store.example"
    bucketName: "portal-data"
```
