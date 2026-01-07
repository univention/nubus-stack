# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH
import os
import re
import subprocess


class SimpleSemver:
    major: int
    minor: int
    patch: int
    rest: str | None
    semver_re: str = r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?P<rest>.*)"

    def __init__(self, major: int, minor: int, patch: int, rest: str | None = None):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.rest = rest

    @classmethod
    def from_dotted(cls, version: str) -> "SimpleSemver":
        """
        Parses a `version` structured like x.y.z
        Allows build metadata and pre-release versions but ignores them for any version comparsions
        """
        res = re.search(cls.semver_re, version)
        assert res, f"invalid semver {version}"
        major = int(res.group("major"))
        minor = int(res.group("minor"))
        patch = int(res.group("patch"))
        rest = res.group("rest")

        return SimpleSemver(major, minor, patch, rest)

    def to_dotted(self) -> str:
        """
        Reconstructs the original semver string
        """
        return f"{self.major}.{self.minor}.{self.patch}{self.rest}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, SimpleSemver):
            return False

        return (
            self.major == value.major
            and self.minor == value.minor
            and self.patch == value.patch
        )

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, SimpleSemver):
            raise NotImplementedError

        if self.major != other.major:
            return self.major < other.major
        if self.minor != other.minor:
            return self.minor < other.minor
        return self.patch < other.patch

    def __repr__(self) -> str:
        return f"SimpleSemver({self.major}, {self.minor}, {self.patch}, '{self.rest}')"


def run_cmd(cmd, cwd=None):
    env = os.environ.copy()
    env.update(
        {
            "GIT_TERMINAL_PROMPT": "false",
            "GIT_CONFIG_GLOBAL": "/dev/null",
            "GIT_CONFIG_SYSTEM": "/dev/null",
            "LANG": "C",
            "LC_ALL": "C",
        }
    )

    finished_cmd = subprocess.run(
        cmd, check=True, text=True, capture_output=True, env=env, cwd=cwd
    )

    return finished_cmd.stdout


def get_versions() -> list[SimpleSemver]:
    cmd = ["git", "tag", "-l", "v*", "--no-column"]
    output = run_cmd(cmd)
    version_prefix = "v"
    versions = [
        SimpleSemver.from_dotted(version.lstrip(version_prefix))
        for version in output.strip().split("\n")
    ]
    return versions


def find_upgrade_version(
    current_version: SimpleSemver, versions: list[SimpleSemver]
) -> SimpleSemver | None:
    versions = sorted(versions, reverse=True)
    for version in versions:
        if version < current_version and version.minor != current_version.minor:
            return version

    return None


if __name__ == "__main__":
    current_version_env = os.environ.get("SEMANTIC_VERSION")
    assert current_version_env, "Please set SEMANTIC_VERSION to the current version"
    versions = get_versions()
    upgrade_version = find_upgrade_version(
        SimpleSemver.from_dotted(current_version_env), versions
    )

    assert upgrade_version, "No lower version found"
    print(upgrade_version.to_dotted())
