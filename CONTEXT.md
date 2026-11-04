# Nubus Helm chart, secrets

The language an operator uses when giving the `nubus` chart its sensitive data.

## Language

**Credential**:
A password, token or key the chart needs for one purpose, such as the Keycloak PostgreSQL password.
_Avoid_: secret (that is the Kubernetes object), password (when the value is a key or token)

**Seed**:
The value at `global.secrets.masterPassword`, from which the chart derives generated passwords.
_Avoid_: master password (legacy key name only), master seed

**Generated password**:
A credential value the chart makes up itself, either derived from the seed or random.
_Avoid_: auto-generated secret, derived secret

**Custom value**:
A credential value the operator writes in the values file, which the chart renders into a Secret.
_Avoid_: provided secret value, plain value

**Existing secret**:
A Kubernetes Secret the operator creates, which the chart references by name and key and never renders.
_Avoid_: external secret, bring-your-own secret

**Generation toggle**:
The switch `global.secrets.generatePasswords`. When off, the chart generates no password and ignores the seed.
_Avoid_: strict mode
