#!/usr/bin/python

from ansible.module_utils.basic import *

import pyaem2


def main():
    fields = {
        "host": {"default": True, "type": "str"},
        "port": {"default": True, "type": "str"},
        "group_name": {"default": True, "type": "str"},
        "package_name": {"default": True, "type": "str"},
        "package_version": {"default": True, "type": "str"},
        "aem_username": {"default": True, "type": "str"},
        "aem_password": {"default": True, "type": "str", "no_log": True}
    }

    module = AnsibleModule(argument_spec=fields)

    host = module.params['host']
    port = module.params['port']
    group_name = module.params['group_name']
    package_name = module.params['package_name']
    package_version = module.params['package_version']

    aem_username = module.params['aem_username']
    aem_password = module.params['aem_password']

    aem = pyaem2.PyAem2(aem_username, aem_password, host, port)
    result = aem.install_package_sync(group_name, package_name, package_version)

    module.exit_json(changed=True, meta=result.message)


if __name__ == '__main__':
    main()
