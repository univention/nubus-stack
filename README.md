# Nubus

This repository does contain a Helm chart which allows to install all the Nubus
components.


## Example usage

This repository is mainly concerned with the Helm chart for the stack. Please
take a look into the README file of the chart in `./helm/nubus/README.md`.


## Development setup

### Known limitations

- The values for a test deployment are currently in the file
  `example.yaml`, which you can use as a starting point.

### Preparation - Load dependencies

The dependencies can be loaded:

```sh
helm dependency build ./helm/nubus
```

### Fast feedback loop with `helm template`

Use `helm template` to have a fast feedback loop and inspect the rendered output
as YAML files. This also works if you don't have a Kubernetes cluster available:

```sh
helm template nubus ./helm/nubus

# Add custom values if you want to check specific scenarios
helm template --values your-values-file.yaml nubus ./helm/nubus
helm template --set example.key=value nubus ./helm/nubus

# Be aware, there are further options to set values on the command line,
# "helm template --help" will provide further details.
```


### Deployment into a Kubernetes cluster

If you want to verify changes in a real deployment, then you have to first make
sure to have a Kubernetes cluster available.

Deployments can be made with plain Helm or by using the CI setup via Helmfile in
the subfolder `./ci`. The CI setup is documented in
[./ci/README.md](./ci/README.md).


#### Plain Helm usage

Typically you would work with the sub-commands `install`, `upgrade` and
`uninstall`:

```sh
# Often the use of "upgrade" with the argument "--install" is useful
helm upgrade --install --values your-values-file.yaml nubus ./helm/nubus

# If you want to run the bootstrap job of Keycloak (required on initial deployment)
helm upgrade --install --values linter_values.yaml --set keycloak-bootstrap.enabled=true nubus ./
```


## Related and further information

- Helm project - <https://helm.sh/>
- Helm project documentation regarding umbrella charts -
  <https://helm.sh/docs/howto/charts_tips_and_tricks/#complex-charts-with-many-dependencies>
