#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-only
# SPDX-FileCopyrightText: 2025 Univention GmbH


import contextlib
import os

from univention.admin.rest.client import UDM, UnprocessableEntity


udm_url = os.environ.get("UDM_URL", "http://localhost:9979/univention/udm")
udm_username = os.environ.get("UDM_USERNAME", "admin")
udm_password = os.environ.get("UDM_PASSWORD", "univention")

print("Adding extended attributes")
client = UDM.http(udm_url, udm_username, udm_password)
module = client.get("settings/extended_attribute")

# Customer1 extended attribute primaryOrgUnit
udm_obj = module.new(
    position="cn=custom attributes,cn=univention,dc=univention-organization,dc=intranet"
)
udm_obj.properties["name"] = "Customer1PrimaryOrgUnit"
udm_obj.properties["CLIName"] = "primaryOrgUnit"
udm_obj.properties["module"] = ["users/user"]
udm_obj.properties["default"] = ""
udm_obj.properties["ldapMapping"] = "univentionFreeAttribute1"
udm_obj.properties["objectClass"] = "univentionFreeAttributes"
udm_obj.properties["shortDescription"] = "Customer1 primary org unit"
udm_obj.properties["multivalue"] = False
udm_obj.properties["valueRequired"] = False
udm_obj.properties["mayChange"] = True
udm_obj.properties["doNotSearch"] = False
udm_obj.properties["deleteObjectClass"] = False
udm_obj.properties["overwriteTab"] = False
udm_obj.properties["fullWidth"] = True

# ignore error 422, it is thrown if the attribute already exists
with contextlib.suppress(UnprocessableEntity):
    udm_obj.save()

# Customer1 extended attribute secondaryOrgUnits
udm_obj = module.new(
    position="cn=custom attributes,cn=univention,dc=univention-organization,dc=intranet"
)
udm_obj.properties["name"] = "Customer1SecondaryOrgUnits"
udm_obj.properties["CLIName"] = "secondaryOrgUnits"
udm_obj.properties["module"] = ["users/user"]
udm_obj.properties["default"] = ""
udm_obj.properties["ldapMapping"] = "univentionFreeAttribute2"
udm_obj.properties["objectClass"] = "univentionFreeAttributes"
udm_obj.properties["shortDescription"] = "Customer1 primary secondary org units"
udm_obj.properties["multivalue"] = True
udm_obj.properties["valueRequired"] = False
udm_obj.properties["mayChange"] = True
udm_obj.properties["doNotSearch"] = False
udm_obj.properties["deleteObjectClass"] = False
udm_obj.properties["overwriteTab"] = False
udm_obj.properties["fullWidth"] = True

# ignore error 422, it is thrown if the attribute already exists
with contextlib.suppress(UnprocessableEntity):
    udm_obj.save()
