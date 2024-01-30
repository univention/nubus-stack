# Disclaimer - Work in progress

The repository you are looking into is work in progress.

It contains proof of concept and preview builds in development created in
context of the
[openDesk](https://gitlab.opencode.de/bmi/souveraener_arbeitsplatz/info)
project.

The repository's content provides you with first insights into the containerized
cloud IAM from Univention, derived from the UCS appliance.


# UMS Stack

This repository does contain a Helm chart which allows to install the Univention
Management Stack components.


## Status - EXPERIMENTAL

The umbrella Helm chart for the UMS Stack is being built up in this repository.
The status will be updated once it does stabilize.


## Contact

- Team openDesk Dev
  - <johannes.bornhold.extern@univention.de>


## Example usage

This repository is mainly concerned with the Helm chart for the stack. Please
take a look into the README file of the chart in `./helm/ums/README.md`.


## Development setup

### Known limitations

- The values for a test deployment are currently in the file
  `linter_values.yaml`.
- `keycloak-bootstrap` is currently disabled in `linter_values.yaml`. Use `--set
  keycloak-bootstrap.enabled=true` when you want to run it during development.


### Preparation - Load dependencies

Make sure that you have the dependencies downloaded. You may have to log into
the OCI registry if you did not yet do so before:

```sh
helm registry login gitregistry.knut.univention.de
```

Afterwards the dependencies can be loaded:

```sh
helm dependency build ./helm/ums
```

### Fast feedback loop with `helm template`

Use `helm template` to have a fast feedback loop and inspect the rendered output
as YAML files. This also works if you don't have a Kubernetes cluster available:

```sh
helm template ums ./helm/ums

# Add custom values if you want to check specific scenarios
helm template --values your-values-file.yaml ums ./helm/ums
helm template --set example.key=value ums ./helm/ums

# Be aware, there are further options to set values on the command line,
# "helm template --help" will provide further details.
```


### Deployment into a Kubernetes cluster

If you want to verify changes in a real deployment, then you have to first make
sure to have a Kubernetes cluster available. Typically you would work with the
sub-commands `install`, `upgrade` and `uninstall`:

```sh
# Often the use of "upgrade" with the argument "--install" is useful
helm upgrade --install --values your-values-file.yaml ums ./helm/ums
```


## Related and further information

- Helm project - <https://helm.sh/>
- Helm project documentation regarding umbrella charts -
  <https://helm.sh/docs/howto/charts_tips_and_tricks/#complex-charts-with-many-dependencies>
