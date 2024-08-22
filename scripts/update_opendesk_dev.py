#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2024 Univention GmbH

import argparse
import tempfile
import os
import shutil
import yaml
import subprocess
import logging
import tarfile
import re

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def run_helm_command(command):
    logging.info(f"Running Helm command: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        logging.error(f"Helm command failed: {result.stderr}")
        raise Exception(f"Helm command failed: {result.stderr}")
    return result.stdout.strip()


def download_chart(repository, chart, version, output_dir):
    logging.info(f"Downloading chart {chart} version {version} from {repository}")
    output_file = os.path.join(output_dir, f"{chart}-{version}.tgz")
    oci_url = f"oci://{repository}/{chart}"
    run_helm_command(["helm", "pull", oci_url, "--version", version, "--destination", output_dir])
    return output_file


def create_custom_values_file(temp_dir):
    custom_values = {
        "global": {
            "nubusDeployment": True,
            "ldap": {"baseDn": "dc=swp-ldap,dc=internal", "domainName": "example.com"},
            "domain": "example.com",
            "ingressClass": "nginx",
            "certManagerIssuer": "letsencrypt-prod-dns",
            "nubusMasterPassword": "nubus",
        }
    }
    values_file = os.path.join(temp_dir, "custom_values.yaml")
    with open(values_file, "w") as f:
        yaml.dump(custom_values, f)
    return values_file


def template_chart_with_values(tgz_file, extract_dir, values_file):
    logging.info(f"Extracting chart from {tgz_file} to {extract_dir} with custom values")
    run_helm_command(
        [
            "helm",
            "template",
            tgz_file,
            "--output-dir",
            extract_dir,
            "-f",
            values_file,
            "--set",
            "postgresql.enabled=false",
            "--set",
            "postgresql.provisioning.enabled=false",
            "--set",
            "minio.enabled=false",
        ]
    )


def get_chart_yaml(tgz_file):
    logging.info(f"Extracting Chart.yaml from {tgz_file}")
    with tarfile.open(tgz_file, "r:gz") as tar:
        chart_yaml = tar.extractfile("nubus/Chart.yaml")
        if chart_yaml:
            return yaml.safe_load(chart_yaml)
    return None


def compare_charts(old_chart_dir, new_chart_dir):
    logging.info("Comparing charts")
    changed_images = {}

    for root, dirs, files in os.walk(new_chart_dir):
        for file in files:
            if file.endswith(".yaml"):
                new_file_path = os.path.join(root, file)
                old_file_path = new_file_path.replace(new_chart_dir, old_chart_dir)

                if os.path.exists(old_file_path):
                    logging.debug(f"Comparing files {old_file_path} and {new_file_path}")
                    with open(old_file_path, "r") as old_file, open(new_file_path, "r") as new_file:
                        old_content = old_file.read()
                        new_content = new_file.read()

                        old_images = re.findall(r'image:\s*"?([^"\s]+)"?', old_content)
                        new_images = re.findall(r'image:\s*"?([^"\s]+)"?', new_content)

                        for old_image, new_image in zip(old_images, new_images):
                            if old_image != new_image:
                                changed_images[new_image] = {"old": old_image, "new": new_image}
                                logging.info(f"Changed image: {old_image} -> {new_image}")
                            else:
                                logging.debug(f"Image {old_image} is the same")

    return changed_images


def update_charts_yaml(file_path, new_version):
    logging.info(f"Updating {file_path} with new version {new_version}")
    with open(file_path, "r") as f:
        content = f.read()

    # Update nubus chart version, registry, and repository
    pattern = r"(^\s{2}nubus:\s*(?:\n\s{4,}.*)*?\n\s{4,})(registry:)(.*)?(\n\s{4,}repository:)(.*)?(\n\s{4,}name:.*\n\s{4,}version:).*"
    match = re.search(pattern, content, flags=re.MULTILINE)

    replacement: str = ""

    if "# registry:" in match.group(1):
        # If comments already exist, keep them and update only the actual values
        replacement = (
            r'\1registry: "artifacts.software-univention.de"\n'
            rf'    repository: "nubus-dev/charts"\6 "{new_version}"'
        )
    else:
        # If no comments exist, add them along with the new values
        replacement = (
            r"\1# \2\3\n    # repository:\5\n"
            r'    registry: "artifacts.software-univention.de"\n'
            rf'    repository: "nubus-dev/charts"\6 "{new_version}"'
        )

    updated_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    if content == updated_content:
        logging.warning("No changes were made to charts.yaml. Was the desired version already set?")

    with open(file_path, "w") as f:
        f.write(updated_content)


def parse_docker_image(image_string):
    pattern = r"^(?:(?P<registry>[\w\.\-]+(?::\d+)?)/)?(?P<repository>[\w\.\-/]+)(?::(?P<tag>[\w\.\-]+))?(?:@(?P<digest>sha256:[a-fA-F0-9]+))?$"
    match = re.match(pattern, image_string)
    if match:
        return match.groupdict()
    return None


def update_images_yaml(file_path, changed_images):
    logging.info(f"Updating {file_path} with changed images")
    logging.debug(f"Changed images: {changed_images}")
    with open(file_path, "r") as f:
        content = f.read()

    for image_name, image_info in changed_images.items():
        logging.debug(f"Updating image {image_name}")
        old_image = image_info["old"]
        new_image = image_info["new"]
        new_parts = parse_docker_image(new_image)

        if new_parts:
            # Use the provided regex pattern
            # TODO: adapt pattern to also match already updated images
            pattern = (
                r'(^\s{2}\w*:(\n\s{4,}.*)+\n\s{4,})(registry: )"([a-zA-Z0-9\.-]+)'
                r'("\n\s{4,}repository: ")([a-zA-Z0-9-/]+/'
                rf'{new_parts["repository"].split("/")[-1]})'
                r'("\n\s{4,}tag: ")(.*)(")$'
            )
            logging.debug(f"Pattern: {pattern}")
            FLAGS = re.MULTILINE
            if not (match := re.search(pattern, content, flags=FLAGS)):
                logging.warning(f"Pattern not found for image {image_name}. Skipping update.")
                continue

            logging.debug(f"Match: {match.groups()}")

            # check if the comment for old registry and repository is already there
            if "# registry:" in match.group(1):
                # If comments already exist, keep them and update only the actual values
                replacement = (
                    rf'\1registry: "{new_parts["registry"]}"\n'
                    rf'    repository: "{new_parts["repository"]}"\n'
                    rf'    tag: "{new_parts["tag"]}{"@" + new_parts["digest"] if new_parts["digest"] else ""}"'
                )
            else:
                replacement = (
                    r'\1# \3"\4"\n'
                    r'    # repository: "\6"\n'
                    rf'    registry: "{new_parts["registry"]}"\n'
                    rf'    repository: "{new_parts["repository"]}"\n'
                    rf'    tag: "{new_parts["tag"]}{"@" + new_parts["digest"] if new_parts["digest"] else ""}"'
                )

            # Perform the substitution
            updated_content = re.sub(pattern, replacement, content, flags=FLAGS)

            if content == updated_content:
                logging.warning(
                    f"No changes were made for image {image_name}. Was the desired version already set?"
                )
            else:
                content = updated_content
                logging.info(f"Updated image {image_name} from {old_image} to {new_image}")
        else:
            logging.warning(f"Invalid image format for {image_name}: {old_image} -> {new_image}")

    with open(file_path, "w") as f:
        f.write(content)


def get_current_version_from_charts_yaml(file_path):
    pattern = r'nubus:(?:\s*#[^\n]*\n)*\s*(?:.*\n)*?\s*version:\s*"?(\d+\.\d+\.\d+(-[a-z0-9-]+)?)"?'
    with open(file_path, "r") as f:
        content = f.read()
    match = re.search(pattern, content)
    if match:
        return match.group(1)
    return None


def main(new_version, current_version=None):
    logging.info(f"Starting chart update process for version {new_version}")
    temp_dir = tempfile.mkdtemp()
    try:
        old_chart_dir = os.path.join(temp_dir, "old_chart")
        new_chart_dir = os.path.join(temp_dir, "new_chart")
        os.makedirs(old_chart_dir)
        os.makedirs(new_chart_dir)

        # Create custom values file
        custom_values_file = create_custom_values_file(temp_dir)

        # Use the provided current_version or get it from charts.yaml
        if current_version:
            old_version = current_version
            logging.info(f"Using provided current nubus version: {old_version}")
        else:
            # Fallback to getting the version from charts.yaml
            charts_yaml_path = "helmfile/environments/default/charts.yaml"
            old_version = get_current_version_from_charts_yaml(charts_yaml_path)
            if old_version:
                logging.info(f"Current nubus version from charts.yaml: {old_version}")
            else:
                logging.error("Could not find the current nubus version in charts.yaml")
                raise Exception("Could not find the current nubus version in charts.yaml")

        # Download and extract charts
        old_tgz = download_chart(
            "artifacts.software-univention.de/nubus-dev/charts",
            "nubus",
            old_version,
            old_chart_dir,
        )
        new_tgz = download_chart(
            "artifacts.software-univention.de/nubus-dev/charts", "nubus", new_version, new_chart_dir
        )

        template_chart_with_values(old_tgz, old_chart_dir, custom_values_file)
        template_chart_with_values(new_tgz, new_chart_dir, custom_values_file)

        # Compare charts and update files
        changed_images = compare_charts(old_chart_dir, new_chart_dir)

        update_charts_yaml("helmfile/environments/default/charts.yaml", new_version)
        update_images_yaml("helmfile/environments/default/images.yaml", changed_images)

    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

    logging.info("Chart update process completed successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upgrade Helm charts and Docker images")
    parser.add_argument("new_version", help="New version of the umbrella chart")
    parser.add_argument("--current-version", help="Current version of the umbrella chart")
    args = parser.parse_args()

    main(args.new_version, args.current_version)
