# ums

The Univention Management Stack

- **Version**: 0.0.1
- **Type**: application
- **AppVersion**:
{%- if chart.home %}
-
{%- end %}

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
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | notifications-api | ^0.9.2 |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-frontend | ^0.9.2 |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-listener | ^0.9.2 |
| oci://gitregistry.knut.univention.de/univention/components/univention-portal/helm | portal-server | ^0.9.2 |
| oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/container-store-dav/helm | store-dav | ^0.2.0 |

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

