# nubus

Univention Nubus

- **Version**: 1.0.0
- **Type**: application

## TL;DR

```console
helm upgrade --install nubus oci://artifacts.software-univention.de/nubus/charts/nubus
```

## Introduction

This chart does install Nubus.

## Installing

To install the chart with the release name `nubus`:

```console
helm upgrade --install nubus oci://artifacts.software-univention.de/nubus/charts/nubus
```

## Uninstalling

To uninstall the chart with the release name `nubus`:

```console
helm uninstall nubus
```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://artifacts.software-univention.de/nubus/charts | nubusGuardian(guardian) | 0.18.0 |
| oci://artifacts.software-univention.de/nubus/charts | keycloak(keycloak) | 0.9.3 |
| oci://artifacts.software-univention.de/nubus/charts | nubusKeycloakBootstrap(keycloak-bootstrap) | 0.10.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusKeycloakExtensions(keycloak-extensions) | 0.16.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLdapNotifier(ldap-notifier) | 0.34.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLdapServer(ldap-server) | 0.34.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLicenseImport(license-import) | 0.1.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusNotificationsApi(notifications-api) | 0.64.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubus-common | ^0.8.x |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalConsumer(portal-consumer) | 0.64.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalFrontend(portal-frontend) | 0.64.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalServer(portal-server) | 0.64.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusProvisioning(provisioning) | 0.49.4 |
| oci://artifacts.software-univention.de/nubus/charts | nubusSelfServiceConsumer(selfservice-consumer) | 0.14.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusStackDataUms(stack-data-ums) | 0.89.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUdmListener(udm-listener) | 0.49.3 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUdmRestApi(udm-rest-api) | 0.29.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUmcGateway(umc-gateway) | 0.39.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUmcServer(umc-server) | 0.39.0 |
| oci://registry-1.docker.io/bitnamicharts | minio | 14.7.0 |
| oci://registry-1.docker.io/bitnamicharts | postgresql | ^12.x.x |

## Values

<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>additionalAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Additional custom annotations to add to all objects deployed directly by the umbrella chart.</td>
		</tr>
		<tr>
			<td>additionalLabels</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Additional custom labels to add to all objects deployed directly by the umbrella chart.</td>
		</tr>
		<tr>
			<td>certificates</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true
}
</pre>
</td>
			<td>SAML certificates generation</td>
		</tr>
		<tr>
			<td>certificates.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable SAML self-signed certificate generation. This required cert-manager.io</td>
		</tr>
		<tr>
			<td>extraSecrets</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.certManagerIssuer</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.configMapUcr</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-ums-ucr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.configUcr.apache2.loglevel</td>
			<td>string</td>
			<td><pre lang="json">
"info"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.configUcr.umc.module.debug.level</td>
			<td>int</td>
			<td><pre lang="json">
2
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.configUcr.umc.server.debug.level</td>
			<td>int</td>
			<td><pre lang="json">
2
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.domain</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.enablePlainUmcLogin</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Allow plain UMC login (otherwise only SAML login is possible) Be aware this will expose the UMC login page to the public, which can circumvent 2FA and other security measures placed in the IdP.</td>
		</tr>
		<tr>
			<td>global.extensions</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Extensions to load. Add entries to load additional extensions into Nubus.</td>
		</tr>
		<tr>
			<td>global.ingressClass</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.keycloak.realm</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.auth.cnAdmin.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.auth.cnAdmin.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.auth.cnAdmin.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.baseDn</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.domainName</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.memcached.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.memcached.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.nubusDeployment</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Indicates to all subcharts that they are being used as part of a Nubus deployment.</td>
		</tr>
		<tr>
			<td>global.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.secrets.masterPassword</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Master password from which other passwords are derived.</td>
		</tr>
		<tr>
			<td>global.subDomains.keycloak</td>
			<td>string</td>
			<td><pre lang="json">
"id"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.subDomains.portal</td>
			<td>string</td>
			<td><pre lang="json">
"portal"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.systemExtensions</td>
			<td>list</td>
			<td><pre lang="json">
[
  {
    "image": {
      "imagePullPolicy": "IfNotPresent",
      "registry": "artifacts.software-univention.de",
      "repository": "nubus/images/portal-extension",
      "tag": "0.59.1@sha256:c9c7faa3cca2be2f45d073517a50e8a8cc89d46c978c2f3a6be3c13d0e6ae900"
    },
    "name": "portal"
  }
]
</pre>
</td>
			<td>Allows to configure the system extensions to load. This is intended for internal usage, prefer to use `global.extensions` for user configured extensions.</td>
		</tr>
		<tr>
			<td>global.udm.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.udmRestApi.uri\" . }}"
