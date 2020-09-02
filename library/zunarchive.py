#!/usr/bin/python
# unarchive a z/OS archive (tar, tar,Z, pax, pax.Z, gzip)

from ansible.module_utils.basic import *

# simplified, flat version of the actual code
if __name__ == '__main__':
    global module
    module = AnsibleModule(
      argument_spec={
          'dest': { 'required': True, 'type': 'str' },
          'dest_tmp': { 'required': False, 'type': 'str' },
          'src': { 'required': True, 'type': 'str' },
      },
      supports_check_mode=False
    )

    
    module.exit_json(changed=True)
