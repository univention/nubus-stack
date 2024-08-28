# Changelog

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
