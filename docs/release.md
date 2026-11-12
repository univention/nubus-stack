# Release

A Nubus for Kubernetes release consists of the release notes in the
[nubus-docs repository](https://git.knut.univention.de/univention/dev/docs/nubus-docs)
and the Helm Chart artifacts from this repository.
A protected `vX.Y.Z` tag on `main` releases the artifacts.
Merging into `main` publishes only a development build to the `nubus-dev` registry project.
Its version is the version of the last release with the suffix `-post-main`.

## Plan the release

### Version and scope

The team releases once every sprint.
Sprints start on Wednesday and end on Tuesday,
so the release usually happens on Tuesday or Wednesday.

The team usually decides ahead of time whether the release is a minor or a patch.
If you are unsure,
check the commits on `main` since the last tag
and ask in the daily or the `#NubusCore` Rocket.Chat channel.

The release contains whatever is on `main` when you start the end-to-end tests.
Optionally, ask in the daily beforehand whether everything critical is on `main`.

### Release notes content

Developers add the release notes entries for their changes
to the `next-release` branch of the nubus-docs repository with their own merge requests.
The first developer who adds an entry after a release also creates the version heading,
and guesses the version.
If the last release was 1.24.1, the first entry might go under 1.24.2,
and a later entry under 1.25.0.

Check that every entry is under the version that you release.
The pipeline reads the release version from the version label, for example `.. _v1.24.2:`.
For how to write entries and version headings, see the
[release notes README](https://git.knut.univention.de/univention/dev/docs/nubus-docs/-/blob/main/docs/nubus-kubernetes-release-notes/README.md).

The tech lead writes the release highlights for a minor release.
If the release highlights are missing, contact the tech lead.

## Prepare the release

### Start the end-to-end tests

Start all manual jobs in the `deploy` stage of the most recent `main` pipeline.
Note the commit SHA of that pipeline. You tag this commit later.

The tests take about an hour.
They must pass before you release the Helm Chart.

### Review the open vulnerabilities

Open the
[vulnerability report of `nubus:main`](https://univention.gitpages.knut.univention.de/dev/tooling/vulnerability-management/nubus/main/).
It lists the open vulnerabilities of the chart's images by audience.

The security update issue of the sprint resolves most vulnerabilities of the application audience,
so expect few of them.

The base image audience usually has more open vulnerabilities.

In both audiences, a vulnerability that is still open on the day of the release
most likely doesn't affect Nubus.
Use your judgment to decide whether it has to delay the release.
If you are unsure, ask in the `#NubusCore` Rocket.Chat channel.

Look closer at the vulnerabilities that the report marks as likely exploited.
A vulnerability is likely exploited when it is on the CISA Known Exploited Vulnerabilities (KEV) list,
when its EPSS score is 10% or more,
or when its EPSS percentile is 95 or more.
The report shows the EPSS values of these vulnerabilities in red
and counts them in the *likely exploited* tile.
To see only them, select *Likely exploited* in the filter bar.

Triage each likely exploited vulnerability
and raise it in the `#NubusCore` Rocket.Chat channel.
For how to triage, see
[Vulnerability scanning](https://univention.gitpages.knut.univention.de/dev/internal/dev-handbook/tools/vulnerability-scanning.html)
in the development handbook.

The `validate-vulnerabilities` job of the tag pipeline checks the same vulnerabilities for the release.
It can fail without stopping the pipeline.

### Prepare the release notes

1. Create a merge request from the `next-release` branch to `main` in the
   [nubus-docs repository](https://git.knut.univention.de/univention/dev/docs/nubus-docs).

1. Set the release date for the version and commit the change.

1. Rebase `next-release` on `main`, because `main` gets commits independently of `next-release`:

   ```console
   $ git fetch
   $ git rebase --rebase-merges origin/main
   $ git push --force-with-lease origin next-release
   ```

Every push to `next-release` runs the `prepare-release-docs-pipeline`.
It adds generated commits for the release version,
the Helm Chart values references, and the fixed CVEs.
Review those commits.

The validation job of that pipeline fails until you push the release tag.
The chart of the new version doesn't exist yet,
so the pipeline uses the `-post-main` development build of `main`.

Don't merge the merge request yet.

## Release

### Tag the Helm Chart

Check the end-to-end tests that you started.
If a job is red, retry it,
or run the failing tests manually against the deployment
as described in the README of the
[e2e-tests repository](https://git.knut.univention.de/univention/dev/nubus-for-k8s/e2e-tests).
If a test keeps failing, don't release. Raise it in the `#NubusCore` Rocket.Chat channel.

Tag the commit that you tested:

```console
$ git fetch
$ git tag --annotate vX.Y.Z --message "Nubus X.Y.Z" TESTED_COMMIT_SHA
$ git push origin vX.Y.Z
```

Replace `X.Y.Z` with the release version
and `TESTED_COMMIT_SHA` with the commit SHA that you noted.

Follow the pipeline of the tag on the
[tags page](https://git.knut.univention.de/univention/dev/nubus-for-k8s/nubus-helm/-/tags).

The pipeline publishes the chart to the public `nubus` registry project.
The `verify-image-signatures` job then verifies the cosign signature of every image in the chart.
If it fails, the job log lists the unsigned images,
and the pipeline doesn't announce the release.
At the end, the pipeline sends the release email and posts a Rocket.Chat message.

### Publish the release notes

The release email says that the release notes can take up to an hour to go online,
so publish them right after the tag pipeline succeeds.

1. Run the pipeline of the `next-release` merge request again.
   It now uses the released chart, and the validation job passes.

1. Merge the merge request.
   You don't need an approval.

The `main` pipeline of the nubus-docs repository publishes the release notes
and creates the tile on the documentation overview page.

## After the release

A nightly pipeline in the nubus repository updates the Nubus version in the
[`publiccode.yml` file](https://git.knut.univention.de/univention/dev/web/nubus/-/blob/main/publiccode.yml).
You don't need to do anything.
