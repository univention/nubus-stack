# Changelog

## [1.10.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.10.0...v1.10.1) (2025-06-02)


### Bug Fixes

* **udm-rest-api:** CronJob additionalAnnotations and podAnnotations ([e44e2da](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e44e2dad9cd236ea70b848df93c20262efff0792)), closes [univention/dev/internal/team-nubus#1170](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1170)

## [1.10.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.9.2...v1.10.0) (2025-05-29)


### Features

* Adjust values configuration for stack-data-ums towards the new secrets structure ([a768a1d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a768a1d0f57f490b50de826aa19e4cd71fcbac9f))
* Adjust values configuration towards updated secrets structure in udm-listener ([2abab0a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2abab0ae8c4618cd6511c3de86f4476ccfcca5c1))
* All containers non-root and w/ read only file system ([e9c70af](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e9c70af7d52a7b5df0fe7d8c145e7baaf3493981)), closes [univention/dev/internal/team-nubus#1139](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1139)
* enable blocklist feature ([b7f22c6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b7f22c6c86466ac700866ce547955c865f9e46ee))
* Init containers of UMC pods are started as non-root ([f0efd54](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f0efd549ed18567d2055a670d4e5d88ddf16528f)), closes [univention/dev/internal/team-nubus#1138](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1138)
* **nubus:** Add scim-server ([d25016c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d25016cf87c0684dd14452ad44cf34752ca156f2)), closes [univention/dev/internal/team-nubus#1112](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1112)
* Update portal components to version 0.68.0 ([61a0d1b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/61a0d1bbb8dee62f72ff059f82394aef3b7b00c9))
* Update stack-data-ums to version 0.93.0 ([959f3ef](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/959f3efc37be0649502cf7ab0071507a2f48a705))
* Update udm-listener to version 0.53.0 ([547ce03](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/547ce03125de68e3d75d398b7dd780267eeb362f))


### Bug Fixes

* Automatically set the univentionObjectIdentifier for new objects ([15df8c7](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/15df8c7cd32032eb2e73b7bd6eebbf4541ee62d8)), closes [univention/dev/internal/team-nubus#1143](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1143)
* disable ingress affinity ([fc5e444](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fc5e4442cb8b0c0a8dc938095327c024a53c6f75)), closes [univention/dev/internal/team-nubus#1121](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1121)
* hide report generation in umc ([4359855](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/43598554410ed70b4d140a4cd23f2734260dda69)), closes [univention/dev/internal/team-nubus#1164](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1164)
* **portal-consumer:** Bump to latest version ([09cd25e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/09cd25e1460ec0a978dc172bfa206457e268dd0d)), closes [univention/dev/internal/team-nubus#1167](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1167)
* **udm-listener:** add configurable storageClass and size to PVC ([192f38c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/192f38c73e8bf4c8fd29f643184911ec40521839)), closes [univention/dev/internal/team-nubus#1181](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1181)
* **udm-listener:** Typo in provisioning api secret key mapping ([5051987](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/50519873677b8205f44e5ce6b499b6575f322043)), closes [univention/dev/internal/team-nubus#1208](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1208)
* **udm-rest-api:** Generate univentionObjectIdentifier for existing objects ([65153ce](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/65153cecf55edcf0fb90c3953fd174ed9a611319)), closes [univention/dev/internal/team-nubus#1157](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1157)

## [1.9.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.9.1...v1.9.2) (2025-05-14)


### Bug Fixes

* add bitnami helm repo to lint-pre-commit job ([8e7b550](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8e7b5502e7c6a08460389123c32bc2f799458cc9))
* add bitnami repo to package-helm-charts ([b6b987a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b6b987a8f95e1c02582247fd4cfc915d1a4799d1))
* move addlicense pre-commit hook ([b871b99](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b871b992d339ddab2ef59671ce8233fe6f225e17))
* move e2e-tests to dev/nubus-for-k8s ([dbfb777](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/dbfb777283d6d8130f1c86968cc7749b86008efe))
* **portal-consumer:** Wrong keys ([19fe7f5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/19fe7f57376381105798f490403dd9ddc4776b10)), closes [univention/dev/internal/team-nubus#1091](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1091)
* **umc-gateway:** Icons were copied to the wrong path ([36445d1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/36445d15264f72e3722be64ebdb6d7290ed1ca8d))
* update common-ci to main ([f0a5388](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f0a5388cfd1648ea4907d989c91487328c60acba))

## [1.9.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.9.0...v1.9.1) (2025-05-07)


### Bug Fixes

* Avoid duplicate key in favicon related Ingress ([87a4a17](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/87a4a175b8580bd2c8ed8032898796050dce4c95))
* Warnings and errors on duplicated keys and security context ([91696cc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/91696cc35f1c4419322be91ae04aae806ec89bcf)), closes [univention/dev/internal/team-nubus#1168](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1168)

## [1.9.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.8.0...v1.9.0) (2025-05-05)


### Features

* Add Ingress for favicon related files ([50df258](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/50df25853038b91dc92e070877a8cbb547910939))
* Bump ucs-base-image version ([fe735af](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fe735af055ac6edf26151f90a5da74507f34f5ac)), closes [univention/dev/internal/team-nubus#1155](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1155)
* **guardian:** secret refactor ([518e1c5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/518e1c51d335d64b6c805e5d5e760526a9633aac)), closes [univention/dev/internal/team-nubus#1087](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1087)
* Keycloak 26 upgrade ([d471d6c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d471d6c9697309cd501f36903a76f50dbe5b017f)), closes [univention/dev/internal/team-nubus#1043](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1043)
* **ldap-server:** (Re)Creating LDAP indexes. ([f1c3a86](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f1c3a86d378530ea697c5f98c58eaa5208461fa7)), closes [univention/dev/internal/team-nubus#1019](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1019)
* **license-import:** Support for adding a license ([f410694](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f410694715c832f9684e3248523bf56617c0f546)), closes [univention/dev/internal/team-nubus#833](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/833)
* Migrate bitnami charts from docker.io to bitnami registry ([198967e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/198967ee0a4978b083ef579ee452912c3f863798)), closes [univention/dev/internal/team-nubus#1131](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1131)
* **portal-consumer:** refactor: use existingSecrets for portal-consumer ([c855337](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c855337db15fcb91c9484fa12d5cc62df8574ab4)), closes [univention/dev/internal/team-nubus#1091](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1091)
* **umc-server:** Run sssd sidecar non-root ([b67c8f5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b67c8f55fdc6d157f00f62fc672c5bd2bda39ad5)), closes [univention/dev/internal/team-nubus#1123](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1123)
* Update portal components to version 0.65.0 ([2357e6b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2357e6b797dcc4c77d7ab6043ce401eeadd40499))
* Update portal components to version 0.66.0 ([9058e7a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9058e7aba87447e539358328d828ab92e6650ed3))


### Bug Fixes

* **keycloak:** New version with error messages ([4c7b6f1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/4c7b6f16cee235a252305435cc71d5a24a5a4043)), closes [univention/dev/internal/team-nubus#996](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/996)
* make copy calls in container init more robust ([cacf062](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cacf0629bfbeb238ff6fb936c2f4467b9c404cef)), closes [univention/dev/internal/team-nubus#1079](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1079)
* Remove "nubusLdapServer.highAvailabilityMode" from values ([5b54b62](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5b54b62353684a5e40d70dd0861c6962004a9966))
* **umc-server:** non-root sssd and umc-server ([47dae34](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/47dae343798fe54ffac56bb98b0d7d25d4c7b1f9)), closes [univention/dev/internal/team-nubus#1123](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1123)
* Update portal components to version 0.66.1 ([137b415](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/137b415202e2643b18643c6d40dd3a8fae6fabbe)), closes [univention/dev/internal/team-nubus#1161](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1161)
* Update Portal components to version 0.66.2 ([db98c45](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/db98c459c41e940ae3ceaa734980454db2fad9ea))

## [1.8.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.7.0...v1.8.0) (2025-04-07)


### Features

* bump stack-data version ([acb5b8e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/acb5b8e2a26a3d6dcd10775578ec27c5f578eef5))
* bump stack-data version ([70a6532](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/70a6532562c78d81531cfd15758e9b255bd35b13))
* bump stack-data version ([901f55c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/901f55cd0d44cff73cf72f91497794c5585f60ea))
* bump stack-data-ums to 0.89.0 to remove obsolete user groups by default ([1838472](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1838472d20a6667da832a67855eb534f801edf0a))
* bump stack-data-ums to 0.89.0 to remove obsolete user groups by default - add Chart.lock ([25c5064](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/25c506457579b1cb9153f7f3283204de634b357a))
* bump stack-data-ums to 0.89.0 to remove obsolete user groups by default - add Chart.lock ([002854a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/002854a61f13f599cc0855ecb31565777afbe5c2))
* Bump version of UMC components to 0.38.0 ([0887299](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/0887299e6fef5759c1b5285abc9de1dc705c8601)), closes [univention/dev/internal/team-nubus#1048](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1048)
* **ldap-server:** integrate refactored existingSecrets of ldap-server (dev version) ([2b3f408](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2b3f408746fbf5c4d1fea4dcd2807927cea7973e)), closes [univention/dev/internal/team-nubus#1089](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1089)
* **portal-server:** Migrate object storage and central navigation secrets ([a19e82d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a19e82d214e0cbd9897ad93ee1c7abd98debbf7b)), closes [univention/dev/internal/team-nubus#1092](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1092)
* remove common from Chart to only use nubus-common which is not rate limited ([94f0bcd](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/94f0bcd12e1c701b63ecac20bf0e31a62e695f12))
* udm rest api not reachable by default ([6284610](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6284610f98ef007ef4797c50ff580cdaf4d2c964))
* Update ldap-server and -notifier to version 0.33.1 ([818ea5c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/818ea5c1b8c93b9fd6e864e617820bc59e18791b))
* Update portal components to version 0.57.0 ([410a2f5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/410a2f5833d8e061d4352509c9adf99cc7a91d9b))
* Update portal components to version 0.59.1 ([a1b3745](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a1b374580ba61d5e5628a52a390c841bc18557c6))


### Bug Fixes

* add adapted readme and chart lock file ([f7d194e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f7d194eb9f619289fa54a3a88a215dec0c8d6f85))
* Adding correct version tag of container-ldap ([ec3464b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ec3464b83f0b2069799e6c605283116863b768f9))
* bump lda-notifier version to dev version from mr for testing ([01270a6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/01270a6fcaadd9fadc4c1fa9b07cbc6c6495ac60))
* fix namespace templating ([05f970b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/05f970b5a081521b2475130b2d429e8a9cf99bdf)), closes [univention/dev/internal/team-nubus#1075](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1075)
* Integrate data-loader refactoring. (no functional changes) ([9ec8ca4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9ec8ca417b62885c024837126eac1ee317e08755))
* **keycloak:** Changed version to 0.9.2 ([0172950](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/0172950ec9c057aeee8327cdc81ac21fafb96569)), closes [univention/dev/internal/team-nubus#996](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/996)
* **ldap-server:** Resources templated correctlly on primary and secondary ([5894640](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/58946401116599a4e2555fe30e936d255a8eda1a)), closes [univention/dev/internal/team-nubus#1117](https://git.knut.univention.de/univention/dev/internal/team-nubus/issues/1117)
* Update portal components to version 0.57.3 ([f42fbaf](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f42fbaf673e0de96999ce0fb199aa41a1ea47141))
* Update portal components to version 0.57.4 ([dcc2049](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/dcc20493f3ae0400747687988934431883c83181))
* update the nats container images ([133401f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/133401f74061fb742e00586a89fb6a30c5ce1395))
* version bump of keycloak to 0.9.0 ([9ba54dc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9ba54dcb8f240e206f722e5e21c35ca8207a860a))
* version bump of keycloak to 0.9.0 bump Chart.lock ([1e30369](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1e30369dc020e0c90fdf05d65186b7cc03ba60ed))
* version bump of keycloak to 0.9.0 include Chart.lock ([f30e7b3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f30e7b3ee2cb776245d2bf1c47637b5c0544a2a4))

## [1.7.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.6.0...v1.7.0) (2025-02-28)


### Features

* Add new dependency "nubus-common" in version 0.8.0 ([862a91c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/862a91c7475912396fa0260df41bf371326bd2f7))
* adhoc provisioning ([eddab3c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/eddab3cb00c20c1ca5ce902e8e447cdbebbde199))
* Bump ucs-base-image to use released apt sources ([d94d64f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d94d64ff6673dd148d8a863fd7ce78ec925ece56))
* remove injected configuration from nubusStackDataUms ([abc934d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/abc934dde86c61113cdbf23b27575d11837addee))
* Remove portal related defaults regarding the log level configuration ([e8698a6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e8698a64df9c16e8912c020551d084468a73e389))
* Replace "global.nubusMasterPassword" with "global.secrets.masterPassword" ([17687dc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/17687dc1d6845f0183e7b412f85b7b1411e8d823))
* Update portal charts to version 0.51.0 ([d33a028](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d33a028180c680032a426e3a9f1e21b58819f741))
* Update portal subcharts to version 0.55.0 ([f8e3c76](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f8e3c766260b6692640a81827dbbee3f6c4a1261))
* Update portal-extension to version 0.55.0 ([1224be8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1224be8c1aaf7e75e4a5568f09b238af3e41d513))
* Update stack-data-ums to version 0.87.0 ([49c92d5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/49c92d5149f0e57692f6d681b7d692c2b605c4fb))


### Bug Fixes

* add resources to guardian ([32a3032](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/32a3032c917a04a70564789e5f4053155cf594fb))
* Bump stack-data chart to add the new data loader actions: modify_if_exists and ensure_list_does_not_contain ([cae1364](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cae136431472d6f5eaafeed608427e1f12927931))
* dispatch crashes if NATS connections fails. ([fe513a9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fe513a92b5ea6463566c56c26b4adfdce7db377c))
* fix keycloak-extensions database connection ([ca701c9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ca701c9468297dae70d78792dece3bb176550765))
* fix security context on portal consumer ([a3c2739](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a3c2739145be3fa1f7c6cea843cf0bad5a986f66))
* **keycloak-extensions:** Fix httpx dependency in keycloak-extensions handler ([676c679](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/676c679ecd07f6660ac3e62cea72257240a2a194))
* **keycloak-extensions:** Fix postgres SSL parsing so it is a boolean ([d3d3b57](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d3d3b57e8968b43e66e8927f5d257afb8efb5452))
* **keycloak-extensions:** handle failed promise in keycloak-extensions proxy ([5beb20f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5beb20fdcf4f3a6ea960e35a059ba2d7bbc527c4))
* set plugin mounts to read-only ([b098137](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b0981372dc4961a72a98e58ec76f38c3c97a00ea))
* **stack-data:** Do not disable OX Context UMC module via UCR ([7647d98](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7647d9842a05972d79746eb117715defd7c70529))
* **stack-data:** Excess pointers caused values and documentation to be double namespaced ([b85806f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b85806f6e7cabf49f317ad9402008ae11adaa4cb))
* **udm-listener:** Fix double resources key in statefulset ([1e7d72c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1e7d72c3113fa1d277dfcd5a9eb7326600938c52))
* Update provisioning subchart to version 0.49.1 ([98ea4b9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/98ea4b945b02a1f289ef589adcda5ffeeb3aaaa2))

## [1.6.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.5.1...v1.6.0) (2025-01-21)


### Features

* Allow to enabled/disable support Ingersses individually. ([4726af5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/4726af5d39b25cf634349b7d741685d14eef685f))
* Consolidate objectStorage configuration for portal components ([14f15da](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/14f15dae8c3db77351e56b30587ed6641e7f07fa))
* Correct name of udm listener to "provisioning-udm-listener" ([86f491e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/86f491e3510297ab5b943688ff8967be51174a8d))
* **guardian:** Enable guardian and ugprade it to v3.0.0 ([c9e0d1e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c9e0d1e4c8cd20f6a1b3d03e7b2dd4ed4148f8d8))
* **minio:** Remove configuration option "defaultBuckets" ([48225b9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/48225b9650a8f35232e307b6025ea48de800c143))
* **minio:** Use a read-only policy for the portal server ([cced2a9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cced2a9e72d63c14d99e31f2abd2b536acac4bb9))
* Remove unused objectStorage related helpers and reduce Ingress to bundled minio ([4448ca0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/4448ca04037ed8a7ce3baa08c72b1616a8856f11))
* upgrade keycloak-bootstrap to not use k8s hooks ([724a64a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/724a64a0b375d3a4be870cb07e4a7e641834dd1c))
* Upgrade portal-consumer / portal-server to version 0.50.0 ([0ff02b6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/0ff02b6efa9026bd151a98da5c422c579574c0ef))
* upgrade provisioning with new NATS chart ([9df584b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9df584ba81bd61a9a26f5dec604f5890e646976e))
* upgrade UCS base image to 2024-12-12 ([99444b3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/99444b3a7fe64dae77cfe583314f6e1564de7da2))


### Bug Fixes

* **ldap-server:** Overwrite the labelSelector on the primary service every 15 seconds to recover from initial state after the service is overwritten by helm ([07c48a2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/07c48a23ba226b97275d128b53634685e74af3c6))

## [1.5.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.5.0...v1.5.1) (2024-12-11)


### Bug Fixes

* kyverno lint fixes in subcharts ([5e2d334](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5e2d334ad1c49b46cb52dff32067e61c260b07eb))
* kyverno lint revert portal-consumer changes ([801b571](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/801b57187ccf7e226e1105819347b1483c9d901f))

## [1.5.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.4.0...v1.5.0) (2024-12-09)


### Features

* **ldap-notifier:** couple provisioning-udm-listener to ldap-server-primary-0 ([eb20005](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/eb200057290e8e2180cc4e1096bc5411acc67003))
* **ldap-server:** Improve database initialization logic to avoid data loss in specific failure scenarios ([6abcd30](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6abcd3021137c7398a58f5f049f29c285c349c60))


### Bug Fixes

* **portal-consumer:** Fix small secrets templating bug in the portal-consumer ([70569b2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/70569b2cc089a84a94c7e40a926b0426f574e7fe))

## [1.4.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.3.0...v1.4.0) (2024-12-03)


### Features

* Adjust "postgresql.auth" for notifications-api to new structure ([c8a7cc6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c8a7cc6dcaf23396d5e72ce778560f6bf220a83c))
* **keycloak-extension:** Integrate keycloak-extension secrets refactor ([8dd60d1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8dd60d174532f2d671b0498990d8f0065506f920))
* **keycloak-extensions:** added ssl support to the database connection on the proxy. ([04072a6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/04072a6fd3c83f3d7e11b1d2790ccf210d69d7b7))
* LDAP server leader elector ([257929f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/257929f747774e578a9e42dfb2fe74083abbbdc8))
* new defaults for the Users module ([8c71b85](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8c71b857e34e5e8598bc1c3c60d00114cc086503))
* **portal-frontend:** Flag to deactivate IPv6 support ([ec96ca8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ec96ca86febfc44a515ee670dfdce11482e243c2))
* **portal:** sync with ucs 5.2 ([b50683f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b50683ffe214bd701396618a06b38e2b48fd3a2c))
* **udm-rest-api:** integrate secret-refactoring ([a239624](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a239624759d450a2d28f29b188a62deebec963d5))
* **umc-server:** Integrate umc-server secrets refactor ([d71e114](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d71e1143c3fc3640e9fb46cae1c57d16f51e08e0))
* Update notifications-api to version 0.46.0 ([7c0ea4e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7c0ea4e0818f225376f8fbdd4caa370ac3d0e969))
* update umc-server and umc-gateway to 0.35.4 ([b227452](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b22745294db00ec888a6254b73e63bc3445eefe5))
* Update umc-server and umc-gateway to version 0.35.3 ([23b3865](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/23b38659f4c322484c8d2743e431916cc1603c7e))


### Bug Fixes

* kyverno lint errors ([b63e375](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b63e3753b20176a3a8608b66030309248ee1b5ff))
* **ldap-server:** remove file ownership errors in the univention-compatibility initContainer ([04fe4c2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/04fe4c2eaf1a909056b57afeee612141be4e0a74))
* **portal-frontend:** reload portal on branding changes. ([bea723c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/bea723cef902aeb754a34c580b2d3348b77a8d7f))
* simplify umbrella chart by removing releaseNameOverride ([0aa2693](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/0aa2693db7cc7311110b76d1dc0fc3a1409b41b7))
* **udm-rest-api:** use public artifacts instead of development ([3de241f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3de241f6fddfe86882616c2d9bce3300b9310693))

## [1.3.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.2.0...v1.3.0) (2024-11-13)


### Features

* **keycloak-bootstrap:** Integrate keycloak-bootstrap secrets refactor ([5895308](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/58953088d4cb9ba7792b2cb2d89ab44e8c1b95a2))

## [1.2.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.1.0...v1.2.0) (2024-11-13)


### Features

* **keycloak:** Integrate keycloak secrets refactor ([52d0cd4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/52d0cd44cbc0ae3c2553b242a10f2eb351bf7373))

## [1.1.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v1.0.0...v1.1.0) (2024-11-05)


### Features

* **provisioning:** Add "existingSecret" into template names ([195c10f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/195c10ffbc7d00b5f3a1e6cb6c45385f0f788a2f))
* **provisioning:** integrate the secrets refactoring in the provisioning chart ([92e21f8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/92e21f8b36ef6c187546ea79542733ee062e9828))
* **provisioning:** Use "existingSecret" pattern in "global.ldap.cnAdmin" configuration ([d0a35d7](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d0a35d772f0a02c409497989754a496afe1ccf17))


### Bug Fixes

* **provisioning:** Update provisioning charts to version 0.45.0 ([70a4d45](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/70a4d45ce94560e2563797dd80bda14d06eb3272))

## [1.0.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.74.0...v1.0.0) (2024-11-01)


### ⚠ BREAKING CHANGES

* trigger the nubus 1.0.0 version bump

### Features

* Release nubus version 1.0.0 ([1762b82](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1762b827308ed6446ba26766ec54e49c05c11c19))


### Bug Fixes

* add digest to wait-for-dependency image ([9c1d700](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9c1d700914e64b45edca702ee813bb5affbbaf6b)), closes [univention/customers/dataport/team-souvap#915](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/915)
* Add license information for trademarked logos ([f86e7dc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f86e7dc072b232e1e5e06ac42d06103ed9a518e8)), closes [univention/customers/dataport/team-souvap#915](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/915)
* Fix umc tile link ([1287eb7](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1287eb761ea57e3726b83b46f9d8d3bc7fb633f8))

## [0.74.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.73.1...v0.74.0) (2024-11-01)


### Features

* Adjust ldap related configuration comment in portalConsumer ([b041287](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b041287920aeefe9bb62d955586024db813efda3))
* Adjust objectStorage related configuration commen for portalConsumer ([a58368e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a58368e0ee1e09e642a1fecaf2fb40ec891af79e))
* Auth configuration for API users in provisioningApi ([0069e88](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/0069e884aed2a4e4ba003f2a29483bd9fcf712a7))
* Auth configuration for minio provisioning does respect configured credentials ([2961507](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/29615074c3e7ec444eeca01597a08aaca5ac06a3))
* Auth configuration for NATS access in provisioning components ([365238c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/365238c88a052dab805750f742c6067348994593))
* Auth configuration for NATS in selfservice-consumer ([d1acc0c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d1acc0c435fb716a09db5bcedbe41e6c6719d39a))
* Auth configuration for provisioningApi in selfservice-consumer ([52051cc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/52051cc93b7f62f9b4860e21f3d68dd8bfc46e97))
* Auth configuration of initial administrator password into templateContext of stack-data ([09a4c06](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/09a4c061e9622c585b7942689662a10508479a6d))
* Auth configuration of NATS admin password via provisioning.nats ([f945dbd](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f945dbd56155749d22f424e5cd9e09812350018d))
* Auth configuration of objectStorage for portal-consumer ([5e360b2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5e360b218a977935c436e9fef5c10e2e46d28185))
* Auth configuration of objectStorage for portal-server ([cde75df](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cde75df8ee7ce482b7ca363e68688577bfc9615f))
* Auth configuration of provisioningApi for portal-consumer ([cb80745](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cb8074535ba40d142e17a397e99c3a335385d409))
* Auth configuration of UDM API for portal-consumer ([a488b5b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a488b5be4440957ea175050136eb5682964b071e))
* Remove "credentialOverride.defaultAdminPassword" and "defaultUserPassword" ([07b0e27](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/07b0e278450ae944e256e0230c0e5f40e578142b))
* Remove obsolete auth configuration for portalListener ([402ddcd](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/402ddcd43295b37dc8dbc44e7cef4526c647a6a6))
* Update portal-consumer sub-chart to version 0.44.0 ([6bd0d0e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6bd0d0e2d4098a41d67a05c1b0e7f019819eb287))
* Use "global.ldap.auth" in Secret generation ([b7fccf6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b7fccf6953d43a456720a184495ca686510a6936))


### Bug Fixes

* Mark ldap related places which need a refactoring together with the sub-chart ([398ff0d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/398ff0de2db7ecf73910b28bf7064ff95c2b59d4))

## [0.73.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.73.0...v0.73.1) (2024-10-30)


### Bug Fixes

* Set keycloak umc-server and ldap-server replicas ([20b91eb](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/20b91ebed7d61597f5531233d6281637b2bac94a))

## [0.73.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.72.2...v0.73.0) (2024-10-29)


### Features

* **selfservice:** Integrate selfservice consumer secrets refactoring ([b27fe95](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b27fe951c071838fa814164ce7ee3ff288b0ba44))


### Bug Fixes

* **selfservice:** update selfservice consumer component chart ([8f64a19](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8f64a19f368d4822c90fa62c07228b7063868cdc)), closes [univention/customers/dataport/team-souvap#891](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/891)

## [0.72.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.72.1...v0.72.2) (2024-10-29)


### Bug Fixes

* Correct doc comment syntax in values file ([7281f93](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7281f93b56564f192287531410e82dbbbf2fbdeb))
* Correct outdated comment around "global.extensions" ([c93bad4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c93bad49ef994c4ea8ded5fa450a1287e4b162b5))

## [0.72.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.72.0...v0.72.1) (2024-10-28)


### Bug Fixes

* remove unused old listeners ([3fb17c2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3fb17c299e3721d6432ab90f6619855c50efe2a5))

## [0.72.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.71.1...v0.72.0) (2024-10-26)


### Features

* Migrate stack-data to jinja2 templates ([efcf37f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/efcf37fe67eff1307a3e1a1de70d6627ef7fb52b))

## [0.71.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.71.0...v0.71.1) (2024-10-25)


### Bug Fixes

* image name for the portal extension ([41d516c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/41d516c8f7a72c4d046b8d2ab7e0cbcdbfb36ea1))

## [0.71.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.70.2...v0.71.0) (2024-10-25)


### Features

* remove OX extension by default ([a155859](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a1558590ab70151cc3afd23d3be88e10ced24470))

## [0.70.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.70.1...v0.70.2) (2024-10-25)


### Bug Fixes

* temporarily disable guardian ([e8e862a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e8e862a3c97922ffa208b6d3f88ba763bf09f3ab))

## [0.70.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.70.0...v0.70.1) (2024-10-24)


### Bug Fixes

* change product name to proper capitalization ([fbacefd](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fbacefd4e961f359c701eaafe545fe68c20cf8df))

## [0.70.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.69.0...v0.70.0) (2024-10-23)


### Features

* upgrade stack-data chart ([fc697c5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fc697c5addff0e83ad5653ef065d7d2aa2969cd5))

## [0.69.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.68.1...v0.69.0) (2024-10-23)


### Features

* disable keycloak-extensions by default ([81fa3f1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/81fa3f1048f1062db39c931dfc8cef06748c510b))

## [0.68.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.68.0...v0.68.1) (2024-10-23)


### Bug Fixes

* release notes typo and missing namespaces ([37d1433](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/37d1433adf007dfc0b6b1aa08a777d9c12b97de4))

## [0.68.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.67.0...v0.68.0) (2024-10-22)


### Features

* add missing portal tiles ([cb99dc8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cb99dc8c3aa9339225d5d12f68523ad6938badc6)), closes [univention/customers/dataport/team-souvap#821](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/821)
* upgrade portal extension image ([c338f54](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c338f54bd6ac6954804044e0fb5d8c8ba383024d))

## [0.67.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.66.1...v0.67.0) (2024-10-22)


### Features

* use new univention-keycloak to configure CORS headers for Keycloak ([f2e9b1b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f2e9b1be9d7e6fba1aa44c4090ee41c9c0d57051))

## [0.66.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.66.0...v0.66.1) (2024-10-21)


### Bug Fixes

* Bump portal related charts ([5acf85e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5acf85ebcd6f8bd7c43a0ff67890b075251ebab6))

## [0.66.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.65.1...v0.66.0) (2024-10-16)


### Features

* enable keycloak events ([04bb72d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/04bb72de89c1420e4d5e00be393c01fbe5b5500e))

## [0.65.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.65.0...v0.65.1) (2024-10-15)


### Bug Fixes

* Integrate self-service DoS fix from upstream ([d97c98d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d97c98d6104985583f2e155b72c56c7b1e55cc67)), closes [univention/customers/dataport/team-souvap#880](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/880)

## [0.65.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.64.6...v0.65.0) (2024-10-14)


### Features

* enable showUmc for the portal and configure default modules ([be9e856](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/be9e8569c3e831c23394af594f4448a59b9c2cd2)), closes [univention/customers/dataport/team-souvap#862](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/862)

## [0.64.6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.64.5...v0.64.6) (2024-10-14)


### Bug Fixes

* remove newlines from nubus-minio-provisioning secret ([13faa72](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/13faa7253d49fc6b3dd8d658d09650d8d656ba7e))

## [0.64.5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.64.4...v0.64.5) (2024-10-14)


### Bug Fixes

* .Release.Name can't be used in yaml keys ([17d9215](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/17d92158052e4ae5501f0ce4ddfa4a3c1a257f0b))

## [0.64.4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.64.3...v0.64.4) (2024-10-11)


### Bug Fixes

* don't hard-code the release name of the minioProvisioning secret ([ef42e84](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ef42e846479a3f63d8cb2a1b596c6ca729ab2a4e))

## [0.64.3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.64.2...v0.64.3) (2024-10-11)


### Bug Fixes

* remove legacy unused user sys-idp-user ([a662740](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a66274018398f3f0eec11518e4d83e3a339fe7b4)), closes [univention/customers/dataport/team-souvap#838](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/838)

## [0.64.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.64.1...v0.64.2) (2024-10-09)


### Bug Fixes

* fix YAML charts ([e30f795](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e30f79508ab7f254a428912fa4ab3747145a869f))

## [0.64.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.64.0...v0.64.1) (2024-10-09)


### Bug Fixes

* fix ingress paths ([3557114](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3557114e17419ed67188271ffc74914c0c2d3902))

## [0.64.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.63.2...v0.64.0) (2024-10-05)


### Features

* Plain nubus theming parity with UCS ([de5c802](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/de5c8025ac04c3c67f1c6a52f96ae58a6f8b4366))

## [0.63.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.63.1...v0.63.2) (2024-10-03)


### Bug Fixes

* cleanup selfservice values ([035847e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/035847ee61fd5c8f3e39d206fb87070d9b2e2586))

## [0.63.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.63.0...v0.63.1) (2024-10-03)


### Bug Fixes

* upgrade umc-server chart ([2e05c94](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2e05c94c92ffd85c2e588b23b4ca255da20f5f93))

## [0.63.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.62.3...v0.63.0) (2024-10-02)


### Features

* **nubus:** Update portal charts to version 0.41.0 ([b751d37](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b751d377014cdac56dc89d3a0209d9a0701e1fbc))

## [0.62.3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.62.2...v0.62.3) (2024-10-02)


### Bug Fixes

* **provisioning:** safe KV updates ([2476e6f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2476e6f7f6d8e145506d3d868e62c03c937e5702))

## [0.62.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.62.1...v0.62.2) (2024-09-26)


### Bug Fixes

* **provisioning:** Bump provisioning to 0.43.1 ([e71eaa4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e71eaa4b7d9a9043da71167e6b90d128f62dcd62))

## [0.62.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.62.0...v0.62.1) (2024-09-26)


### Bug Fixes

* provisioning subscriptions format consistency and persistence ([90d34c6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/90d34c6cfc75beae6bfedab7f23db88a1e470317))

## [0.62.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.61.0...v0.62.0) (2024-09-25)


### Features

* remove cache http from portal ([b802dff](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b802dff6c457af311de7d0da43bb1a9225f32cf0))

## [0.61.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.60.0...v0.61.0) (2024-09-24)


### Features

* upgrade umc-server chart ([606e07f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/606e07f7f15c5256581828dd4bd54108eb0479e4))

## [0.60.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.59.1...v0.60.0) (2024-09-24)


### Features

* rename endpoints of Provisioning API ([760939b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/760939b91026e480cd6b07e91505fd83becfd1ba))

## [0.59.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.59.0...v0.59.1) (2024-09-23)


### Bug Fixes

* Don't leak secrets in bash scripts ([70adcd6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/70adcd6573d4e514a4e391cec80434a29fcf2056)), closes [univention/customers/dataport/team-souvap#843](https://git.knut.univention.de/univention/customers/dataport/team-souvap/issues/843)

## [0.59.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.58.1...v0.59.0) (2024-09-19)


### Features

* **register-consumer:** register ox-connector in the provisioning ([82a9515](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/82a951580f961e5118cfe4b825711315008fe542))

## [0.58.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.58.0...v0.58.1) (2024-09-18)


### Bug Fixes

* remove admin credentials ([9fdb1fc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9fdb1fc2f42660c62bb2c14e84242161234a7036))

## [0.58.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.57.3...v0.58.0) (2024-09-18)


### Features

* upgrade ucs base image in all subcharts ([3fe53fc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3fe53fc85f8e3c75f40313f5d81f2d494deb7ee4))

## [0.57.3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.57.2...v0.57.3) (2024-09-13)


### Bug Fixes

* Update portal components to version 0.38.3 ([3145fd2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3145fd2818dec38d22bdda5e50fc1a76f47dc6d4))

## [0.57.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.57.1...v0.57.2) (2024-09-12)


### Bug Fixes

* **provisioning-consumers:** make consumers wait until the subscriptions are created by the register-consumers job ([f97962c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f97962cad4e9aae5ad1c105da89c94efbf7d76cd))

## [0.57.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.57.0...v0.57.1) (2024-09-12)


### Bug Fixes

* set all log/debug levels to INFO or equivalent ([d06b201](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d06b201d736e44190b60296c6fe496e2ad82ca7d))
* set default service loglevels to INFO or equivalent ([7a602aa](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7a602aad9a150e391d6f0fcfdcd7f7740d03d453))

## [0.57.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.56.1...v0.57.0) (2024-09-12)


### Features

* **provisioning:** activate provisioning and consumers instead of listeners ([c8bef31](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c8bef315e0b83b92a26d92cc27926f245f478280))
* update udm-listener (BSI compliance) ([174d4f5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/174d4f50bcf4ba5ef14468bb0247cde3ce91f589))

## [0.56.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.56.0...v0.56.1) (2024-09-12)


### Bug Fixes

* disable logging of credentials during set_facts ([95fff96](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/95fff968ff4940cf6d7feb6695f1fc8b72576fad))

## [0.56.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.55.1...v0.56.0) (2024-09-11)


### Features

* upgrade stack-data chart ([38b9a61](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/38b9a61dd1819cc2748021d0b99705a3f49c141d))

## [0.55.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.55.0...v0.55.1) (2024-09-11)


### Bug Fixes

* **portal-consumer:** bump portal consumer version to integrate initial-values race-condition ([8bc6caf](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8bc6caf85759612139db462c545d7cba4f1b3695))

## [0.55.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.54.0...v0.55.0) (2024-09-11)


### Features

* **stack-data:** reload udm-rest-api cache ([97ee9b9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/97ee9b9fea0ce52326b6aa1c9dfcc096565de50c))

## [0.54.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.53.0...v0.54.0) (2024-09-10)


### Features

* Plain UMC login configurable ([31ea347](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/31ea3472b37ed97115a5acf8486acc230f006f01))

## [0.53.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.52.0...v0.53.0) (2024-09-10)


### Features

* **provisioning:** activate provisioning and consumers instead of listeners ([5ead0b2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5ead0b229f7528fb016f54e0dc58e2af8d155a82))

## [0.52.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.51.1...v0.52.0) (2024-09-10)


### Features

* remove installUmcpolicies parameter ([6c94541](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6c945412ee8d0b463a4367a8a3d49003f1b4b3ca))
* upgrade stack-data-ums version ([6725ee7](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6725ee74ce74ad78878820347dd87ece5c851bb4))

## [0.51.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.51.0...v0.51.1) (2024-09-09)


### Bug Fixes

* **ldap:** Configure LDAP Server Chart to only deploy one primary by default ([198953f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/198953f2b8ec755c623a96337aa562032a268b00))

## [0.51.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.50.1...v0.51.0) (2024-09-06)


### Features

* update ldap subchart (BSI compliant notifier) ([de2519a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/de2519a5316ddf1e8d8b94ac5bda97d53fa3a161))

## [0.50.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.50.0...v0.50.1) (2024-09-05)


### Bug Fixes

* **provisioning:** add credentialOverride for all provisioning secrets ([e533400](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e5334001c0ef55a935abdfbffaa2b641369cac60))

## [0.50.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.49.0...v0.50.0) (2024-09-05)


### Features

* **stack-data-swp:** Remove stack-data-swp chart ([d705260](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d705260c44e92407c46e3e2b34c38ff801ab36e8))

## [0.49.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.48.0...v0.49.0) (2024-09-04)


### Features

* BSI compliance portal-consumer ([676aaa5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/676aaa56ed778f35aa133acb542e9607705cfc23))

## [0.48.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.47.0...v0.48.0) (2024-09-03)


### Features

* remove default portal tile on plain nubus ([cec1f87](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cec1f87d0c5b0677c36ba4adfaaa8e8ae73a9d41))

## [0.47.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.46.0...v0.47.0) (2024-09-03)


### Features

* update umc-server subchart (BSI compliance) ([e55f9a5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e55f9a5253b856a7a42ef55d917db7c5ea8b8d71))

## [0.46.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.45.0...v0.46.0) (2024-09-03)


### Features

* **keycloak:** Use StatefulSets ([59d958f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/59d958f1cbbf718adeb18feefe1a6b06d341c3d9))

## [0.45.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.44.0...v0.45.0) (2024-09-03)


### Features

* configure UCR from Helm ([aacbeb8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/aacbeb81fe0dc40b8f63018e38879cb22134ca15))
* migrate dev users to external extension ([5235a87](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5235a879ba6c5ae9b09da2d5a9effa74954327c0))
* upgrade stack-data chart ([9b7aac0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9b7aac071821fa30b1f06a8b902b578f59ad3c72))


### Bug Fixes

* Add secret for Administrator user ([be83f5b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/be83f5bdde20530f704b9c022df00b059d9b9f61))
* set minio version ([48b26a8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/48b26a8114261cebbfcb8fc90da6d99ef39be165))

## [0.44.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.43.0...v0.44.0) (2024-09-02)


### Features

* bump portal and selfservice-listener ([aa90003](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/aa90003969f76ed760b107a8f7a1097db271fde9))

## [0.43.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.42.1...v0.43.0) (2024-09-02)


### Features

* configure UCR from Helm ([7f3d653](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7f3d6531447d11823c055c1968ee28c094bcbf92))

## [0.42.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.42.0...v0.42.1) (2024-08-30)


### Bug Fixes

* **keycloak:** update accidentally merged branch version of the keycloak chart ([59a40bc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/59a40bc9647c0228fb0ae520548b901a3f64824e))

## [0.42.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.41.1...v0.42.0) (2024-08-30)


### Features

* upgrade to keycloak 25 ([3242927](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3242927aebf715c8dd2282dc210e12d65e591348))

## [0.41.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.41.0...v0.41.1) (2024-08-29)


### Bug Fixes

* fix Keycloak init race condition ([be3e83b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/be3e83ba5781298a323e9d152ade323ed89bf578))

## [0.41.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.40.0...v0.41.0) (2024-08-29)


### Features

* create readonly user for ldap federation on plain nubus ([39d9619](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/39d9619fc68eec38badfe6e31db458b42700cfea))

## [0.40.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.39.3...v0.40.0) (2024-08-28)


### Features

* Bump ldap-server to UCS 5.2 and ldap-notifier ([97adfdc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/97adfdc2d63d0e6ed948f9537f2fe7eca03b66b8))
* Bump umc-server and gateway ([b859298](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b859298fa74683705f53db33a985dab75be2ceec))

## [0.39.3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.39.2...v0.39.3) (2024-08-28)


### Bug Fixes

* bump provisioning and stack-data ([b3da597](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b3da597da304536f8f7e2870bb2fb507b7371561))

## [0.39.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.39.1...v0.39.2) (2024-08-27)


### Bug Fixes

* **umc-server:** Update umc-gateway and umc-server to version 0.27.1 ([b5d125c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b5d125c14c09bcd31bf4a846144b3c5e0220e7d6))

## [0.39.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.39.0...v0.39.1) (2024-08-22)


### Bug Fixes

* **selfservice-consumer:** fix feature-flag typo ([3acdb20](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3acdb2083c6f31d98db3817e8c87c49fe65a1c86))

## [0.39.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.38.2...v0.39.0) (2024-08-22)


### Features

* **nubus:** Add certManager template for ingress ([4725259](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/47252590c055bf5a8ef876a574d6c2c647c2e204))


### Bug Fixes

* Downgrade ldap-server and ldap-notifier to version 0.20.0 ([ea32f16](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ea32f163879c277919112f1b046aa3ed4d9e650d))
* Pin the minio dependency to 14.7.0 ([1920e5d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1920e5dbe22c8d009bc76c14142b0803ec478a11))

## [0.38.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.38.1...v0.38.2) (2024-08-21)


### Bug Fixes

* **selfservice-consumer:** rename selfservice-listener to selfservice-consumer to avoid helm package bug ([47bafb6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/47bafb69cfed01d745849ac8f013a15c97a83268))

## [0.38.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.38.0...v0.38.1) (2024-08-21)


### Bug Fixes

* **provisioning:** put provisioning consumers behind a feature-flag ([a031258](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a031258cc2c912b1997fea9c422a5c64f17ed3fa))
* **provisioning:** temporarily add old secrets to enable provisioning consumers feature-flag ([849a440](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/849a440d9f8b0364e697fcd01efe45465119d4b7))

## [0.38.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.37.0...v0.38.0) (2024-08-19)


### Features

* update provisioning and add provisioning-based selfservice-consumer and portal-consumer ([9a60585](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9a60585aed48795a4787b2fd4da872e01e6a0399))
* upgrade only affected components ([28c5006](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/28c5006cb1f18aee47d932aa4db144ac19a56028))


### Bug Fixes

* bump selfservice-consumer and portal-consumer ([d1aaec0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d1aaec014ee0a0676fac97190409330957bd949c))
* set nats replicas back to 1 until nats clustering is stable ([9d46db6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9d46db6cc110e8fdb28131d6b6e9460eb6b11c4a))

## [0.37.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.36.0...v0.37.0) (2024-08-19)


### Features

* Use data-loader to load the ox-extension ([f75bea6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f75bea655607b05a65de3b162b7e7f4892fe027f))

## [0.36.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.35.0...v0.36.0) (2024-08-19)


### Features

* Add maildev into the CI setup ([4ce07f6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/4ce07f6fa83b9941ded0cbd5b5ea8afab1004a17))


### Bug Fixes

* Add trailing whitespace for the UCR configuration values which are empty ([942f403](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/942f4036e55b9d15c641d536743e8dda157fc4de))

## [0.35.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.34.0...v0.35.0) (2024-08-19)


### Features

* **umc-server:** Session stickyness ([a769fdf](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a769fdf0db5f68a0cbc0674103bdee1e7182769d))

## [0.34.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.33.1...v0.34.0) (2024-08-16)


### Features

* use univention-keycloak for guardian provisioning ([c72a6a2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c72a6a2ab4723bc48fb903e75eee1626e1212bd9))

## [0.33.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.33.0...v0.33.1) (2024-08-09)


### Bug Fixes

* drop unused menu patches ([5e7695f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5e7695ffb30de4bb5edc996d3c7e9d304c5b585f))

## [0.33.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.32.1...v0.33.0) (2024-08-05)


### Features

* migrate attribute-to-group mapper to external extension ([a2e5ec4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a2e5ec48c8881622d80e12b9546e5393c7257bdb))

## [0.32.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.32.0...v0.32.1) (2024-08-05)


### Bug Fixes

* **keycloak:** missing proxy configuration ([03bcba0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/03bcba017f2d031ce6c19e979467a489502f76af))
* **udm-rest-api:** Force udm-rest-api cache reload workaround from stack-data ([be08b85](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/be08b8561f2b74ea7e71ca36c00e04026a9ea8a2))

## [0.32.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.31.0...v0.32.0) (2024-08-05)


### Features

* **keycloak-extensions:** proxy scaling ([e2a150d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e2a150d6f8b6025ba1b28b3090045f729d414117))

## [0.31.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.30.0...v0.31.0) (2024-08-04)


### Features

* high-availability Keycloak ([cd16f24](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cd16f2449f11b93b37d8611e756aed6c6e13843a))

## [0.30.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.29.1...v0.30.0) (2024-08-02)


### Features

* migrate announcements to external extension ([370bb63](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/370bb63abcbd04d363fd3b14f3d759dfc8d9e7ed))

## [0.29.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.29.0...v0.29.1) (2024-08-01)


### Bug Fixes

* **keycloak-extensions:** mark emails as sent and better logging ([dec9b0a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/dec9b0a4e19d26bff93a6cd6704f2688c018242d))

## [0.29.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.28.1...v0.29.0) (2024-07-31)


### Features

* **keycloak-extensions:** bump python-keycloak to support newer Keycloaks ([ddce8a2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ddce8a204e2b2c9564f6c74967b06fe5ee6b370f))

## [0.28.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.28.0...v0.28.1) (2024-07-30)


### Bug Fixes

* UMC policies ([8fb731e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8fb731e11ab8a368e5f200dd9e5f07bcfc2470a9))
* Use ldap-server-primary since it shares the socket with ldap-notifier ([293dcfd](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/293dcfd0e46c95ea1dc68ac4821dffaab6088c30))

## [0.28.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.27.0...v0.28.0) (2024-07-30)


### Features

* update charts ([b803fd0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b803fd08c572ec2c6f909bd8fb4a238ec0c91ab8))


### Bug Fixes

* add missing configuration for selfservice-listener ([228b13e](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/228b13e0959b6db11e66348eb6c90c20fc71d779))

## [0.27.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.26.0...v0.27.0) (2024-07-24)


### Features

* remove old branding configuration ([cb6a077](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cb6a0771f7c7c22bfa662b8e67801eae82368675))
* udpate chart versions for theme configuration ([a8aa0f4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a8aa0f4700da0fb115a18b35f4c8b3911f9eddb9))

## [0.26.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.25.2...v0.26.0) (2024-07-19)


### Features

* Update stack-data-ums and stack-data-swp to version 0.55.1 ([7417548](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/74175486a93b947e3bf36f788881ed5a8661585b))
* Use the secondary ldap server by default ([de4e6b8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/de4e6b89139349e8544f50ccfc5c88cf563f1d26))

## [0.25.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.25.1...v0.25.2) (2024-07-18)


### Bug Fixes

* **nubus:** bump stack-data version to drop email templates ([d4b8b45](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d4b8b45b55b628da23660f03f6424c39614302b6))
* **nubus:** bump univention-portal to fix missing logo animation ([f616dad](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f616dadca6901e168f51568bee1afcc64e9c4e19))
* **nubus:** bump univention-portal to support central navigation shared secret ([cfed78f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cfed78fbfc619a0e845d8ce01a28b3a22097b948))

## [0.25.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.25.0...v0.25.1) (2024-07-16)


### Bug Fixes

* remove patch to set UMC page title ([cf8fb48](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/cf8fb480482ee683c8154eb9f53e5ed2d4d791c4))

## [0.25.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.24.1...v0.25.0) (2024-07-12)


### Features

* bump keycloak-extensions ([e64efe2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e64efe2c294474ecaf751a33e88930b34529a311))

## [0.24.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.24.0...v0.24.1) (2024-07-12)


### Bug Fixes

* Allow default users credentials to be overwritten ([670956d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/670956dbcfb6bc8f44f7a738c9edd24349cfb88b))
* make credentialOverride global to allow for use in subchart used template definitions ([3028da2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/3028da21fbdc7af1a252f4bcc315e20ce307ffea))

## [0.24.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.23.0...v0.24.0) (2024-07-11)


### Features

* add credentialOverride functionality ([1d876dc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/1d876dcd84c4ed2b5c6b52f8aeacfffe33b4a2a0))
* replace stack-gateway with ingress definitions ([223fb0d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/223fb0dae83a430288466156be5ce8f7a4fc988f))


### Bug Fixes

* **nubus:** Add further overridable ldap-server credentials ([08f136f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/08f136fcdbfa30a5003cf5ff1f1383d8529fb3a4))
* upstream change umc-server extra volumes ([b5887f9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b5887f9dc17402f551876363af50fc2adf3f2ae6))
* upstream extension changes ([5dd4b25](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5dd4b252c7139905cfcb86da8d9bcdc05bcebb9b))

## [0.23.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.22.1...v0.23.0) (2024-07-10)


### Features

* Update umc-server to ucs-520 image ([bd19ca6](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/bd19ca610b0a09554552469ea9a6fa0467d1b494))


### Bug Fixes

* Upstream umc-server ingress configuration ([066f542](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/066f542695b752498a6cca077cfbe3d3301de01f))

## [0.22.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.22.0...v0.22.1) (2024-07-05)


### Bug Fixes

* LDAP server version bump (uses UCS 5.2 sources) ([ec0c98a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ec0c98a348e216bfa5c0f7e89333a7b44f4ff5fd))

## [0.22.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.21.0...v0.22.0) (2024-07-05)


### Features

* configMap for self-service password email moved to sub-chart ([05868c2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/05868c26a66a4c334b0be7635530eb535bd9d81e))

## [0.21.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.20.0...v0.21.0) (2024-07-05)


### Features

* Update component charts to leverage extension configuration ([35e2ace](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/35e2acef04074966a04920fae4ebc4bcefa5c739))
* Update ox extension to version 0.10.0 ([302daf1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/302daf1ead8765545fecb196f8151f5bbb5a01a8))
* Update the Chart.lock file ([d5b3812](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d5b3812803147b8b6d452a7a4fe2c56f0f57c923))

## [0.20.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.19.5...v0.20.0) (2024-07-05)


### Features

* Configure portal and ox extensions ([561d019](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/561d019fa2c34c1cb13ea144c9c092ae0309de64))

## [0.19.5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.19.4...v0.19.5) (2024-07-04)


### Bug Fixes

* remove extensions from container-ldap ([c5b0327](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c5b03274266b4c3daa9257567da531c0aa715dec))

## [0.19.4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.19.3...v0.19.4) (2024-07-01)


### Bug Fixes

* udm-rest-api initContainer tags were wrongly set upstream ([ca7bcbb](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ca7bcbb116eee8c540fe2753845935fffd1b7a19))

## [0.19.3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.19.2...v0.19.3) (2024-06-27)


### Bug Fixes

* update notifcations-api sub-chart ([caaa13c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/caaa13c576f7a8e5b6566551d1d66ac21af5f094))

## [0.19.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.19.1...v0.19.2) (2024-06-27)


### Bug Fixes

* add prefix to nats passwords to avoid the possibility of them being interpreted as integers ([234469a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/234469a822160d85973e53253b7c362313298cd7))
* bump ucs-base to 5.0-8 ([a63c708](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a63c708fce1462e10ed14d37466e73478a44121c))

## [0.19.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.19.0...v0.19.1) (2024-06-25)


### Bug Fixes

* UDM REST API version bump (uses UCS 5.2 sources) ([0172c7a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/0172c7a006e70161dd4882c758ab50a07d2efbbf))

## [0.19.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.18.4...v0.19.0) (2024-06-25)


### Features

* disable password checks for default.admin, user and ldap search users ([ef7935c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ef7935cb3d2f6bd93ed223ba9220ae465c5ad464))

## [0.18.4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.18.3...v0.18.4) (2024-06-25)


### Bug Fixes

* keycloak-extensions bump version ([fbef4de](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/fbef4deaaa797ee38842683df0e7c1870a701981))

## [0.18.3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.18.2...v0.18.3) (2024-05-31)


### Bug Fixes

* **guardian:** provisioning from opendesk ([4e7180f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/4e7180f72bef09982e390d3771be3febdb61c533))

## [0.18.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.18.1...v0.18.2) (2024-05-30)


### Bug Fixes

* Update chart description with new product name. ([52e2ebe](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/52e2ebe3d3aa45eff3a3e7d003544e6871feb1af))

## [0.18.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.18.0...v0.18.1) (2024-05-28)


### Bug Fixes

* Add annotation for ingress-nginx ([367cb2c](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/367cb2cdada632994a1ed0702ea05087e5317d60))
* Tweak password derivation to avoid trouble during bootstrap ([a163e20](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a163e208fe112ac8a60b6ad5088e68684559c818))

## [0.18.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.17.0...v0.18.0) (2024-05-27)


### Features

* value deduplication ([d81ed74](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d81ed74f0844360495d0b95dd318430889ea6702))

## [0.17.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.16.1...v0.17.0) (2024-05-27)


### Features

* Add interim "stage1_values" ([bdbe63b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/bdbe63bb094cbf7c742ca54fdeb8d610d37c78d6))
* Add minimal Helmfile to deploy nubus ([736db95](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/736db958ff6197745fce0b49c90b01ce32f57f60))
* Add notes about certificates installation in the CI environment ([9d6bf92](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9d6bf92f8e1a1ea3f7f8c90192e6ff1f112e3f45))
* Add support for reviewPrefix in CI deployment ([f373d99](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f373d997c1f330432e9169216afebd1309cc31a9))
* Add values file with the current public image configuration ([50702e3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/50702e3ba0d964b74f27d57c65119b46935d6e72))
* Allow to override the chart version dynamically ([8af44bb](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8af44bb61190d42aea924ae34463f2fde155422f))
* Capture domain specific configuration into a dedicated file ([edc9b01](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/edc9b016b63c3bb3e0020472bf325a9dbc7f517b))
* Copy CI certificate into target namespace ([c77c8c7](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c77c8c7ca33dc9bc0e0f80ba829a5c2aae8b154e))
* Use secret name "certificates-tls" for ingress configuration ([b89fea8](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b89fea8c04f437dbdf39de1db76aa7c67d100830))


### Bug Fixes

* Adjust postgresql configuration for guardian update ([f8fa53a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/f8fa53a3cbf38e563aaeb2a1a807c9f4c6efd14b))
* Adjust values configuration to updated keycloak dependency ([87c6ccd](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/87c6ccdd9f24da84c4ae74a373008d1e17cdf6a1))
* Cleanup domain_values.yaml ([34b6ab9](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/34b6ab9b36544f6bc0f0786ce1c01479a0073a5c))
* Cleanup the outdated todo remark around keycloak-bootstrap and the related setting ([11b0447](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/11b04477734eb14e3559e85eb38f0362750514da))
* Comment out the login entry in the dev values ([8a1eb11](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/8a1eb118c5a30acaf8a4f3926161044a0427b833))
* Correct database configuration for notifications-api in linter values ([2139364](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2139364e7873e511ff1b2140a3946000ce05af31))
* Correct domain for keycloak-bootstrap ([711142f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/711142fd87635d9d3367c4074d9e5df689344d0b))
* Correct keycloak configuration in linter values ([e5449c5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e5449c5027289a9a1f08685b3f2684b5ba86966f))
* Correct open policy agent service name in linter values ([e31af90](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e31af90f9907709f1d6b7385327ea67b6fa286b8))
* Correct the upstream configuration for guardian/opa in stack-gateway ([7f0a701](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/7f0a701c66ecf598a0aae346b3ee520b09ff6023))
* Enable TLS in the keycloak extensions ingress ([c6af8fa](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/c6af8faef81c2e9a158e917d991fcf06c8fdde16))
* Enabled ingress for keycloak-extensions ([20e7760](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/20e776079ffd72150a5318a1e5f856b4e0b96f6c))
* Ensure that umc-server deploys its dependencies ([5f6ebaf](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/5f6ebaf04343aa2f36938e622db6047b6eba9484))
* Provide "reviewPrefix" from within the helmfile ([16a0eeb](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/16a0eeb00d5992549e70da8e06399e91f7ebf9c7))
* Provide domain into stack-data-swp ([6af7529](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6af7529191ee4034e4bc0f5f22f4cad36e02537a))
* Provide ldapBase for stack-data-swp ([209e547](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/209e5478c960d62c1d1bd53280ef86d39ed3a3c3))
* Remove duplicated entry for stack-gateway ([30bd314](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/30bd314e26d08c59ae160c1ecc29f3f106c189fd))
* Remove the tag configuration for keycloak-bootstrap in linter values ([a7ee3ab](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/a7ee3ab0926092791cf7e5e8f5ec73eaf9d75d2f))
* Setting stub value for bundled postgresql of notifications-api ([e80d84a](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e80d84a39d59bf348718e8e77aaf001cd39f3fb4))
* Switch off the Ingress configuration in linter values consistently ([9e1de65](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/9e1de65863c34e3b284c3ab5ddb47aeee6b62898))
* Update extraSecrets configuration in linter values ([284d338](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/284d3383d25f78c176f077285256f4456bea57ad))
* Update image configuration regarding the udm-rest-api ([b308eea](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/b308eeade0384654b016f2293869b3430877c374))
* Use secretRef for guardian credentials ([44339be](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/44339beefb713cde5755787c87e3595d7cdfa990))

## [0.16.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.16.0...v0.16.1) (2024-05-23)


### Bug Fixes

* Adjust linter_values to match latest guardian configuration schema ([e3a8c1d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e3a8c1d7d95509074da2fa346e36082eeab5eb49))
* Adjust the extra ingress configuration around the portal frontend ([94edb57](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/94edb5726f062d6ae7c2578ae0e39615067bf25b))

## [0.16.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.15.0...v0.16.0) (2024-05-21)


### Features

* **guardian:** deduplicated yaml values ([85ef851](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/85ef851dc11b0f53818280601c1602a1784c8472))

## [0.15.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.14.0...v0.15.0) (2024-05-20)


### Features

* upgrade keycloak version ([051f386](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/051f386c44fa21ff12a27e295d293ecf5e787acf))

## [0.14.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.13.0...v0.14.0) (2024-05-16)


### Features

* update provisioning subchart ([46f24ad](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/46f24ad0253fc82b4eae6674004da0d47b702de0))


### Bug Fixes

* update linter values ([4fb8e88](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/4fb8e88901a94a18b4ac42b844415b55094a1c9a))

## [0.13.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.12.0...v0.13.0) (2024-05-14)


### Features

* update keycloak-bootstrap subchart ([6065ac3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6065ac36f248cbe5e053eec716c2d82b38eb0cdd))


### Bug Fixes

* update keycloak-extensions subchart ([2cd3233](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2cd323328771ee348aa5f8b83c46dff728a19e62))

## [0.12.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.11.2...v0.12.0) (2024-04-29)


### Features

* pre-refactored umbrella with refactored sub charts ([50a2d56](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/50a2d56e86912158e5d83ee955fdf725e9575322))

## [0.11.2](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.11.1...v0.11.2) (2024-04-26)


### Bug Fixes

* Update portal-listener images to 0.20.7 ([744b48b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/744b48bae39539440f4c738482be2c6e39c24017))
* Update portal-listener to 0.20.7 ([d772342](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/d7723429aed43c5389f672ab2943c1c4ab1536d1))

## [0.11.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.11.0...v0.11.1) (2024-04-17)


### Bug Fixes

* Update provisioning to version 0.23.1 ([52f2d82](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/52f2d8269c5ae2718361eab975ad037fbed8a977))

## [0.11.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.10.0...v0.11.0) (2024-04-05)


### Features

* **guardian:** demo values ([6f72032](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/6f7203242db9c642162101c9b663087c3a4b46cb))


### Bug Fixes

* **guardian:** default value with no trailing slash ([ca34394](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ca343943d7ba97ba02b4b11eaf624715992d08d5))
* update dependencies ([95c935d](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/95c935d795558babed7bfd29d951932527a50f98))

## [0.10.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.9.1...v0.10.0) (2024-04-05)


### Features

* **guardian:** refactor values ([ec017e5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/ec017e5115ee065336ccd8db09c6a0fdf24d89f5))

## [0.9.1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.9.0...v0.9.1) (2024-04-02)


### Bug Fixes

* reference updated charts (container-umc) ([243d873](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/243d873f8174501fa7aaa6df232bd9d2b821f6cc))

## [0.9.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.8.0...v0.9.0) (2024-03-28)


### Features

* **guardian:** guardian keycloak provisioning and settings ([efeea2f](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/efeea2fd5f4d2b044f85af3e515efbd39bec8ec0))

## [0.8.0](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.7.5...v0.8.0) (2024-03-25)


### Features

* **helm:** demo values ([87ea152](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/87ea1520a24f608a0560fa5b8bf20bb60eb40007))


### Bug Fixes

* default to enabled keycloak bootstrap ([e5a1341](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e5a13413bcf681135e4398dc79b8447475e376fd))
* remove contact details ([81afd3b](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/81afd3b88b6aa3157385aa1e659e7827ea2981fc))

## [0.7.5](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.7.4...v0.7.5) (2024-03-25)


### Bug Fixes

* **univention-management-stack:** update helm chart ([e9125fc](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/e9125fc5434365cd9426b5e6008ee7b83bf94d8a))

## [0.7.4](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.7.3...v0.7.4) (2024-03-21)


### Bug Fixes

* missing values ([44b25b1](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/44b25b1c4f042fca8e4666114e067ef64fd1f3e3))

## [0.7.3](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/compare/v0.7.2...v0.7.3) (2024-03-21)


### Bug Fixes

* **ci:** renovate target branch ([2b8bd95](https://git.knut.univention.de/univention/customers/dataport/upx/ums-stack/commit/2b8bd9543614acc3d72cd9775b7d61bea83040f0))

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
