# nubus

Univention Nubus

- **Version**: 1.0.0
- **Type**: application

## TL;DR

```console
helm upgrade --install nubus oci://artifacts.software-univention.de/nubus/charts/nubus
```

## Introduction

This chart does install Nubus.

## Installing

To install the chart with the release name `nubus`:

```console
helm upgrade --install nubus oci://artifacts.software-univention.de/nubus/charts/nubus
```

## Uninstalling

To uninstall the chart with the release name `nubus`:

```console
helm uninstall nubus
```

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://artifacts.software-univention.de/nubus/charts | nubusGuardian(guardian) | 0.24.7 |
| oci://artifacts.software-univention.de/nubus/charts | keycloak(keycloak) | 0.16.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusKeycloakBootstrap(keycloak-bootstrap) | 0.20.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusKeycloakExtensions(keycloak-extensions) | 0.24.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLdapNotifier(ldap-notifier) | 0.47.12 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLdapServer(ldap-server) | 0.47.12 |
| oci://artifacts.software-univention.de/nubus/charts | nubusLicenseImport(license-import) | 0.8.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusNotificationsApi(notifications-api) | 0.90.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubus-common | 0.29.5 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalConsumer(portal-consumer) | 0.90.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalFrontend(portal-frontend) | 0.90.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusPortalServer(portal-server) | 0.90.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusProvisioning(provisioning) | 0.68.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusScimServer(scim-server) | 0.48.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusSelfServiceConsumer(selfservice-consumer) | 0.20.2 |
| oci://artifacts.software-univention.de/nubus/charts | nubusStackDataUms(stack-data-ums) | 0.100.7 |
| oci://artifacts.software-univention.de/nubus/charts | nubusTwofaHelpdesk(twofa-helpdesk) | 0.15.3 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUdmListener(udm-listener) | 0.68.1 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUdmRestApi(udm-rest-api) | 0.41.9 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUmcGateway(umc-gateway) | 0.56.0 |
| oci://artifacts.software-univention.de/nubus/charts | nubusUmcServer(umc-server) | 0.56.0 |
| oci://docker.io/bitnamicharts | minio | 14.7.0 |
| oci://docker.io/bitnamicharts | postgresql | ^12.x.x |

## Values