</pre>
</td>
			<td>Global default for the URL via which the UDM Rest API can be reached. In transition state, not all subcharts do make use of this yet.</td>
		</tr>
		<tr>
			<td>ingress</td>
			<td>object</td>
			<td><pre lang="json">
{
  "annotations": {
    "nginx.ingress.kubernetes.io/proxy-body-size": "128k",
    "nginx.ingress.kubernetes.io/proxy-buffer-size": "64k",
    "nginx.ingress.kubernetes.io/proxy-buffers-number": "4",
    "nginx.ingress.kubernetes.io/proxy-busy-buffers-size": "128k",
    "nginx.ingress.kubernetes.io/proxy-http-version": "1.1",
    "nginx.ingress.kubernetes.io/proxy-set-headers": "Host $http_host;\nX-Forwarded-For $proxy_add_x_forwarded_for;\nX-Forwarded-Host $http_x_forwarded_host;\nX-Forwarded-Port $http_x_forwarded_port;\nX-Forwarded-Proto $http_x_forwarded_proto;\n",
    "nginx.ingress.kubernetes.io/use-regex": "true"
  },
  "certManager": {
    "enabled": true,
    "issuerRef": {
      "kind": "ClusterIssuer",
      "name": ""
    }
  },
  "favicon": {
    "enabled": true
  },
  "host": "",
  "ingressClassName": "",
  "minio": {
    "enabled": true
  },
  "tls": {
    "enabled": true,
    "secretName": ""
  }
}
</pre>
</td>
			<td>Configure supporting Ingress resources created directly by the umbrella chart.  The "enabled" attribute has been split, so that it is easier to enabled or disable individual resources. They are organized according to the pattern "{purpose}.enabled".  Ref.: https://kubernetes.io/docs/concepts/services-networking/ingress/</td>
		</tr>
		<tr>
			<td>ingress.annotations</td>
			<td>object</td>
			<td><pre lang="json">
{
  "nginx.ingress.kubernetes.io/proxy-body-size": "128k",
  "nginx.ingress.kubernetes.io/proxy-buffer-size": "64k",
  "nginx.ingress.kubernetes.io/proxy-buffers-number": "4",
  "nginx.ingress.kubernetes.io/proxy-busy-buffers-size": "128k",
  "nginx.ingress.kubernetes.io/proxy-http-version": "1.1",
  "nginx.ingress.kubernetes.io/proxy-set-headers": "Host $http_host;\nX-Forwarded-For $proxy_add_x_forwarded_for;\nX-Forwarded-Host $http_x_forwarded_host;\nX-Forwarded-Port $http_x_forwarded_port;\nX-Forwarded-Proto $http_x_forwarded_proto;\n",
  "nginx.ingress.kubernetes.io/use-regex": "true"
}
</pre>
</td>
			<td>Define custom ingress annotations. annotations:   nginx.ingress.kubernetes.io/rewrite-target: /</td>
		</tr>
		<tr>
			<td>ingress.certManager</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true,
  "issuerRef": {
    "kind": "ClusterIssuer",
    "name": ""
  }
}
</pre>
</td>
			<td>Request certificates via cert-manager.io annotation</td>
		</tr>
		<tr>
			<td>ingress.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable cert-manager.io annotaion.</td>
		</tr>
		<tr>
			<td>ingress.certManager.issuerRef.kind</td>
			<td>string</td>
			<td><pre lang="json">
"ClusterIssuer"
</pre>
</td>
			<td>Type of Issuer, f.e. "Issuer" or "ClusterIssuer".</td>
		</tr>
		<tr>
			<td>ingress.certManager.issuerRef.name</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Name of cert-manager.io Issuer resource.</td>
		</tr>
		<tr>
			<td>ingress.favicon</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true
}
</pre>
</td>
			<td>Serve an icon on the path "/favicon.ico" if enabled.</td>
		</tr>
		<tr>
			<td>ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Define the Fully Qualified Domain Name (FQDN) where application should be reachable.</td>
		</tr>
		<tr>
			<td>ingress.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>The Ingress controller class name.</td>
		</tr>
		<tr>
			<td>ingress.minio</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true
}
</pre>
</td>
			<td>Serve dynamic portal assets (icons, logos, background images) out of the MinIO bucket "portal-assets".  This is intended to be used together with the bundled minio. If an external S3-compatible store is used then a potentially needed Ingress resource as to be set up by the operator.</td>
		</tr>
		<tr>
			<td>ingress.tls</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true,
  "secretName": ""
}
</pre>
</td>
			<td>Secure an Ingress by specifying a Secret that contains a TLS private key and certificate.  Ref.: https://kubernetes.io/docs/concepts/services-networking/ingress/#tls</td>
		</tr>
		<tr>
			<td>ingress.tls.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable TLS/SSL/HTTPS for Ingress.</td>
		</tr>
		<tr>
			<td>ingress.tls.secretName</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>The name of the kubernetes secret which contains a TLS private key and certificate. Hint: This secret is not created by this chart and must be provided.</td>
		</tr>
		<tr>
			<td>keycloak.config.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.ingress.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.keycloak.auth.existingSecret.keyMapping.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
