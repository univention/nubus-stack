#!/usr/bin/env sh
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2026 Univention GmbH

# Helm post-renderer: rewrite Ingress paths with `path: /$` from
# `pathType: Exact` to `pathType: ImplementationSpecific`.
#
# Reason: the cluster's ingress-nginx admission webhook rejects the
# Exact + "/$" combination, but older Nubus chart versions (used as the
# pre-upgrade baseline in UPGRADE_TEST) still emit it. See
# https://github.com/kubernetes/ingress-nginx/issues/10631
set -eu
exec yq '(select(.kind == "Ingress") | .spec.rules[].http.paths[] | select(.path == "/$") | .pathType) = "ImplementationSpecific"'
