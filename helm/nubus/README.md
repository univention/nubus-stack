# nubus

Univention Nubus

- **Version**: 0.0.1
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
| oci://artifacts.software-univention.de/nubus/charts | nubusGuardian(guardian) | 0.9.1 |
| oci://artifacts.software-univention.de/nubus/charts | keycloak(keycloak) | 0.1.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusKeycloakBootstrap(keycloak-bootstrap) | 0.1.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusKeycloakExtensions(keycloak-extensions) | 0.8.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLdapNotifier(ldap-notifier) | 0.15.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLdapServer(ldap-server) | 0.17.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusNotificationsApi(notifications-api) | 0.27.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalFrontend(portal-frontend) | 0.27.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalListener(portal-listener) | 0.24.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalServer(portal-server) | 0.27.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusProvisioning(provisioning) | 0.28.3 |
| oci://artifacts.software-univention.de/nubus/charts | nubusSelfServiceListener(selfservice-listener) | 0.6.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusStackDataSwp(stack-data-swp) | 0.52.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusStackDataUms(stack-data-ums) | 0.52.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUdmListener(udm-listener) | 0.28.3 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUdmRestApi(udm-rest-api) | 0.19.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUmcGateway(umc-gateway) | 0.24.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUmcServer(umc-server) | 0.24.1 |
| oci://registry-1.docker.io/bitnamicharts | common | ^2.x.x |
| oci://registry-1.docker.io/bitnamicharts | minio | ^14.6.19 |
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
"{{ .Release.Name }}-stack-data-swp-ucr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.configMapUcrDefaults</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-ums-ucr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.configMapUcrForced</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.credentialOverride.defaultUsers.defaultAdminPassword</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.credentialOverride.defaultUsers.defaultUserPassword</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.credentialOverride.ldapServer.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
""
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
			<td>global.extensions</td>
			<td>list</td>
			<td><pre lang="json">
[
  {
    "image": {
      "imagePullPolicy": "IfNotPresent",
      "registry": "artifacts.software-univention.de",
      "repository": "nubus/images/ox-extension",
      "tag": "0.10.0"
    },
    "name": "ox"
  }
]
</pre>
</td>
			<td>Extensions to load. Add entries to load additional extensions into Nubus. Interim this value is pre-configured with the typical extensions loaded in the openDesk integration of Nubus to allow for a smooth transition. On the long run this value will become an empty list by default.</td>
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
			<td>global.nubusMasterPassword</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Master password from which other passwords are derived.</td>
		</tr>
		<tr>
			<td>global.objectStorage.bucket</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.objectStorage.connection.endpoint</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.objectStorage.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.objectStorage.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.objectStorage.connection.protocol</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
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
      "tag": "0.26.3"
    },
    "name": "portal"
  }
]
</pre>
</td>
			<td>Allows to configure the system extensions to load. This is intended for internal usage, prefer to use `global.extensions` for user configured extensions.</td>
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
			<td>keycloak.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>minio.defaultBuckets</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
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
"nubus-bucket-policy"
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
			<td>minio.provisioning.policies[0].statements[1].actions[0]</td>
			<td>string</td>
			<td><pre lang="json">
"s3:*"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].statements[1].effect</td>
			<td>string</td>
			<td><pre lang="json">
"Allow"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].statements[1].resources[0]</td>
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
			<td>nubusGuardian.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
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
			<td>nubusGuardian.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"guardian"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusGuardian.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"guardian"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.postgresql.bundled</td>
			<td>bool</td>
			<td><pre lang="json">