<table>
	<thead>
		<th>Key</th>
		<th>Type</th>
		<th>Default</th>
		<th>Description</th>
	</thead>
	<tbody>
		<tr>
			<td>additionalAnnotations</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Additional custom annotations to add to all objects deployed directly by the umbrella chart.</td>
		</tr>
		<tr>
			<td>additionalLabels</td>
			<td>object</td>
			<td><pre lang="json">
{}
</pre>
</td>
			<td>Additional custom labels to add to all objects deployed directly by the umbrella chart.</td>
		</tr>
		<tr>
			<td>certificates</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true
}
</pre>
</td>
			<td>SAML certificates generation</td>
		</tr>
		<tr>
			<td>certificates.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable SAML self-signed certificate generation. This requires cert-manager.io</td>
		</tr>
		<tr>
			<td>extraSecrets</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.certManagerIssuer</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Cert manager issuer of the cluster</td>
		</tr>
		<tr>
			<td>global.configMapUcr</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-ums-ucr"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.configUcr.ldap.index</td>
			<td>object</td>
			<td><pre lang="json">
{
  "approx": "cn,givenName,mail,sn,uid",
  "eq": "aRecord,automountInformation,cNAMERecord,cn,description,dhcpHWAddress,displayName,entryUUID,gidNumber,givenName,homeDirectory,krb5PrincipalName,macAddress,mail,mailAlternativeAddress,mailPrimaryAddress,memberUid,objectClass,ou,pTRRecord,relativeDomainName,sambaAcctFlags,sambaDomainName,sambaGroupType,sambaPrimaryGroupSID,sambaSID,sambaSIDList,secretary,shadowExpire,sn,uid,uidNumber,uniqueMember,univentionCanonicalRecipientRewriteEnabled,univentionDataType,univentionInventoryNumber,univentionLicenseModule,univentionLicenseObject,univentionMailHomeServer,univentionNagiosHostname,univentionObjectFlag,univentionObjectType,univentionPolicyReference,univentionServerRole,univentionService,univentionShareGid,univentionShareSambaName,univentionShareWriteable,univentionUDMOptionModule,univentionUDMPropertyCLIName,univentionUDMPropertyCopyable,univentionUDMPropertyDefault,univentionUDMPropertyDeleteObjectClass,univentionUDMPropertyDoNotSearch,univentionUDMPropertyHook,univentionUDMPropertyLayoutOverwritePosition,univentionUDMPropertyLayoutOverwriteTab,univentionUDMPropertyLayoutPosition,univentionUDMPropertyLayoutTabAdvanced,univentionUDMPropertyLayoutTabName,univentionUDMPropertyLdapMapping,univentionUDMPropertyLongDescription,univentionUDMPropertyModule,univentionUDMPropertyMultivalue,univentionUDMPropertyObjectClass,univentionUDMPropertyOptions,univentionUDMPropertyShortDescription,univentionUDMPropertySyntax,univentionUDMPropertyTranslationLongDescription,univentionUDMPropertyTranslationShortDescription,univentionUDMPropertyTranslationTabName,univentionUDMPropertyValueMayChange,univentionUDMPropertyValueRequired,univentionUDMPropertyVersion,zoneName,univentionObjectIdentifier",
  "pres": "aRecord,automountInformation,cn,description,dhcpHWAddress,displayName,gidNumber,givenName,homeDirectory,krb5PrincipalName,macAddress,mail,mailAlternativeAddress,mailPrimaryAddress,memberUid,name,objectClass,ou,relativeDomainName,shadowMax,sn,uid,uidNumber,uniqueMember,univentionMailHomeServer,univentionObjectFlag,univentionPolicyReference,univentionUDMPropertyCLIName,univentionUDMPropertyDefault,univentionUDMPropertyDeleteObjectClass,univentionUDMPropertyDoNotSearch,univentionUDMPropertyHook,univentionUDMPropertyLayoutOverwritePosition,univentionUDMPropertyLayoutOverwriteTab,univentionUDMPropertyLayoutPosition,univentionUDMPropertyLayoutTabAdvanced,univentionUDMPropertyLayoutTabName,univentionUDMPropertyLdapMapping,univentionUDMPropertyLongDescription,univentionUDMPropertyModule,univentionUDMPropertyMultivalue,univentionUDMPropertyObjectClass,univentionUDMPropertyOptions,univentionUDMPropertyShortDescription,univentionUDMPropertySyntax,univentionUDMPropertyTranslationLongDescription,univentionUDMPropertyTranslationShortDescription,univentionUDMPropertyTranslationTabName,univentionUDMPropertyValueMayChange,univentionUDMPropertyValueRequired,univentionUDMPropertyVersion,zoneName,univentionObjectIdentifier",
  "sub": "aRecord,associatedDomain,automountInformation,cn,default,description,displayName,employeeNumber,givenName,macAddress,mail,mailAlternativeAddress,mailPrimaryAddress,name,ou,pTRRecord,printerModel,relativeDomainName,sambaSID,sn,uid,univentionInventoryNumber,univentionOperatingSystem,univentionSyntaxDescription,univentionUDMPropertyLongDescription,univentionUDMPropertyShortDescription,zoneName"
}
</pre>
</td>
			<td>Indexes for the LDAP database</td>
		</tr>
		<tr>
			<td>global.domain</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Domain of the deployment</td>
		</tr>
		<tr>
			<td>global.enablePlainUmcLogin</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Allow plain UMC login (otherwise only SAML login is possible) Be aware this will expose the UMC login page to the public, which can circumvent 2FA and other security measures placed in the IdP.</td>
		</tr>
		<tr>
			<td>global.extensions</td>
			<td>list</td>
			<td><pre lang="json">
[]
</pre>
</td>
			<td>Extensions to load. Add entries to load additional extensions into Nubus.</td>
		</tr>
		<tr>
			<td>global.ingressClass</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.keycloak.realm</td>
			<td>string</td>
			<td><pre lang="json">
