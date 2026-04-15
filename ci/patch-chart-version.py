#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Univention GmbH
# SPDX-License-Identifier: AGPL-3.0-only

"""Patch global.nubusChartVersion in values.yaml with the release version.

Uses text replacement instead of YAML parsing to preserve anchors,
aliases, comments, and formatting.

Expects environment variables:
    RELEASE_VERSION: the semantic version to set
"""

import logging
import os
import re
import sys

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.INFO)

VALUES_PATH = "helm/nubus/values.yaml"


def patch_chart_version(file_path, version):
    """Replace the nubusChartVersion value in a values.yaml file."""
    with open(file_path, encoding="utf-8") as fh:
        content = fh.read()

    pattern = r"(nubusChartVersion:\s*)\"[^\"]*\""
    replacement = rf'\1"{version}"'
    new_content, count = re.subn(pattern, replacement, content)

    if count == 0:
        logger.warning("nubusChartVersion not found in %s", file_path)
        return

    with open(file_path, "w", encoding="utf-8") as fh:
        fh.write(new_content)

    logger.info("Set global.nubusChartVersion to %s in %s", version, file_path)


if __name__ == "__main__":
    release_version = os.environ.get("RELEASE_VERSION")
    if not release_version:
        logger.error("RELEASE_VERSION is not set")
        sys.exit(1)

    patch_chart_version(VALUES_PATH, release_version)
