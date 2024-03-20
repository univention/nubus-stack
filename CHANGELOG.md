# Changelog

## [0.7.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.7.1...v0.7.2) (2024-03-20)


### Bug Fixes

* check helm sha256 sum ([7824e8c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7824e8c6573f1392536abd22ee476409fc691382))

## [0.7.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.7.0...v0.7.1) (2024-03-20)


### Bug Fixes

* add renovate job for automatic dependency update MRs ([bf3ad38](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/bf3ad38fec1275cd0582aab31e7496321f47e7cf))
* chart versions ([8eb0658](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8eb0658a00191135b63af76343743d4c4285ddf1))

## [0.7.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.6.0...v0.7.0) (2024-03-20)


### Features

* use BSI compliant charts ([9b2b97b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9b2b97bf08e6c5cca231853c7555bbb9424d506e))


### Bug Fixes

* adjust to upstream helm changes ([cf1be6d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cf1be6d95ed4897d91950fb1c73add07c9c226fc))
* fix linter_values.yaml ([6be7c69](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6be7c6931f941452168c70ce3baed4cf19301588))
* merge artifact ([aa43a77](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/aa43a7767228e78df977f0009678ab2a9a750bc5))
* ref ldap-server feature branch ([66e3328](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/66e33289e0e99385f8c7961c15959878611211e4))
* remove store-dav references ([e1f426e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e1f426ea7913d9d75c4b02cd5f74894222cc7cdb))
* test new upstream versions ([9762162](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/97621626f14ab156e2f8fd0eced9b7068671b993))

## [0.6.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.5.0...v0.6.0) (2024-03-20)


### Features

* Add configuration regarding the S3 compatible object store for portal-listener ([aa41f2c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/aa41f2ca1c374f4414cceddb84a257fdb3a2ed82))
* Apply password policy and tls related UCR settings from dev-env ([967b028](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/967b0283070509bd65a3a76e3bcc212768c6f778))
* Extend minio configuration for usage by other components ([0874a16](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/0874a16a42badd8bec94affda337a6a6fb175fab))
* Simplify development stub passwords after policy update ([4651956](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/4651956d90e2b53c503dda51258531bdd432858f))
* Update dependencies to latest versions ([887045c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/887045cf867c2aaa096e823bfc56f60acd5b9afa))


### Bug Fixes

* Add "proxy-buffer-size" annotation to stack-gateway for ingress-nginx ([617c4df](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/617c4dffb91385a56a8bfd4c646b11e716f68d0d))
* Add UMC related settings to stack-data-ums ([805165b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/805165b006869288cf8852257c6ec65281c01fe0))
* Add workaround for provisioning until the default registry is configured ([ea18192](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ea18192d8f4ecac9a0d21e571dae7fccb0d5802b))
* Add workaround regarding the postgresql version for notifications-api ([be91792](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/be91792f2ae8bbaef8514945f3a7904f14ee658c))
* Adjust portal-server configuration to use minio ([fb3943c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fb3943c9e34306accd3468a7a8386a81e0f1a5c6))
* Adjust secrets configuration for notifications-api's postgres ([666a0d8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/666a0d89b126c42e4026929001eb209849edd662))
* Apply interim fix related to the udm-rest-api ([86539a4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/86539a4218cf41bf1da4a2552bfd82f2e3fd69ff))
* Correct ldap related credentials for udm-rest-api ([8163782](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8163782ff539b3e121ed4f5ecbc2b2116e63c45a))
* Correct objectStorageEndpoint for the portal-listener ([7612586](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7612586b1026cad82f74f653280e6be4fe34e1a7))
* Correct SAML ID in the ldap configuration ([941dca1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/941dca143e1a0c4e1c81f60085992cd5485150c6))
* Remove cert-manager related configuration from linter values ([bdc3c8b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/bdc3c8b577609ad6d30902f31595c4cb1c0cec68))
* Remove now outdated secret configuration for udm-rest-api ([5a9495c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5a9495c788bc886f3126e0da4bbed07c0a032424))
* Switch to use "extraSecrets" for udm rest api ([9859a71](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9859a710724c8d7e34aa30b56090f17ac0c89611))
* Workaround for the keycloak default memory limit ([621a1f8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/621a1f893c8937ba9a1fca3f1133b8a9edcc4cd6))

## [0.5.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.4.0...v0.5.0) (2024-03-13)


### Features

* add stack-gateway ([f6d78d4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f6d78d4422c78655fe6bd3a9ad9b7592a8f92620))

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