"nubus"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.auth.admin.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"password"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.auth.admin.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-admin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.baseDn</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.memcached.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.memcached.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.nubusDeployment</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Indicates to all subcharts that they are being used as part of a Nubus deployment.</td>
		</tr>
		<tr>
			<td>global.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-postgresql"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.secrets.masterPassword</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Master password from which other passwords are derived.</td>
		</tr>
		<tr>
			<td>global.subDomains.keycloak</td>
			<td>string</td>
			<td><pre lang="json">
"id"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.subDomains.portal</td>
			<td>string</td>
			<td><pre lang="json">
"portal"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.subDomains.scim</td>
			<td>string</td>
			<td><pre lang="json">
"scim"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>global.systemExtensions</td>
			<td>list</td>
			<td><pre lang="json">
[
  {
    "image": {
      "imagePullPolicy": "IfNotPresent",
      "registry": "artifacts.software-univention.de",
      "repository": "nubus/images/portal-extension",
      "tag": "0.90.0@sha256:8afb793ddf37bed3b931c8b35e0896b89c4eb0cb4fc67aa1004b3986da4585bc"
    },
    "name": "portal"
  },
  {
    "image": {
      "imagePullPolicy": "IfNotPresent",
      "registry": "artifacts.software-univention.de",
      "repository": "nubus/images/twofa-helpdesk-extensions",
      "tag": "0.15.2@sha256:fb41190e73ea8ee77c746301acdf8579e73d787fdebf76f2289a0dac9e309548"
    },
    "name": "2fa-helpdesk"
  }
]
</pre>
</td>
			<td>Allows to configure the system extensions to load. This is intended for internal usage, prefer to use `global.extensions` for user configured extensions.</td>
		</tr>
		<tr>
			<td>global.udm.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"http://{{ .Release.Name }}-udm-rest-api:9979/udm/"
</pre>
</td>
			<td>Global default for the URL via which the UDM Rest API can be reached. In transition state, not all subcharts do make use of this yet.</td>
		</tr>
		<tr>
			<td>ingress</td>
			<td>object</td>
			<td><pre lang="json">
{
  "annotations": {
    "nginx.ingress.kubernetes.io/affinity": "none",
    "nginx.ingress.kubernetes.io/proxy-body-size": "128k",
    "nginx.ingress.kubernetes.io/proxy-buffer-size": "64k",
    "nginx.ingress.kubernetes.io/proxy-buffers-number": "4",
    "nginx.ingress.kubernetes.io/proxy-busy-buffers-size": "128k",
    "nginx.ingress.kubernetes.io/proxy-http-version": "1.1",
    "nginx.ingress.kubernetes.io/use-regex": "true"
  },
  "certManager": {
    "enabled": true,
    "issuerRef": {
      "kind": "ClusterIssuer",
      "name": ""
    }
  },
  "favicon": {
    "enabled": true
  },
  "host": "",
  "ingressClassName": "",
  "minio": {
    "enabled": false
  },
  "tls": {
    "enabled": true,
    "secretName": ""
  }
}
</pre>
</td>
			<td>Configure supporting Ingress resources created directly by the umbrella chart.  The "enabled" attribute has been split, so that it is easier to enabled or disable individual resources. They are organized according to the pattern "{purpose}.enabled".  Ref.: https://kubernetes.io/docs/concepts/services-networking/ingress/</td>
		</tr>
		<tr>
			<td>ingress.annotations</td>
			<td>object</td>
			<td><pre lang="json">
{
  "nginx.ingress.kubernetes.io/affinity": "none",
  "nginx.ingress.kubernetes.io/proxy-body-size": "128k",
  "nginx.ingress.kubernetes.io/proxy-buffer-size": "64k",
  "nginx.ingress.kubernetes.io/proxy-buffers-number": "4",
  "nginx.ingress.kubernetes.io/proxy-busy-buffers-size": "128k",
  "nginx.ingress.kubernetes.io/proxy-http-version": "1.1",
  "nginx.ingress.kubernetes.io/use-regex": "true"
}
</pre>
</td>
			<td>Define custom ingress annotations. annotations:   nginx.ingress.kubernetes.io/rewrite-target: /</td>
		</tr>
		<tr>
			<td>ingress.certManager</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true,
  "issuerRef": {
    "kind": "ClusterIssuer",
    "name": ""
  }
}
</pre>
</td>
			<td>Request certificates via cert-manager.io annotation</td>
		</tr>
		<tr>
			<td>ingress.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable cert-manager.io annotaion.</td>
		</tr>
		<tr>
			<td>ingress.certManager.issuerRef.kind</td>
			<td>string</td>
			<td><pre lang="json">
