# Label usage

Overview of common label usage within the umbrella chart and its sub-charts.


## General approach

- We strive to use Kubernetes' well-known labels where appropriate.


## Resources managed at run-time

For Kubernetes resources which are managed at run-time we use the Label
`app.kubernetes.io/managed-by` to indicate which component is responsible for
the resource.

The first example has been the `ldap-server` which does track status about the
initialization of the directory content as shown in the following excerpt:

```yaml
kind: ConfigMap
metadata:
  labels:
    app.kubernetes.io/managed-by: ldap-server-evaluate-database-init
  name: nubus-ldap-server-status
```


## Pointers

- Well-Known Labels, Annotations and Taints in Kubernetes -
  <https://kubernetes.io/docs/reference/labels-annotations-taints/>
