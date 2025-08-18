# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH


from pathlib import Path
from typing import Any, Iterable

from pytest_helm.models import KubernetesResource
from ruamel.yaml import YAML


def get_secret_names(manifests: list[KubernetesResource]) -> list[str]:
    return [
        manifest["metadata"]["name"]
        for manifest in manifests
        if manifest["kind"] == "Secret"
    ]


def _dotted(path: list[str | int]) -> str:
    """
    ['spec','template','spec','containers',0,'env',2,'valueFrom','secretKeyRef','name']
    -> "spec.template.spec.containers[0].env[2].valueFrom.secretKeyRef.name"
    """
    out: list[str] = []
    for p in path:
        if isinstance(p, int):
            out[-1] = f"{out[-1]}[{p}]"
        else:
            out.append(str(p))
    return ".".join(out)


def _iter_string_values(obj: Any, path: list[str | int] | None = None) -> Iterable[tuple[str, list[str | int]]]:
    if path is None:
        path = []
    if isinstance(obj, str):
        yield obj, path
        return
    if isinstance(obj, list):
        for i, item in enumerate(obj):
            yield from _iter_string_values(item, path + [i])
        return
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from _iter_string_values(v, path + [k])
        return
    return


def find_secret_usages(resource: dict, forbidden: set[str], ignore_paths: list[str]) -> list[tuple[str, str]]:
    hits: list[tuple[str, str]] = []
    for value, path in _iter_string_values(resource):
        if value in forbidden:
            path_string = _dotted(path)
            if any((ignore in path_string for ignore in ignore_paths)):
                continue
            hits.append((value, path_string))
    return hits


def jsonpaths_from_yaml_file(file: Path):
    yaml = YAML(typ="safe")
    with file.open("r") as f:
        data = yaml.load(f)

    return [_dotted(i) for _, i in _iter_string_values(data)]