"ClusterIssuer"
</pre>
</td>
			<td>Type of Issuer, f.e. "Issuer" or "ClusterIssuer".</td>
		</tr>
		<tr>
			<td>ingress.certManager.issuerRef.name</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Name of cert-manager.io Issuer resource.</td>
		</tr>
		<tr>
			<td>ingress.favicon</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true
}
</pre>
</td>
			<td>Serve an icon on the path "/favicon.ico" if enabled.</td>
		</tr>
		<tr>
			<td>ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>Define the Fully Qualified Domain Name (FQDN) where application should be reachable.</td>
		</tr>
		<tr>
			<td>ingress.ingressClassName</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>The Ingress controller class name.</td>
		</tr>
		<tr>
			<td>ingress.minio</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": false
}
</pre>
</td>
			<td>Serve dynamic portal assets (icons, logos, background images) out of the MinIO bucket "portal-assets".  This is intended to be used together with the bundled minio. If an external S3-compatible store is used then a potentially needed Ingress resource as to be set up by the operator.</td>
		</tr>
		<tr>
			<td>ingress.tls</td>
			<td>object</td>
			<td><pre lang="json">
{
  "enabled": true,
  "secretName": ""
}
</pre>
</td>
			<td>Secure an Ingress by specifying a Secret that contains a TLS private key and certificate.  Ref.: https://kubernetes.io/docs/concepts/services-networking/ingress/#tls</td>
		</tr>
		<tr>
			<td>ingress.tls.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Enable TLS/SSL/HTTPS for Ingress.</td>
		</tr>
		<tr>
			<td>ingress.tls.secretName</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td>The name of the kubernetes secret which contains a TLS private key and certificate. Hint: This secret is not created by this chart and must be provided.</td>
		</tr>
		<tr>
			<td>keycloak.config.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.ingress.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.keycloak.auth.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>keycloak.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>minio.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Enable bundled MinIO object storage. Disable when using an external S3-compatible object store. See demo-values.yaml and prod-values.yaml for examples.</td>
		</tr>
		<tr>
			<td>minio.image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"bitnamilegacy/minio"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusDevelopment.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.authorizationApi.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.authorizationApi.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.authorizationApi.udm.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"guardian"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.keycloak.auth.existingSecret.keyMapping.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.provisioning.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusGuardian.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.bootstrap.twoFactorAuthentication.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.bootstrap.twoFactorAuthentication.group</td>
			<td>string</td>
			<td><pre lang="json">
"2FA Users"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.keycloak.auth.existingSecret.keyMapping.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.ldap.auth.bindDn</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubus.keycloak.ldap.auth.bindDn\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-stack-data-ums-readonly-user\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-bootstrap"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakBootstrap.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.handler.appConfig.emailNotificationTimezone</td>
			<td>string</td>
			<td><pre lang="json">
"UTC"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.handler.appConfig.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.handler.appConfig.newDeviceLoginNotificationEnable</td>
			<td>string</td>
			<td><pre lang="json">