"admin_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.postgresql.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-postgresql-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak_user"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.auth.existingSecret</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-minio-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.auth.rootUser</td>
			<td>string</td>
			<td><pre lang="json">
"admin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.networkPolicy.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.networkPolicy.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.networkPolicy.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.networkPolicy.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.networkPolicy.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.buckets[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.buckets[0].versioning</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.buckets[0].withLock</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.cleanupAfterFinished.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.cleanupAfterFinished.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.cleanupAfterFinished.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.cleanupAfterFinished.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.cleanupAfterFinished.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.cleanupAfterFinished.seconds</td>
			<td>int</td>
			<td><pre lang="json">
900
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.extraCommands[0]</td>
			<td>string</td>
			<td><pre lang="json">
"mc anonymous set download provisioning/nubus/portal-assets"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"nubus-readwrite"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].statements[0].actions[0]</td>
			<td>string</td>
			<td><pre lang="json">
"s3:*"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].statements[0].effect</td>
			<td>string</td>
			<td><pre lang="json">
"Allow"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].statements[0].resources[0]</td>
			<td>string</td>
			<td><pre lang="json">
"arn:aws:s3:::nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].statements[0].resources[1]</td>
			<td>string</td>
			<td><pre lang="json">
"arn:aws:s3:::nubus/*"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"nubus-read"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[1].statements[0].actions[0]</td>
			<td>string</td>
			<td><pre lang="json">
"s3:GetBucketLocation"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[1].statements[0].actions[1]</td>
			<td>string</td>
			<td><pre lang="json">
"s3:GetObject"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[1].statements[0].effect</td>
			<td>string</td>
			<td><pre lang="json">
"Allow"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[1].statements[0].resources[0]</td>
			<td>string</td>
			<td><pre lang="json">
"arn:aws:s3:::nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[1].statements[0].resources[1]</td>
			<td>string</td>
			<td><pre lang="json">
"arn:aws:s3:::nubus/*"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.usersExistingSecrets[0]</td>
			<td>string</td>
			<td><pre lang="json">
"nubus-minio-provisioning"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.tls.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.tls.existingSecret</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-minio-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.tls.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.tls.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.tls.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.tls.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.authorizationApi.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"udmDataAdapterPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.authorizationApi.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-guardian-udm-secret\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.authorizationApi.udm.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.managementApi.oauth.auth.existingSecret.keyMapping.clientSecret</td>
			<td>string</td>
			<td><pre lang="json">
"oauthAdapterM2mSecret"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.managementApi.oauth.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-guardian-keycloak-client-secret\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"guardian"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"guardian"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.postgresql.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-guardian-management-api-postgresql-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"guardian"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.keycloak.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-guardian-provisioning-secret\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.keycloak.auth.existingSecret.keyMapping.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
"admin_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.ldap.auth.bindDn</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubus.keycloak.ldap.auth.bindDn\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-bootstrap-ldap-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-bootstrap"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.handler.appConfig.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.auth.existingSecret.keyMapping.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
"admin_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak_extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-extensions-postgresql-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak_extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.proxy.appConfig.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"info"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.smtp.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-extensions-smtp-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.smtp.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.smtp.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"ldap-notifier"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.ldapServer.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.ldapServer.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"ldap-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.replicaCountPrimary</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.replicaCountProxy</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.replicaCountSecondary</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.ldap.auth.cnAdmin.existingSecret.keyMapping.password }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"license-import"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"notifications-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"notificationsapi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.postgresql.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-notifications-api-postgresql-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"notificationsapi_user"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.postgresql.bundled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.ldap.auth</td>
			<td>object</td>
			<td><pre lang="json">
{
  "existingSecret": {
    "keyMapping": {
      "password": "adminPassword"
    },
    "name": "{{ .Release.Name }}-ldap-server-credentials"
  }
}
</pre>
</td>
			<td>Optional reference to a different secret containing credentials</td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.ldap.tls.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.ldap.tls.existingSecret</td>
			<td>object</td>
			<td><pre lang="json">
{
  "keyMapping": {
    "ca.crt": null,
    "tls.crt": null,
    "tls.key": null
  },
  "name": null
}
</pre>
</td>
			<td>Optional reference to the secret to use for reading certificates</td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-consumer"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.objectStorage.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-portal-consumer-minio-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.objectStorage.bucketName</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.objectStorage.endpoint</td>
			<td>string</td>
			<td><pre lang="json">
