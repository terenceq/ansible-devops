## Changes
Note that links to pull requests prior to public release of the code (4.0) direct to IBM GitHub Enterprise, and will only be accessible to IBM employees.

- `10.3` Multiple Updates:
    - Add support for Cloudflare DNS integration ([#349](https://github.com/ibm-mas/ansible-devops/pull/349))
    - Support creation of Db2 LDAP user ([#330](https://github.com/ibm-mas/ansible-devops/pull/330))
- `10.2` Deploy Grafana in `cluster_monitoring` role ([#336](https://github.com/ibm-mas/ansible-devops/pull/336))
- `10.1` Multiple Updates:
    - Update suite application roles to support Optimizer application ([#309](https://github.com/ibm-mas/ansible-devops/pull/309))
    - Support AIO configuration in Manage ([#316](https://github.com/ibm-mas/ansible-devops/pull/316))
    - Consolidate entitlement management ([#323](https://github.com/ibm-mas/ansible-devops/pull/323))
    - Add support for source & channel selection to `mas-devops-sls` Tekton task ([#324](https://github.com/ibm-mas/ansible-devops/pull/324))
- `10.0` One-click installer support ([#285](https://github.com/ibm-mas/ansible-devops/pull/285), [#296](https://github.com/ibm-mas/ansible-devops/pull/296), [#299](https://github.com/ibm-mas/ansible-devops/pull/299))
- `9.0` Multiple Updates:
    - Added ability to set annotations onto suite CR ([#269](https://github.com/ibm-mas/ansible-devops/pull/269))
    - Add Assist install playbooks ([#271](https://github.com/ibm-mas/ansible-devops/pull/271))
    - Added gencfg-sls and gencfg-uds playbooks for using existing SLS and UDS ([#275](https://github.com/ibm-mas/ansible-devops/pull/275))
    - Add new required var `CPD_METADB_BLOCK_STORAGE_CLASS` for CP4D 4.0 ([#273](https://github.com/ibm-mas/ansible-devops/pull/273))
- `8.0` Multiple Updates:
    - SMTP email support for Azure and other changes ([#265](https://github.com/ibm-mas/ansible-devops/pull/265))
    - Configure azurefiles storage class for multi-cloud ([#260](https://github.com/ibm-mas/ansible-devops/pull/260))
    - Create secure route to CP4D web client when setting up DNS using CIS and suite_dns role ([#251](https://github.com/ibm-mas/ansible-devops/pull/251))
    - Add cp4d_wds role for discovery instance provison ([#234](https://github.com/ibm-mas/ansible-devops/pull/234))
    - Change MAS_APPWS_COMPONENTS variable format ([#267](https://github.com/ibm-mas/ansible-devops/pull/267))
- `7.0` Mulitple Updates:
    - Consolidate cluster specific provision/deprovision playbooks ([#236](https://github.com/ibm-mas/ansible-devops/pull/236))
    - Fix SLS bootstrap and update docs ([#242](https://github.com/ibm-mas/ansible-devops/pull/242))
    - Support GPU node in OCP on ROKS ([#224](https://github.com/ibm-mas/ansible-devops/pull/224))
    - Azure support for OCP cluster deployment ([#243](https://github.com/ibm-mas/ansible-devops/pull/243))
    - Add UDSCfg (BASCfg) generator ([#210](https://github.com/ibm-mas/ansible-devops/pull/210))
- `6.5` Multiple Updates:
    - Add JDBCCfg generator role ([#188](https://github.com/ibm-mas/ansible-devops/pull/188))
    - Add mustgather clusterTask to pipeline and new mustgather_download playbook ([#222](https://github.com/ibm-mas/ansible-devops/pull/222))
- `6.4` Add support for MVI deployment ([#196](https://github.com/ibm-mas/ansible-devops/pull/196))
- `6.3` Allow `ocp_server` and `ocp_token` to be used for `ocp_login` ([#211](https://github.com/ibm-mas/ansible-devops/pull/211))
- `6.2` Multiple Updates:
    - Support manual upgrade approvals ([#205](https://github.com/ibm-mas/ansible-devops/pull/205))
    - Add support for Db2u operator ([#203](https://github.com/ibm-mas/ansible-devops/pull/203))
    - Add Workspace config generator ([#189](https://github.com/ibm-mas/ansible-devops/pull/189))
- `6.1` Create WSL project and enable HPU deploy ([#201](https://github.com/ibm-mas/ansible-devops/pull/201))
- `6.0` Multiple Updates:
    - Upgrade to [kubernetes.core](https://docs.ansible.com/ansible/latest/collections/kubernetes/core/) Ansible module ([#194](https://github.com/ibm-mas/ansible-devops/pull/194))
    - Remove BAS support (replaced by UDS) ([#194](https://github.com/ibm-mas/ansible-devops/pull/194))
- `5.3` Multiple Updates:
    - Add support for db2wh backup & restore ([#133](https://github.com/ibm-mas/ansible-devops/pull/133))
    - Add support for appConnect ([#170](https://github.com/ibm-mas/ansible-devops/pull/170))
    - Switch BAS from FullDeployment to AnalyticsProxy ([#178](https://github.com/ibm-mas/ansible-devops/pull/178))
- `5.2` Multiple Updates:
    - Support MongoDb CPU and memory configuration ([#158](https://github.com/ibm-mas/ansible-devops/pull/158))
    - Separate CIS_APIKEY support for MAS Installation ([#156](https://github.com/ibm-mas/ansible-devops/pull/156))
    - Support configurable prometheus storage & retention policy ([#151](https://github.com/ibm-mas/ansible-devops/pull/151))
    - Support configurable application spec ([#160](https://github.com/ibm-mas/ansible-devops/pull/160))
- `5.1` Multiple Updates:
    - Add support for Cloud Object Storage setup ([#122](https://github.com/ibm-mas/ansible-devops/pull/122))
    - Conditional application deployment in Tekton pipelines ([#118](https://github.com/ibm-mas/ansible-devops/pull/118))
    - Add support for CP4D v4 alongside existing support for v3.5 ([#93](https://github.com/ibm-mas/ansible-devops/pull/93))
- `5.0` Multiple Updates:
    - Add support for AI Applications' must-gather tooling ([#91](https://github.com/ibm-mas/ansible-devops/pull/91))
    - Migrate airgap support into ibm.mas_airgap collection ([#38](https://github.com/ibm-mas/ansible-devops/pull/38))
    - Support for Assist application ([#76](https://github.com/ibm-mas/ansible-devops/pull/76))
    - Significant refactoring for CP4D support ([#68](https://github.com/ibm-mas/ansible-devops/pull/68))
    - Migrate build system to GitHub Actions ([#68](https://github.com/ibm-mas/ansible-devops/pull/68))
- `4.5` Add support for Manage ([#61](https://github.com/ibm-mas/ansible-devops/pull/61))
- `4.4` Add CP4D and DB2W playbooks ([#51](https://github.com/ibm-mas/ansible-devops/pull/51))
- `4.3` Add support for playbook junit result generation ([#39](https://github.com/ibm-mas/ansible-devops/pull/39))
- `4.2` Add support for Tekton pipelines ([#34](https://github.com/ibm-mas/ansible-devops/pull/34))
- `4.1` Add `ocp_verify` role and associated playbook ([#20](https://github.com/ibm-mas/ansible-devops/pull/20))
- `4.0` Initial Public Release on ibm.mas_devops ([#5](https://github.com/ibm-mas/ansible-devops/pull/5))
- `3.3` Support configurable SLS settings ([#53](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/53))
- `3.2` Add support for BAS ([#44](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/44))
- `3.1` Add support for SLS ([#35](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/35))
- `3.0` Switch to config dir instead of config file list ([#36](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/36))
- `2.7` Support AirGap install of MAS ([#28](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/28))
- `2.6` Add support for Gen2 application mgmt (install and configure) ([#24](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/24))
- `2.5` Add support for Watson Studio ([#16](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/16))
- `2.4` Add support for MongoDb Community Edition ([#25](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/25))
- `2.3` Add support for IBM Cloud resource groups ([#20](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/20))
- `2.2` Support DNS and certificate mgmt with CIS & LetsEncrypt ([#10](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/10))
- `2.1` Add support for AMQ Streams (Kafka) ([#19](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/19))
- `2.0` Major refactor of the roles and playbooks ([#17](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/17))
- `1.2` Add initial Spark support (incomplete) ([#15](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/15))
- `1.1` Enable db2wh SSL and generate jdbccfg for MAS ([#9](https://github.ibm.com/maximoappsuite/mas-devops-ansible/pull/9))
- `1.0` Initial release