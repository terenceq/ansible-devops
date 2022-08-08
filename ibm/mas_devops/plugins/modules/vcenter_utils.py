# coding: utf-8 -*-
# # (C) Copyright IBM Corp. 2020 All Rights Reserved.
# Eclipse Public License 2.0 (see https://spdx.org/licenses/EPL-2.0.html)

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: vcenter_utils

short_description: A collection of utilities for VCenter

version_added: "1.0.0"

description: Provides a collection of utilities for VCenter

options:
    vcenter_host:
        description: Host name of VCenter admin endpoint.
        required: true
        type: str
    vcenter_username:
        description: username of VCenter admin.
        required: true
        type: str
    vcenter_password:
        description: true
        required: true
        type: str
    certificates:
        description: true
        required: true
        type: complex

author:
    - @cuddlyporcupine
'''

from ansible.module_utils.basic import AnsibleModule

import requests
import urllib3
import tempfile
import os
from vmware.vapi.vsphere.client import create_vsphere_client

def pingVCenter(module):
    vcenter_host     = module.params.get('vcenter_host')
    vcenter_username = module.params.get('vcenter_username')
    vcenter_password = module.params.get('vcenter_password')

    # Configure REST session (disable cert verification and insecure warnings)
    session = requests.session()
    session.verify = False
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    try:
        module.log(msg="ping {}".format(vcenter_host))
        vclient = create_vsphere_client(server=vcenter_host,
                                        username=vcenter_username,
                                        password=vcenter_password,
                                        session=session)
    except Exception as ex:
        module.fail_json(msg = f"Unexpected error: {str(ex)}")
    
    return module.exit_json(changed=False, meta={'info': 'pingVCenter'})

def main():
    fields = dict(
        vcenter_host = dict(
            type = "str",
            required = True,
        ),

        vcenter_username = dict(
            type = "str",
            required = True,
        ),

        vcenter_password = dict(
            type = "str",
            required = True,
            no_log = True,
        ),

        method = dict(
            type = "str",
            required = True,
        ),
    )

    module = AnsibleModule(
        argument_spec=fields,
        supports_check_mode = True,
    )

    methodName = module.params.get('method')
    method = globals()[methodName]
    method(module)

    '''
    # Construct Mongo URI
    params_config = module.params.get('config')
    if params_config is not None:
        mongo_uri = 'mongodb://'

        # Add creds
        mongo_uri += f"{params_config['username']}:{params_config['password']}@"

        # Add hosts
        nodes = []
        for host in params_config['hosts']:
            nodes.append(f"{host['host']}:{host['port']}")
        mongo_uri += ','.join(nodes)

        # Add options
        mongo_uri += "/?"

        # LDAP
        if params_config['authMechanism'] == 'PLAIN':
            mongo_uri += f"authSource=$external&authMechanism=PLAIN"
        # Regular
        else:
            auth_source = params_config['configDb']
            mongo_uri += f"authSource={auth_source}"
    else:
        mongo_uri = module.params['mongo_uri']


    ca_file = None
    mongo_client = None
    try:
        # Write certificates out to a (temporary) file so we can pass them into pymongo
        if module.params['certificates'] is not None:
            with tempfile.NamedTemporaryFile(delete=False) as ca_file:
                for certificate in module.params['certificates']:
                    ca_file.write(bytes(certificate['crt'], 'utf-8'))
                    ca_file.write(b'\n')

        try:
            mongo_client = pymongo.MongoClient(
                mongo_uri,
                tls = True,
                tlsCAFile = ca_file.name if ca_file is not None else None,
                tlsAllowInvalidCertificates = False
            )
        except Exception as ex:
            module.fail_json(msg = f"Unable to initialize mongo client: {str(ex)}")


        try:
            inst_id = module.params['instance_id']

            # Drop databases as defined in https://github.ibm.com/maximoappsuite/coreapi/blob/bbd6607a42f0cb4d645ce59dfd4ec75d6567832c/image/coreapi/src/wipeData.py#L133
            db_names = mongo_client.list_database_names()

            dbs_to_drop = [
                f'mas_{inst_id}_core',
                f'mas_{inst_id}_catalog',
                f'mas_{inst_id}_adoptionusage'
            ]

            # Map to a list of (db_name, exists?) tuples so we can return information
            # about what was *actually* dropped in the results
            db_statuses = list(
                map(
                    lambda db_name :
                        dict(
                            name = db_name,
                            exists = db_name in db_names
                        ),
                    dbs_to_drop
                )
            )

            # discover any iot databases for this instance
            # (these implicitly exist since they were derived from the actual list of db names)
            for db_name in db_names:
                if db_name.startswith(f"iot_{inst_id}_"):
                    db_statuses.append(
                        dict(
                            name =  db_name,
                            exists = True
                        )
                    )

            if module.check_mode:
                for db_status in db_statuses:
                    # In check mode, we'll assume if the database exists then the drop will work
                    db_status['dropped'] = db_status['exists']
            else:
                for db_status in db_statuses:
                    if db_status['exists']:
                        try:
                            mongo_client.drop_database(db_status['name'])
                            db_status['dropped'] = True
                        except Exception as ex:
                            db_status['dropped'] = True
                            db_status['error'] = f"Failed to drop database: {str(ex)}"
                    else:
                        db_status['dropped'] = False


            # report failure iff at least one database failed to drop
            failed = False
            for db_status in db_statuses:
                if db_status.get('error') is not None:
                    failed = True
                    break


            if failed:
                module.fail_json(
                    msg = f"Failed to drop at least one database. See db_statuses for details.",
                    mongo_uri=mongo_uri,
                    db_statuses=db_statuses,
                )
            else:
                # changed is true iff at least one database was dropped
                changed = False
                for db_status in db_statuses:
                    if db_status['dropped']:
                        changed = True
                        break

                module.exit_json(
                    changed = changed,
                    mongo_uri=mongo_uri,
                    db_statuses=db_statuses,
                )
        
        except Exception as ex:
            module.fail_json(msg = f"Unexpected error: {str(ex)}")
    finally:
        if mongo_client is not None:
            mongo_client.close()

        if ca_file is not None:
            os.remove( ca_file.name )
    '''

if __name__ == '__main__':
    main()
