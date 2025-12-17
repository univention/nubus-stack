# SPDX-FileCopyrightText: 2024 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re

import pytest

from pytest_helm.helm import HelmChart
from pytest_helm.utils import load_yaml

from .helpers import get_secret_names, find_secret_usages, jsonpaths_from_yaml_file


base_dir = (Path(__file__).parent / "../../").resolve()
CUSTOM_SECRET_VALUES_FILE = base_dir / "helm/nubus/example-custom-secret-values.yaml"
EXISTING_SECRETS_FILE = base_dir / "helm/nubus/example-existing-secret.yaml"
SECRETS_DOCS_PATH = (
    base_dir / "../nubus-docs/docs/nubus-kubernetes-operation/configuration/secrets.rst"
)

"""Ignore secret names in Kubernetes manifest paths that are unrelated to secret"""
PATH_IGNORE_LIST = [
    "metadata.name",
    "configMapRef",
    "serviceAccountName",
]

"""Secrets that currently can't be replaced using existing secrets"""
SECRET_IGNORE_LIST = set(
    (
        "release-name-stack-data-ums-context",
        "release-name-stack-data-ums-svc-portal-server",
    )
)

"""Username configuration paths don't need to be mentioned in the secrets documentation"""
IGNORE_ONLY_CONFIG = set(
    (
        # Usernames don't need to be configured.
        "keycloak.keycloak.auth.username",
        "nubusGuardian.postgresql.auth.username",
        "nubusKeycloakExtensions.smtp.auth.username",
        "nubusStackDataUms.templateContext.ldapSystemUsers[0].username",
        # Will be fixed in follow-up issue
        "nubusKeycloakExtensions.smtp.auth.existingSecret.name",
        "nubusKeycloakExtensions.smtp.auth.existingSecret.keyMapping.password",
        # Unused tls secrets
        "nubusUdmListener.ldap.tlsSecret.name",
        "nubusUmcServer.ldap.tlsSecret.name",
    )
)


@pytest.fixture()
def helm_default_values(request):
    default_values = [
        base_dir / "helm/nubus/linter_values.yaml",
    ]
    return default_values


@pytest.fixture()
def chart_default_path():
    chart_path = base_dir / "helm/nubus"
    return chart_path


def test_existing_secrets_can_be_specified_everywhere(chart: HelmChart, subtests):
    # Disable embedded databases
    values = load_yaml(
        """
        postgresql:
          enabled: false
          provisioning:
            enabled: false
        minio:
          enabled: false
        """
    )

    with ThreadPoolExecutor(max_workers=2) as executor:
        future_baseline = executor.submit(chart.helm_template)
        future_existing = executor.submit(
            chart.helm_template,
            values=values,
            helm_args=["--values", EXISTING_SECRETS_FILE],
        )
        # Template baseline nubus
        baseline_manifests = future_baseline.result()
        # Template existing secrets nubus
        existing_secrets_manifests = future_existing.result()

    baseline_secrets = set(get_secret_names(baseline_manifests)) - SECRET_IGNORE_LIST
    assert baseline_secrets, "No Secret resources found in the baseline render."

    # Test that no baseline secret names are used in the existing secrets manifests
    for resource in existing_secrets_manifests:
        kind = resource["kind"]
        name = resource["metadata"]["name"]
        if kind in (
            "Certificate",
            "ConfigMap",
            "Ingress",
            "Secret",
            "Service",
            "ServiceAccount",
        ):
            continue
        with subtests.test(kind=kind, name=name):
            failures = find_secret_usages(resource, baseline_secrets, PATH_IGNORE_LIST)
            if not failures:
                continue
            details = "\n".join(
                f"- '{secret}' at {section}" for secret, section in failures
            )
            pytest.fail(f"Found baseline secret name(s) in {kind}/{name}:\n{details}")


def test_docs_matches_configuration(subtests):
    docs_text = SECRETS_DOCS_PATH.read_text(encoding="utf-8")
    docs_paths = parse_docs_text(docs_text)

    custom_secret_value_paths = jsonpaths_from_yaml_file(CUSTOM_SECRET_VALUES_FILE)
    existing_secret_paths = jsonpaths_from_yaml_file(EXISTING_SECRETS_FILE)

    config_paths = set(custom_secret_value_paths).union(existing_secret_paths)
    docs_paths_set = set(docs_paths)

    with subtests.test("docs_duplicates"):
        duplicates = [x for x, c in Counter(docs_paths).items() if c > 1]
        assert not duplicates, "duplicates:\n" + "\n".join(sorted(duplicates))

    with subtests.test("only_documented"):
        extra = docs_paths_set - config_paths
        assert not extra, "only in docs:\n" + "\n".join(sorted(extra))

    with subtests.test("only_configured"):
        missing = config_paths - docs_paths_set - IGNORE_ONLY_CONFIG
        # NATS extraEnvVars are documented differently.
        missing = [
            m
            for m in missing
            if not m.startswith("nubusProvisioning.nats.extraEnvVars")
        ]
        assert not missing, "only in config:\n" + "\n".join(sorted(missing))


def parse_docs_text(text: str) -> list:
    heading_pattern = re.compile(r"^List of secrets\n-+$", re.M)
    envvar_pattern = re.compile(r":envvar:`([^`]+)`")

    m = heading_pattern.search(text)
    assert m, "Could not find the 'List of secrets' section header."

    return envvar_pattern.findall(text[m.end() :])