"True"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.auth.existingSecret.keyMapping.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.keycloak.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak-extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.auth.database</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak_extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-extensions-postgresql-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.postgresql.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"keycloak_extensions"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.proxy.appConfig.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"info"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.smtp.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusKeycloakExtensions.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"ldap-notifier"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapNotifier.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"ldap-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.replicaCountPrimary</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.replicaCountProxy</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.replicaCountSecondary</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesPrimary.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesProxy.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLdapServer.resourcesSecondary.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusLicenseImport.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"license-import"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"notifications-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusNotificationsApi.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.ldap.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-ldap-server-primary"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-consumer"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.provisioningApi.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"http://{{ .Release.Name }}-provisioning-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalConsumer.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-frontend"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalFrontend.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"portal-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusPortalServer.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-stack-data-ums-svc-portal-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"provisioning"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.auth.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.cluster.replicas</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-udm-listener-nats"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"udmlistener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.permissions.publish</td>
			<td>string</td>
			<td><pre lang="json">
"\u003e"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.config.createUsers.udmListener.permissions.subscribe</td>
			<td>string</td>
			<td><pre lang="json">
"\u003e"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.global.imageRegistry</td>
			<td>string</td>
			<td><pre lang="json">
"docker.io"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.natsBox.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.reloader.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.nats.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.prefill.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.createUsers.portalConsumer.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-portal-consumer-provisioning-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.createUsers.selfserviceConsumer.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-selfservice-listener-provisioning-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.registerConsumers.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.api.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.dispatcher.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.resources.prefill.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.udmTransformer.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusProvisioning.udmTransformer.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.auth.allowedAudience</td>
			<td>string</td>
			<td><pre lang="json">
"scim-api-access"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.auth.allowedClientId</td>
			<td>string</td>
			<td><pre lang="json">
"scim-client"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.auth.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.corsOrigins</td>
			<td>string</td>
			<td><pre lang="json">
"[\"https://{{ .Values.global.subDomains.scim }}.{{ .Values.global.domain }}\"]"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.externalId.groupMapping</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.externalId.userMapping</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.host</td>
			<td>string</td>
			<td><pre lang="json">
"https://{{ .Values.global.subDomains.scim }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.config.logLevel</td>
			<td>string</td>
			<td><pre lang="json">
"INFO"
</pre>
</td>
			<td>Available log levels are: TRACE, DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL  For detailed information please have a look at the loguru documentation: https://loguru.readthedocs.io/en/stable/api/logger.html#levels</td>
		</tr>
		<tr>
			<td>nubusScimServer.config.roles.userMapping</td>
			<td>string</td>
			<td><pre lang="json">
null
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.docu.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.ingress.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.ingress.certManager.issuerRef.kind</td>
			<td>string</td>
			<td><pre lang="json">
"ClusterIssuer"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.ingress.certManager.issuerRef.name</td>
			<td>string</td>
			<td><pre lang="json">
""
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.ingress.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.scim }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.ingress.tls.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.keycloak.connection.realm</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.keycloak.realm }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.keycloak.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"https://{{ .Values.global.subDomains.keycloak }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"scim-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.udm.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"cn=admin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusScimServer.udm.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.udmRestApi.uri\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.provisioningApi.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"http://{{ .Release.Name }}-provisioning-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusSelfServiceConsumer.umc.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"http://{{ .Release.Name }}-umc-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"stack-data-ums"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"selfservice"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.memcached.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s-umc-server-memcached\" .Release.Name }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.postgres.host\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.nubusUmcServer.postgresql.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.postgres.port\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.stackDataContext.ldapHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.ldap.primary.host\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.stackDataContext.ldapMasterHost</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.ldap.primary.host\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.portalTwoFaAllowedGroups[0]</td>
			<td>string</td>
			<td><pre lang="json">
"Domain Admins"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.portalTwoFaLinkBase</td>
			<td>string</td>
			<td><pre lang="json">
"https://{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.twofaAdminHelpdeskActivated</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td>Creates the Portal Tile for the 2FA admin helpdesk.</td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.twofaAdminTileCategory</td>
			<td>string</td>
			<td><pre lang="json">
"domain-admin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.twofaSelfServiceActivated</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Creates the Portal Tile for the 2FA self-service.</td>
		</tr>
		<tr>
			<td>nubusStackDataUms.templateContext.twofaSelfserviceTileCategory</td>
			<td>string</td>
			<td><pre lang="json">
