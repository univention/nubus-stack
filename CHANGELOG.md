# Changelog

## [0.4.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.3.0...v0.4.0) (2024-03-13)


### Features

* add minio to chart ([9563ca9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9563ca9aa4910f1c93e5cf7488bd2ee314409749))


### Bug Fixes

* **ci/docs:** update docs, update gitlab-ci ([9789063](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/97890638968342a00af662c0ad7577d1d69b7d86))

## [0.3.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.2.0...v0.3.0) (2024-01-30)


### Features

* Add "ldapSearchUser" for the keycloak integration ([667c1b8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/667c1b8a7fe61ad7241a64b4f595c44f86aada5a))
* Add guardian related charts into the list of dependencies ([bf49bde](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/bf49bde444325167337d9e73b19e99c59cd938d8))
* Add keycloak-bootstrap and extensions as dependencies ([fb628fb](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fb628fbf94cf28805c9145ef1e64eb1d72d2e5ac))
* Add SAML related settings for stack-data-ums ([2ff3677](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2ff36774d041afc5e9aec5690f4e1299401f1f2f))
* Add selfservice-listener ([16ac8de](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/16ac8de6593fbf757bb5419a1897de20b06c6071))
* Add theming related configuration regarding Keycloak ([61bf6b3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/61bf6b3afe9e476758c30e025bf73eebc6af7222))
* Add univention keycloak into the dependencies ([3a36626](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3a36626e45862e322f0f4bae888b7a01196e1f5c))
* Adjust oauth related settings to realm "opendesk" ([9d79b97](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9d79b978e2fb56291329ea3c8b63e6d2b1a31e3b))
* Domain and realm related tweaks for the keycloak integration ([8e0119a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8e0119aedbe4c3b71d482c0c3b5a6d29f3c98c9b))
* Expose the Keycloak admin interface via Ingress of keycloak-extensions ([7f227ff](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7f227fff48d5364e63ffb76be9fa714e3f81628d))
* First iteration on Guardian related configuration ([616bb3c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/616bb3c99af2e1ba793659c8f7284d086190a81d))
* Update dependencies to latest versions ([de65e6e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/de65e6eed1a696735abc1b289fc401039796a4d6))


### Bug Fixes

* Configure "natsHost" for the provisioning listener ([c4bf7c5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c4bf7c5a88e804b17d030abd052644a839d8e9a1))
* Correct typo in parameter "keycloak-bootstrap.config.ums.ldap.baseDN" ([3d36a7a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3d36a7a62fec57adf8ed79e1fa921c8feed34158))
* Ensure a more recent image is used in "keycloak-bootstrap" ([7e5fb47](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7e5fb479aad29f1be1db4dcff51dcb8887aa688c))

## [0.2.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.1.0...v0.2.0) (2024-01-23)


### Features

* Add "dev_values.yaml" to support local development needs ([826bae0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/826bae05735174ab491c44eff56e9a211ab2aa72))
* Add extra volume configuration from openDesk ([403d47d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/403d47d60b7cbad1f6332638bda4354d9fadcafa))
* Add extraIngress configuration for the portal frontend ([a65bb0c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a65bb0cbf3e164021379f471760ca2059e746c4f))
* Add initialPasswordSysIdpUser to stack-data-ums ([ba068ec](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ba068ecc3d19158e3c36cbea1e357ae6b0d15811))
* Add ldap-server, ldap-notifier and stack-data as dependencies ([c88b08a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c88b08a39e0e678031798695db2efc9bf125c5be))
* Add store-dav as dependency ([4027821](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/402782192243dd3db9c0e5787742cd2ebdbf6848))
* Add the portal subcharts as dependencies ([ac43828](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ac4382816b66c9a79d8291336f30014ab8755c1c))
* Add the Provisioning components into the chart ([05f7a91](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/05f7a917430a2d30e9757adde5864e86387f2663))
* Add UMC charts into dependencies ([5dddf2c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5dddf2c9464816110f92bbebd593052e1b0d1125))
* Catch up with removal of secrets from the notifications-api defaults ([feffbeb](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/feffbeb6be9465534b9a88db42cd98b708035c46))
* Enable the bundled memcached for the umc-server ([3d03c28](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3d03c28bcee59656d193db8f29338b748cad9d20))
* Enable the bundled postgresql for the umc-server ([7303aa1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7303aa1994108f5e856e7e5e41ed6c0bdecf4f05))
* Integrate udm-rest-api ([e350db7](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e350db7e532b42fe9e947cf71e49eebcaf836833))
* Only lock the major version on our subcharts ([ee4d240](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ee4d240360ca3f789c4fe08ab643628ff196d4b5))
* Prefix the bundled postgresql in notifications-api ([2c0bd89](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2c0bd897512758efa8efbcb7410dd02ea49e829f))
* Rename the chart to "ums" to keep names short ([39e59cd](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/39e59cdebe9e07ccbc3eb3eb989335fcb0aeef9e))


### Bug Fixes

* Passwords in linter_values meet the complexity rules ([a02daa5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a02daa57763c1bf90fe30c384c0b07016d00beec))

## [0.1.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.0.3...v0.1.0) (2024-01-20)


### Features

* Enable souvap publishing of the helm package ([1f8b609](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1f8b609962a4908b754db72e381f5fe6fd7dc114))
