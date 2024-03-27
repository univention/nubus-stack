# Development

## Hints

### Symbolic links in `charts`

Symbolic links can be useful during development. When using symbolic links
inside the folder `helm/nubus/charts`, then the `.tgz` packages can cause
trouble during the evaluation.

Example command:

```sh
for x in $(find charts -type l); do rm $x*.tgz; done
```
