# ums-stack

The Univention Management Stack

- **Version**: 0.0.1
- **Type**: application
- **AppVersion**:
{%- if chart.home %}
-
{%- end %}

## TL;DR

```console
helm upgrade --install ums-stack oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/ums-stack/helm/ums-stack
```

## Introduction

This chart does install the Univention Management Stack.

## Installing

To install the chart with the release name `ums-stack`:

```console
helm upgrade --install ums-stack oci://gitregistry.knut.univention.de/univention/customers/dataport/upx/ums-stack/helm/ums-stack
```

## Uninstalling

To uninstall the chart with the release name `portal-server`:

```console
helm uninstall ums-stack
```

