# ums

The Univention Management Stack

- **Version**: 0.0.1
- **Type**: application

## TL;DR

```console
helm upgrade --install ums oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/ums-stack/helm/ums
```

## Introduction

This chart does install the Univention Management Stack.

## Installing

To install the chart with the release name `ums`:

```console
helm upgrade --install ums oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/ums-stack/helm/ums
```

## Uninstalling

To uninstall the chart with the release name `ums`:

```console
helm uninstall ums
```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://gitregistry.knut.univention.de/univention/components/keycloak-extensions/helm | keycloak-extensions | 0.3.2 |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | notifications-api | 0.20.4 |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-frontend | 0.20.4 |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-listener | 0.20.4 |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-server | 0.20.4 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-ldap/helm | ldap-notifier | 0.10.3 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-ldap/helm | ldap-server | 0.10.3 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-udm-rest/helm | udm-rest-api | 0.9.2 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-umc/helm | umc-gateway | 0.11.6 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-umc/helm | umc-server | 0.11.6 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/guardian-helm/helm | guardian | 0.3.0 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/provisioning/helm | provisioning | 0.23.1 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/provisioning/helm | udm-listener | 0.21.3 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/selfservice-listener/helm | selfservice-listener | 0.4.0 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm | stack-data-swp | 0.45.2 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm | stack-data-ums | 0.45.2 |
| oci://registry-1.docker.io/bitnamicharts | common | ^2.x.x |
| oci://registry-1.docker.io/bitnamicharts | minio | 14.1.4 |
| oci://registry-1.docker.io/bitnamicharts | stack-gateway(nginx) | ^15.x.x |
| oci://registry-1.docker.io/bitnamicharts | keycloak-postgresql(postgresql) | ^12.x.x |
| oci://registry.souvap-univention.de/souvap/tooling/charts/univention-keycloak-bootstrap | keycloak-bootstrap(ums-keycloak-bootstrap) | 1.* |
| oci://registry.souvap-univention.de/souvap/tooling/charts/univention-keycloak | keycloak(ums-keycloak) | 1.* |

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
			<td>ldap-server.limits</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>ldap-server.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>ldap-server.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"100m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>ldap-server.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"512Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.defaultBuckets</td>
			<td>string</td>
			<td><pre lang="json">
"ums"
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
			<td>minio.persistence.accessModes[0]</td>
			<td>string</td>
			<td><pre lang="json">
"ReadWriteOnce"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.persistence.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.persistence.mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/bitnami/minio/data"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.persistence.size</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.persistence.storageClass</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.buckets[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"ums"
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
"mc anonymous set download provisioning/ums/portal-assets"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.provisioning.policies[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"ums-bucket-policy"
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
"arn:aws:s3:::ums"
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
"arn:aws:s3:::ums/*"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.natsBox.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"256Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.natsBox.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"100m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.natsBox.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"64Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.reloader.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"256Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.reloader.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"100m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.reloader.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"64Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"100m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.nats.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"64Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.api.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.api.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.api.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"32Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.dispatcher.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.dispatcher.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.dispatcher.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"32Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.prefill.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.prefill.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>provisioning.resources.prefill.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"32Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>tags.pre-release</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Components which are not yet fully integrated or not yet feature complete are flagged with this tag. The intention is to make it easy to follow the development progress for evaluation purposes.</td>
		</tr>
		<tr>
			<td>udm-rest-api.limits</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>udm-rest-api.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>udm-rest-api.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"100m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>udm-rest-api.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"512Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>ums</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Load data to override ucr variables. example: ums:   ucrForcedValues: |     portal/auth-mode: ucs</td>
		</tr>
	</tbody>
</table>

