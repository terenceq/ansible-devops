# Dependencies Playbooks

## Install AMQ Streams
AMQ Streams operator will be installed into the `amq-streams` namespace, a cluster named `maskafka` will be created using the small configuration and `ibmc-block-gold` as the storage class.  The generated configuration for MAS will be available in the `~/masconfig` directory on the local system.

Refer to the [amqstreams](../roles/amqstreams.md) role documentation for more information.

```bash
export KAFKA_STORAGE_CLASS=ibmc-block-gold
export MAS_INSTANCE_ID=masdev1
export MAS_CONFIG_DIR=~/masconfig

ansible-playbook playbooks/dependencies/install-amqstreams.yml
```

## Install MongoDb (CE)
MongoDb CE operator will be installed into the `mongoce` namespace, a 3 node cluster cluster will be created.  The cluster will bind six 20GB `ibmc-block-gold` PVCs, these provide persistence for the data and system logs across the three nodes.  The generated configuration for MAS will be available in the `~/masconfig` directory on the local system.

Refer to the [mongodb](../roles/mongodb.md) role documentation for more information.

```bash
export MONGODB_STORAGE_CLASS=ibmc-block-gold
export MAS_INSTANCE_ID=masdev1
export MAS_CONFIG_DIR=~/masconfig

ansible-playbook playbooks/dependencies/install-mongodb-ce.yml
```


## Install BAS
Installs **IBM Behavior Analytics Services** on IBM Cloud Openshift Clusters (ROKS) and generates configuration that can be directly applied to IBM Maximo Application Suite.

Before you use this playbook you will likely want to edit the `mas_config_dir` variable to supply your own configuration, instead of the sample data provided.
This is the directory where this playbook will store BAS configurations such as BAS endpoint and username/password credentials to configure BAS in your Maximo Application Suite instance.

### Required environment variables
- `BAS_CONTACT_MAIL` Defines the email for person to contact for BAS
- `BAS_CONTACT_FIRSTNAME` Defines the first name of the person to contact for BAS
- `BAS_CONTACT_LASTNAME` Defines the last name of the person to contact for BAS

### Optional environment variables
- `BAS_USERNAME` BAS default username. If not provided, default username will be `basuser`.
- `BAS_PASSWORD` Defines the password for your BAS instance. If not provided, a random 15 character password will be generated.
- `BAS_GRAFANA_USERNAME` Defines the username for the BAS Graphana instance, default is `basuser`.
- `BAS_GRAFANA_PASSWORD` Defines the password for BAS Graphana dashboard. If not provided, a random 15 character password will be generated
- `BAS_NAMESPACE` Defines the targetted cluster namespace/project where BAS will be installed. If not provided, default BAS namespace will be 'ibm-bas'.

### Usage:

```bash
export BAS_NAMESPACE=ibm-bas
export BAS_USER=basuser
export BAS_PASSWORD=xxx
export BAS_GRAFANA_USER=basuser
export BAS_GRAFANA_PASSWORD=xxx
export BAS_CONTACT_MAIL=xxx@xxx.com
export BAS_CONTACT_FIRSTNAME=xxx
export BAS_CONTACT_LASTNAME=xxx

ansible-playbook playbooks/dependencies/install-bas.yml
```



## Install SLS
Before you use this playbook you will likely want to edit the `mas_config_dir` variable to supply your own configuration, instead of the sample data provided.

### Required environment variables
- `SLS_ENTITLEMENT_KEY` Provide your IBM entitlement key

### Optional environment variables
- `SLS_CATALOG_SOURCE` Set to `ibm-sls-operators` if you want to deploy pre-release development builds
- `SLS_CHANNEL` Override the default release channel (3.x)
- `SLS_ICR_CP` Override the registry source for all container images deployed by the SLS operator
- `SLS_ICR_CPOPEN` Override the registry source for all container images deployed by the SLS operator
- `SLS_ENTITLEMENT_USERNAME` Override the default entitlement username (cp)
- `SLS_NAMESPACE` Override the default entitlement username (ibm-sls)
- `SLS_STORAGE_CLASS` Defines Storage Class to be used by SLS Persistent Volumes
- `SLS_LICENSE_ID` Must be set to the license id specified in the license file when one is provided
- `SLS_REGISTRATION_KEY` optional var when you want to install sls using a registration key you have.

### Example usage: release build

```bash
export SLS_INSTANCE_ID=xxx
export SLS_ENTITLEMENT_KEY=xxx
export SLS_STORAGE_CLASS=xxx

ansible-playbook playbooks/dependencies/install-sls.yml
```

!!! note
    Lookup your entitlement key from the [IBM Container Library](https://myibm.ibm.com/products-services/containerlibrary)


### Example usage: pre-release build

```bash
export SLS_CATALOG_SOURCE=ibm-sls-operators
export SLS_CHANNEL=3.1.0-pre.stable
export SLS_INSTANCE_ID=xxx

export SLS_ICR_CP=wiotp-docker-local.artifactory.swg-devops.com
export SLS_ICR_CPOPEN=wiotp-docker-local.artifactory.swg-devops.com
export SLS_ENTITLEMENT_USERNAME=$W3_USERNAME_LOWERCASE
export SLS_ENTITLEMENT_KEY=$ARTIFACTORY_APIKEY
export SLS_STORAGE_CLASS=xxx


ansible-playbook playbooks/dependencies/install-sls.yml
```

!!! important
    You must have already installed the development (pre-release) catalogs, pre-release builds are not available directly from the IBM Operator Catalog.