"http://{{ .Release.Name }}-minio:9000"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.portalConsumer.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-primary"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.provisioningApi.auth</td>
			<td>object</td>
			<td><pre lang="json">
{
  "existingSecret": {
    "keyMapping": {
      "password": "PROVISIONING_API_PASSWORD"
    },
    "name": "{{ .Release.Name }}-portal-consumer-credentials"
  },
  "password": "",
  "username": "portal-consumer"
}
</pre>
</td>
			<td>Authentication parameters</td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.provisioningApi.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>The password to authenticate with. A secret will be created if existingSecret is not set.</td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.provisioningApi.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"portal-consumer"
</pre>
</td>
			<td>The username to authenticate with. A secret will be created if existingSecret is not set.</td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.provisioningApi.connection.baseUrl</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"http://%s-provisioning-api\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-frontend"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.objectStorage.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-portal-server-minio-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.objectStorage.bucketName</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.objectStorage.endpoint</td>
			<td>string</td>
			<td><pre lang="json">
"http://{{ .Release.Name }}-minio:9000"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.portalServer.centralNavigation.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-portal-server-central-navigation-shared-secret"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-ums-svc-portal-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.admin.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"ADMIN_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.admin.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-api-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.eventsUdm.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"EVENTS_PASSWORD_UDM"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.eventsUdm.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-api-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.prefill.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"PREFILL_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.prefill.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-api-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.prefillPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.auth.udmTransformerPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.config.LOG_LEVEL</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.nats.auth.existingSecret.keyMapping.provisioningApiPassword</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.nats.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-api-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.nats.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.nats.connection.password.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.nats.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.api.nats.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"events_and_consumer_api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.dispatcher.config.LOG_LEVEL</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.dispatcher.nats.auth.existingSecret.keyMapping.dispatcherPassword</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.dispatcher.nats.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-dispatcher-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.dispatcher.nats.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.dispatcher.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.dispatcher.nats.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.ldap.auth.cnAdmin.existingSecret.keyMapping.password }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-ldap-server-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"provisioning"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.auth.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.cluster.replicas</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.password</td>
			<td>string</td>
			<td><pre lang="json">
"$NATS_UDM_LISTENER_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.permissions.publish</td>
			<td>string</td>
			<td><pre lang="json">
"\u003e"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.permissions.subscribe</td>
			<td>string</td>
			<td><pre lang="json">
"\u003e"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.user</td>
			<td>string</td>
			<td><pre lang="json">
"udmlistener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_UDM_LISTENER_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[0].valueFrom.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[0].valueFrom.secretKeyRef.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-udm-listener-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[1].valueFrom.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"admin_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[1].valueFrom.secretKeyRef.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-nats-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[2].name</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PROVISIONING_API_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[2].valueFrom.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[2].valueFrom.secretKeyRef.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-api-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[3].name</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_DISPATCHER_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[3].valueFrom.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[3].valueFrom.secretKeyRef.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-dispatcher-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[4].name</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_UDM_TRANSFORMER_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[4].valueFrom.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[4].valueFrom.secretKeyRef.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-udm-transformer-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[5].name</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PREFILL_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[5].valueFrom.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.extraEnvVars[5].valueFrom.secretKeyRef.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-prefill-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.global.imageRegistry</td>
			<td>string</td>
			<td><pre lang="json">
"docker.io"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.config.LOG_LEVEL</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.nats.auth.existingSecret.keyMapping.prefillPassword</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.nats.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-prefill-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.nats.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.nats.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.createUsers.portalConsumer.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"portal-consumer.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.createUsers.portalConsumer.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-provisioning-register-consumers-json-secrets\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.createUsers.selfserviceConsumer.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.createUsers.selfserviceConsumer.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-provisioning-register-consumers-json-secrets\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.udmTransformer.config.LOG_LEVEL</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.udmTransformer.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-primary"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.udmTransformer.nats.auth.existingSecret.keyMapping.udmTransformerPassword</td>
			<td>string</td>
			<td><pre lang="json">