"domain-service"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.udm.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusStackDataUms.udm.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.ingress.certManager.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.ingress.tls.secretName</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-twofa-backend-api-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.keycloak.admin_realm</td>
			<td>string</td>
			<td><pre lang="json">
"master"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.keycloak.auth.existingSecret.keyMapping.adminPassword</td>
			<td>string</td>
			<td><pre lang="json">
"adminPassword"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.keycloak.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{- printf \"%s-keycloak-credentials\" .Release.Name -}}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.keycloak.auth.username</td>
			<td>string</td>
			<td><pre lang="json">
"kcadmin"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.keycloak.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-keycloak"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.keycloak.connection.url</td>
			<td>string</td>
			<td><pre lang="json">
"https://{{ .Values.global.subDomains.keycloak }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.keycloak.realm</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.keycloak.realm }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"helpdesk"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.nubusBaseUrl</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"%s.%s\" .Values.global.subDomains.portal .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.provisioning.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.twofaHelpdeskFrontend.config.enableAdminHelpdesk</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.twofaHelpdeskFrontend.config.enableSelfService</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusTwofaHelpdesk.twofaHelpdeskFrontend.config.postLogoutRedirectURI</td>
			<td>string</td>
			<td><pre lang="json">
"{{ printf \"https://%s.%s/\" .Values.global.subDomains.portal .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"provisioning-udm-listener"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.nats.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-nats"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.provisioningApi.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-provisioning-api-events"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmListener.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ingress.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"udm-rest-api"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUdmRestApi.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"umc-gateway"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcGateway.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
true
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[0].mountPath</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumeMounts[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"certificates"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[0].name</td>
			<td>string</td>
			<td><pre lang="json">
"certificates"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.extraVolumes[0].secret.secretName</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-saml-tls"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.ingress.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Values.global.subDomains.portal }}.{{ .Values.global.domain }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.ldap.auth.existingSecret.keyMapping.password</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.keyMapping.password . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.ldap.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ tpl .Values.global.ldap.auth.admin.existingSecret.name . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.nameOverride</td>
			<td>string</td>
			<td><pre lang="json">
"umc-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.authSession.connection.host</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.postgres.host\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.postgresql.authSession.connection.port</td>
			<td>string</td>
			<td><pre lang="json">
"{{ include \"nubusTemplates.connections.postgres.port\" . }}"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.replicaCount</td>
			<td>int</td>
			<td><pre lang="json">
1
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.limits.cpu</td>
			<td>int</td>
			<td><pre lang="json">
288
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.limits.memory</td>
			<td>string</td>
			<td><pre lang="json">
"1Gi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.requests.cpu</td>
			<td>string</td>
			<td><pre lang="json">
"10m"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.resources.requests.memory</td>
			<td>string</td>
			<td><pre lang="json">
"16Mi"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.terminationGracePeriodSeconds</td>
			<td>int</td>
			<td><pre lang="json">
5
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.umcServer.certPemFile</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl/tls.crt"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.umcServer.oidcClient.auth.existingSecret.name</td>
			<td>string</td>
			<td><pre lang="json">
"{{ .Release.Name }}-keycloak-bootstrap-oidc-rp-umc-server"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>nubusUmcServer.umcServer.privateKeyFile</td>
			<td>string</td>
			<td><pre lang="json">
"/var/secrets/ssl/tls.key"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.enabled</td>
			<td>bool</td>
			<td><pre lang="json">
false
</pre>
</td>
			<td>Enable bundled PostgreSQL database. Disable when using an external database. See demo-values.yaml and prod-values.yaml for examples.</td>
		</tr>
		<tr>
			<td>postgresql.image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"bitnamilegacy/postgresql"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.image.registry</td>
			<td>string</td>
			<td><pre lang="json">
"docker.io"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.image.repository</td>
			<td>string</td>
			<td><pre lang="json">
"bitnamilegacy/postgresql"
</pre>
</td>
			<td></td>
		</tr>
		<tr>
			<td>postgresql.provisioning.image.tag</td>
			<td>string</td>
			<td><pre lang="json">
"15.4.0-debian-11-r45"
</pre>
</td>
			<td></td>
		</tr>
	</tbody>
</table>