false
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
			<td>nubusGuardian.provisioning.config.keycloak.admin</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.config.keycloak.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.config.managementApi.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"managementApiClientSecret"
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
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusKeycloakExtensions.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusKeycloakExtensions.smtp.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusLdapServer.extraVolumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/lib/univention-ldap-local/local-schema/opendeskFileshare.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-schemas"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[0].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"opendeskFileshare.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[1].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/lib/univention-ldap-local/local-schema/opendeskKnowledgemanagement.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-schemas"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[1].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"opendeskKnowledgemanagement.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[2].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/lib/univention-ldap-local/local-schema/opendeskLearnmanagement.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[2].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-schemas"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[2].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"opendeskLearnmanagement.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[3].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/lib/univention-ldap-local/local-schema/opendeskLivecollaboration.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[3].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-schemas"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[3].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"opendeskLivecollaboration.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[4].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/lib/univention-ldap-local/local-schema/opendeskProjectmanagement.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[4].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-schemas"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumeMounts[4].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"opendeskProjectmanagement.schema"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumes[0].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-schemas"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.extraVolumes[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-schemas"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.highAvailabilityMode</td>
			<td>bool</td>
			<td><pre lang="json">
true
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
			<td>nubusLdapServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
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
			<td>nubusNotificationsApi.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
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
			<td>nubusNotificationsApi.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusPortalFrontend.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/www/html/favicon.ico"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[0].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"favicon.ico"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[1].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/www/html/css/custom.css"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[1].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"custom.css"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[2].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/www/html/icons/logo.svg"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[2].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[2].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"logo.svg"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[3].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/www/html/icons/logo_small_border.svg"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[3].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[3].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"logo_small_border.svg"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[4].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/www/html/custom/portal_background_image.png"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[4].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[4].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"portal_background_image.png"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[5].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/www/html/custom/portal_background_image.svg"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[5].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumeMounts[5].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"portal_background_image.svg"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumes[0].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.extraVolumes[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"opendesk-branding"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
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
			<td>nubusPortalListener.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.portalListener.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-primary"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.portalListener.objectStorageBucket</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalListener.terminationGracePeriodSeconds</td>
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
			<td>nubusPortalServer.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
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
			<td>nubusPortalServer.portalServer.objectStorageBucket</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
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
			<td>nubusProvisioning.dispatcher.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.dispatcher.nats.connection.password.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusProvisioning.dispatcher.nats.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"dispatcher"
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
			<td>nubusProvisioning.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"provisioning"
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
			<td>nubusProvisioning.prefill.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.nats.connection.password.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusProvisioning.prefill.nats.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"prefill"
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
			<td>nubusSelfServiceListener.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.provisioningApi.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceListener.umc.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"Administrator"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"stack-data-swp"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.stackDataContext.ldapSystemUsers[0].password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.credentials.ldap.users.readonly.password\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.stackDataContext.ldapSystemUsers[0].username</td>
			<td>string</td>
			<td><pre lang="json">
"readonly"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.stackDataSwp.loadDevData</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataSwp.terminationGracePeriodSeconds</td>
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
			<td>nubusStackDataUms.nubusKeycloakBootstrap.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakBootstrap.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-bootstrap"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakBootstrap.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakBootstrap.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakBootstrap.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakBootstrap.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakBootstrap.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.keycloak.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.keycloak.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak_extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak_extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.smtp.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.smtp.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.smtp.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusKeycloakExtensions.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"notifications-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"notificationsapi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"notificationsapi_user"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.postgresql.bundled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusNotificationsApi.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.portalListener.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-primary"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.portalListener.objectStorageBucket</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalListener.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.portalServer.objectStorageBucket</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusPortalServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.api.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.api.nats.connection.password.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.api.nats.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.api.nats.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"events_and_consumer_api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.dispatcher.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.dispatcher.nats.connection.password.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.dispatcher.nats.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.dispatcher.nats.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"dispatcher"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"provisioning"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.global.imageRegistry</td>
			<td>string</td>
			<td><pre lang="json">
"docker.io"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.natsBox.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.natsBox.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.natsBox.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.natsBox.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.reloader.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.reloader.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.reloader.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.reloader.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.nats.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.prefill.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.prefill.nats.connection.password.secretKeyRef.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.prefill.nats.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.prefill.nats.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"prefill"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.api.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.api.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.api.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.api.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.dispatcher.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.dispatcher.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.dispatcher.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.dispatcher.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.prefill.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.prefill.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.prefill.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.resources.prefill.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusProvisioning.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.provisioningApi.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusSelfServiceListener.umc.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"Administrator"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"stack-data-swp"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.stackDataContext.ldapSystemUsers[0].password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.credentials.ldap.users.readonly.password\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.stackDataContext.ldapSystemUsers[0].username</td>
			<td>string</td>
			<td><pre lang="json">
"readonly"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.stackDataSwp.loadDevData</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusStackDataSwp.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.config.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-primary"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.ldap.auth.bindDn</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin,dc=example,dc=org"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.ldap.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.ldap.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"provisioning-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmListener.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/lib/python3/dist-packages/univention/admin/hooks.d/AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumeMounts[0].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumeMounts[1].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/share/attribute-to-group-mapper/flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumeMounts[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumeMounts[1].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumes[0].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.extraVolumes[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.ldap.auth.bindDn</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin,dc=example,dc=org"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.ldap.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.ldap.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"udm-rest-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUdmRestApi.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"certificates"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[1].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/entrypoint.d/90-customization.sh"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"entrypoint-swp-patches"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[1].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"90-customization.sh"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[2].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/lib/python3/dist-packages/univention/admin/hooks.d/AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[2].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[2].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[3].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/share/attribute-to-group-mapper/flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[3].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[3].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[4].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/share/univention-management-console/modules/udm-portals-announcement.xml"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[4].name</td>
			<td>string</td>
			<td><pre lang="json">
"announcements-customization"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumeMounts[4].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"udm-portals-announcement.xml"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"certificates"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[0].secret.secretName</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-saml-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[1].configMap.defaultMode</td>
			<td>int</td>
			<td><pre lang="json">
365
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[1].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-umc-server-entrypoint"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"entrypoint-swp-patches"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[2].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[2].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[3].configMap.defaultMode</td>
			<td>int</td>
			<td><pre lang="json">
292
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[3].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-umc-server-announcements"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.extraVolumes[3].name</td>
			<td>string</td>
			<td><pre lang="json">
"announcements-customization"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.global.imageRegistry</td>
			<td>string</td>
			<td><pre lang="json">
"docker.io"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.image.registry</td>
			<td>string</td>
			<td><pre lang="json">
"artifacts.software-univention.de"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"memcached-password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.auth.credentialSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.auth.existingPasswordSecret</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-memcached-credentials\" .Release.Name }}"
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
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.connection.username</td>
			<td>string</td>
			<td><pre lang="json">
"umcserver"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.containerSecurityContext.readOnlyRootFilesystem</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"umc-server-memcached"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"umc-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.umcServer.certPemFile</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl/tls.crt"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.umcServer.privateKeyFile</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl/tls.key"
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
			<td>nubusStackDataUms.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.config.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-primary"
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
"provisioning-listener"
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
			<td>nubusUdmRestApi.extraVolumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/lib/python3/dist-packages/univention/admin/hooks.d/AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.extraVolumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.extraVolumeMounts[0].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.extraVolumeMounts[1].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/share/attribute-to-group-mapper/flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.extraVolumeMounts[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.extraVolumeMounts[1].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.extraVolumes[0].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.extraVolumes[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
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
			<td>nubusUdmRestApi.ldap.auth.bindDn</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin,dc=example,dc=org"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ldap.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ldap.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
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
			<td>nubusUmcGateway.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
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
			<td>nubusUmcServer.extraVolumeMounts[1].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/entrypoint.d/90-customization.sh"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"entrypoint-swp-patches"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[1].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"90-customization.sh"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[2].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/lib/python3/dist-packages/univention/admin/hooks.d/AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[2].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[2].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"AttributeToGroupMapper.py"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[3].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/share/attribute-to-group-mapper/flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[3].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[3].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"flag_to_group_mapping.json"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[4].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/usr/share/univention-management-console/modules/udm-portals-announcement.xml"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[4].name</td>
			<td>string</td>
			<td><pre lang="json">
"announcements-customization"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[4].subPath</td>
			<td>string</td>
			<td><pre lang="json">
"udm-portals-announcement.xml"
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
			<td>nubusUmcServer.extraVolumes[1].configMap.defaultMode</td>
			<td>int</td>
			<td><pre lang="json">
365
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[1].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-umc-server-entrypoint"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[1].name</td>
			<td>string</td>
			<td><pre lang="json">
"entrypoint-swp-patches"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[2].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[2].name</td>
			<td>string</td>
			<td><pre lang="json">
"attribute-to-group-mapper-hook"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[3].configMap.defaultMode</td>
			<td>int</td>
			<td><pre lang="json">
292
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[3].configMap.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-swp-umc-server-announcements"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[3].name</td>
			<td>string</td>
			<td><pre lang="json">
"announcements-customization"
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
			<td>nubusUmcServer.ingress.annotations."cert-manager.io/cluster-issuer"</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.certManagerIssuer }}"
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
			<td>nubusUmcServer.memcached.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"memcached-password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.auth.credentialSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
""
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
			<td>nubusUmcServer.memcached.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.memcached.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
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
			<td>nubusUmcServer.postgresql.auth.credentialSecret.key</td>
			<td>string</td>
			<td><pre lang="json">
"password"
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
			<td>nubusUmcServer.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
""
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
		<tr>
			<td>ucrForcedValues</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Load data to override ucr variables. example: ucrForcedValues: |   portal/auth-mode: ucs</td>
		</tr>
	</tbody>
</table>