"NATS_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.udmTransformer.nats.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-udm-transformer-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.udmTransformer.nats.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.nats.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.provisioningApi.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"PROVISIONING_API_PASSWORD"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.provisioningApi.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-selfservice-listener-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.provisioningApi.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.provisioningApi.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"stack-data-ums"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-memcached\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-postgresql\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
"5432"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.stackDataContext.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.ldap.primary.host\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.stackDataContext.ldapMasterHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.ldap.primary.host\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.initialPasswordAdministrator</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.credentials.administrator.password\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.ldapSearchUsers</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.ldapSystemUsers[0].lastname</td>
			<td>string</td>
			<td><pre lang="json">
"LDAP-system-User"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.ldapSystemUsers[0].password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.credentials.ldap.users.readonly.password\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.ldapSystemUsers[0].username</td>
			<td>string</td>
			<td><pre lang="json">
"readonly"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.readonlyUserPassword</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.credentials.ldap.users.readonly.password\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.svcPortalServerUserPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.config.debugLevel</td>
			<td>string</td>
			<td><pre lang="json">
"2"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.ldap.auth.bindDn</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin,dc=example,dc=org"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.ldap.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.ldap.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"provisioning-udm-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.nats.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ingress.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"udm-rest-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.udmRestApi.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.ldap.auth.cnAdmin.existingSecret.keyMapping.password }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.udmRestApi.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-ldap-server-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.udmRestApi.ldap.baseDn</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.udmRestApi.ldap.uri</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"umc-gateway"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"certificates"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"certificates"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[0].secret.secretName</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-saml-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.global.imageRegistry</td>
			<td>string</td>
			<td><pre lang="json">
"docker.io"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.image.registry</td>
			<td>string</td>
			<td><pre lang="json">
"artifacts.software-univention.de"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.ldap.existingSecret.keyMapping.ldapPasswordKey</td>
			<td>string</td>
			<td><pre lang="json">
"ldap.secret"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.ldap.existingSecret.keyMapping.machinePasswordKey</td>
			<td>string</td>
			<td><pre lang="json">
"machine.secret"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.ldap.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-ldap-credentials\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.auth.existingPasswordSecret</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-memcached-credentials\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-memcached-credentials\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"umcserver"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.containerSecurityContext.readOnlyRootFilesystem</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"umc-server-memcached"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"umc-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-postgresql-credentials\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.proxy.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.smtp.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-smtp-credentials\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.umcServer.certPemFile</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl/tls.crt"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.umcServer.privateKeyFile</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl/tls.key"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.existingSecret</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-postgresql-credentials"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.secretKeys.adminPasswordKey</td>
			<td>string</td>
			<td><pre lang="json">
"admin_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.secretKeys.replicationPasswordKey</td>
			<td>string</td>
			<td><pre lang="json">
"replication_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.secretKeys.userPasswordKey</td>
			<td>string</td>
			<td><pre lang="json">
"user_password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.primary.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.allowPrivilegeEscalation</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.capabilities.drop[0]</td>
			<td>string</td>
			<td><pre lang="json">
"ALL"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.privileged</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.readOnlyRootFilesystem</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.runAsGroup</td>
			<td>int</td>
			<td><pre lang="json">
1001
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.runAsNonRoot</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.runAsUser</td>
			<td>int</td>
			<td><pre lang="json">
1001
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.seLinuxOptions</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.containerSecurityContext.seccompProfile.type</td>
			<td>string</td>
			<td><pre lang="json">
"RuntimeDefault"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.image.registry</td>
			<td>string</td>
			<td><pre lang="json">
"docker.io"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"bitnami/postgresql"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.image.tag</td>
			<td>string</td>
			<td><pre lang="json">
"15.4.0-debian-11-r45"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.ttlSecondsAfterFinished</td>
			<td>int</td>
			<td><pre lang="json">
30
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.tls.certCaFilename</td>
			<td>string</td>
			<td><pre lang="json">
"ca.crt"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.tls.certFilename</td>
			<td>string</td>
			<td><pre lang="json">
"tls.crt"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.tls.certKeyFilename</td>
			<td>string</td>
			<td><pre lang="json">
"tls.key"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.tls.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.tls.existingSecret</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-postgresql-tls"
</pre>
</td>
			<td></td>
		</tr>
	</tbody>
</table>

