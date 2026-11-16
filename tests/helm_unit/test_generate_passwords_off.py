# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

import subprocess
from pathlib import Path

import pytest
from pytest_helm.helm import HelmChart
from pytest_helm.utils import add_jsonpath_prefix

from .helpers import jsonpaths_from_yaml_file

base_dir = (Path(__file__).parent / "../../").resolve()
NO_GENERATION_VALUES = Path(__file__).parent / "values-no-generation.yaml"

# keycloak-extensions requires the username, but no chart generates it.
NOT_A_CREDENTIAL = {"nubusKeycloakExtensions.smtp.auth.username"}
CREDENTIALS = sorted(
    set(jsonpaths_from_yaml_file(NO_GENERATION_VALUES)) - NOT_A_CREDENTIAL
)

# Charts name a credential relative to their own values, and nats is a subchart of provisioning.
NESTED_SUBCHARTS = ("nubusProvisioning.nats",)


@pytest.fixture()
def helm_default_values():
    return [
        base_dir / "helm/nubus/prod-values.yaml",
        base_dir / "helm/nubus/example.yaml",
        NO_GENERATION_VALUES,
    ]


@pytest.fixture()
def chart_default_path():
    return base_dir / "helm/nubus"


def path_in_subchart(credential: str) -> str:
    path = credential.removesuffix(".password")
    for subchart in NESTED_SUBCHARTS:
        if path.startswith(f"{subchart}."):
            return path.removeprefix(f"{subchart}.")
    return path.split(".", 1)[1]


def secret_values(manifests) -> dict[tuple[str, str], str]:
    return {
        (secret["metadata"]["name"], key): str(value)
        for secret in manifests.get_resources(kind="Secret")
        for field in ("data", "stringData")
        for key, value in (secret.get(field) or {}).items()
    }


def seed(value: str | None) -> dict:
    return {"global": {"secrets": {"masterPassword": value}}}


def test_renders_without_a_seed(chart: HelmChart):
    chart.helm_template(seed(None))


@pytest.mark.parametrize("credential", CREDENTIALS)
def test_missing_credential_fails_the_render(chart: HelmChart, credential: str):
    with pytest.raises(subprocess.CalledProcessError) as error:
        chart.helm_template(add_jsonpath_prefix(credential, None))
    assert path_in_subchart(credential) in error.value.stderr


def test_no_secret_value_is_generated(chart: HelmChart):
    """A derived value differs between the seeds, a random one between any two renders."""
    first = secret_values(chart.helm_template(seed("stub-seed-a")))
    second = secret_values(chart.helm_template(seed("stub-seed-b")))
    assert first
    assert first == second
