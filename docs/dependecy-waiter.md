# Dependency waiter setup

It's common to need to wait for dependencies before our containers can start running.
For that reason we have a container dedicated to wait for dependencies.
(container-wait-for-dependencies)[https://git.knut.univention.de/univention/customers/dataport/upx/container-wait-for-dependencies]

## Configure wait-for-dependencies container

We want to keep consistency over all our charts on how to define and configure the dependency waiter
on each char. The agreed form is the following:

```yaml
# Configures an init container that waits for X to be ready
waitForDependency:
  enabled: true
  image:
    imagePullPolicy: "IfNotPresent"
    registry: ""
    repository: "nubus/images/wait-for-dependency"
    tag: "0.26.0@sha256:a31fde86bf21c597a31356fe492ab7e7a03a89282ca215eb7100763d6eb96b6b"
```

Keeping this consistent between repositories will help to easily identify and modified the dependency waiters.
