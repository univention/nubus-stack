# ums

The Univention Management Stack

- **Version**: 0.0.1
- **Type**: application
- **AppVersion**:

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

To uninstall the chart with the release name `portal-server`:

```console
helm uninstall ums
```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | notifications-api | 0.* |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-frontend | 0.* |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-listener | 0.* |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-server | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/common-helm/helm | common | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-ldap/helm | ldap-notifier | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-ldap/helm | ldap-server | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-store-dav/helm | store-dav | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-udm-rest/helm | udm-rest-api | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-umc/helm | umc-gateway | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-umc/helm | umc-server | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/provisioning/helm | provisioning | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm | stack-data-swp | 0.* |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/stack-data/helm | stack-data-ums | 0.* |

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
			<td>tags.pre-release</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Components which are not yet fully integrated or not yet feature complete are flagged with this tag. The intention is to make it easy to follow the development progress for evaluation purposes.</td>
		</tr>
	</tbody>
</table>

