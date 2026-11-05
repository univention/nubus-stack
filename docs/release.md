# Release

A Nubus for Kubernetes release consists of the release notes in
[nubus-docs](https://git.knut.univention.de/univention/dev/docs/nubus-docs)
and the Helm chart artifacts from this repository.
A protected `vX.Y.Z` tag on `main` releases the artifacts.
Merging into `main` publishes only a development build,
`<last release>-post-main`, to the `nubus-dev` registry project.

## Release notes

### Create and prepare the release notes

1. Create a merge request from the `next-release` branch to `main` in the
   [nubus-docs repository](https://git.knut.univention.de/univention/dev/docs/nubus-docs).

1. Follow the [release notes README](https://git.knut.univention.de/univention/dev/docs/nubus-docs/-/blob/main/docs/nubus-kubernetes-release-notes/README.md).
   It describes the version label the pipeline reads, for example `.. _v1.24.1:`.

### Generated changes

Every push to `next-release` runs the `prepare-release-docs-pipeline`.
It adds generated commits for the release version,
the Helm chart values references, and the fixed CVEs.
Review those commits.

Before you push the release tag, the chart of the new version doesn't exist yet.
The pipeline then uses the development build of `main`, `<previous release>-post-main`,
and the validation job fails.
After you push the release tag, run the pipeline again.
It then uses the released chart, and the validation job passes.

### Verify your changes

Before you push your changes, verify the documentation:

1. Go to the release notes directory:

   ```console
   $ cd docs/nubus-kubernetes-release-notes
   ```

1. Run the spelling checker:

   ```console
   $ make docker-spelling
   ```

1. Check all links:

   ```console
   $ make docker-linkcheck
   ```

1. Preview your changes in a browser:

   ```console
   $ make docker-livehtml
   ```

### Request review

Request a review of the release notes from Nico Gulden (`@ngulden`) from the technical documentation team.

Permissions to merge into `main` in nubus-docs are restrictive.
You may need help to merge, even with the required approvals.

## Helm chart artifacts

### Prepare the release

1. Check that the latest `main` pipeline of this repository succeeded.

1. Run the end-to-end tests: start the manual jobs in the `deploy` stage of that pipeline.

1. Review the open vulnerabilities of the chart's images in the
   [vulnerability report of `nubus:main`](https://univention.gitpages.knut.univention.de/dev/tooling/vulnerability-management/nubus/main/)
   and triage them.

### Push the release tag

Choose the version by the changes since the last release:
a patch release for fixes only, a minor release for new features.

```console
$ git switch main
$ git pull
$ git tag --annotate v1.24.1 --message "Nubus 1.24.1"
$ git push origin v1.24.1
```

`v*` tags are protected. Only a maintainer can push them.

The tag pipeline does the following:

1. It publishes the chart to the `nubus` registry project.
1. It imports the chart's images into Dependency-Track under `nubus:1.24.1`,
   validates them, and attests the VEX document to the images.
1. After every other job succeeded, it creates the GitLab release,
   sends the release mail, and posts the release to `#product-announcements`.

The mail says that the release notes can take up to an hour to go online.
Run the nubus-docs pipeline again and merge the release notes right after the tag pipeline.

### Update the public code metadata

Update the `softwareVersion` and `releaseDate` fields in
[publiccode.yml](https://git.knut.univention.de/univention/dev/nubus/-/blob/main/publiccode.yml).

## After the release

### Close related issues

1. Review all GitLab issues and verify whether they have an associated Bugzilla link.

1. For each issue with a Bugzilla link, close the corresponding Bugzilla bug and mention the fixed version.

1. Move issues from the `waiting for release` status to `Done`.
