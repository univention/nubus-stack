# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH

import pytest

from upgrade_version.upgrade_version import SimpleSemver, find_upgrade_version


@pytest.fixture
def versions() -> list[SimpleSemver]:
    return [
        SimpleSemver.from_dotted("1.15.2"),
        SimpleSemver.from_dotted("1.15.1"),
        SimpleSemver.from_dotted("1.14.1"),
        SimpleSemver.from_dotted("1.14.0"),
    ]


@pytest.mark.parametrize(
    "current,expected",
    [
        (SimpleSemver.from_dotted("1.16.0"), SimpleSemver.from_dotted("1.15.2")),
        (SimpleSemver.from_dotted("1.15.0"), SimpleSemver.from_dotted("1.14.1")),
        (SimpleSemver.from_dotted("1.15.2"), SimpleSemver.from_dotted("1.14.1")),
        (SimpleSemver.from_dotted("1.15.3"), SimpleSemver.from_dotted("1.14.1")),
        (SimpleSemver.from_dotted("2.0.0"), SimpleSemver.from_dotted("1.15.2")),
        (SimpleSemver.from_dotted("1.13.0"), None),
        (SimpleSemver.from_dotted("1.15.2"), SimpleSemver.from_dotted("1.14.1")),
        (SimpleSemver.from_dotted("1.16.0-rc.1"), SimpleSemver.from_dotted("1.15.2")),
    ],
)
def test_find_upgrade_version(
    versions: list[SimpleSemver], current: SimpleSemver, expected: SimpleSemver
):
    res = find_upgrade_version(current, versions)

    assert res == expected
