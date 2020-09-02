deploy-profile
=========

This role can be used to deploy select Rocket ported Open Source tools to a z/OS system.

Requirements
------------

* SCP must be available on Ansible controller and z/OS target system.

Dependencies
------------

None

Example Playbook
----------------

```yaml
  tasks:
    - include_role:
        name: deploy-profile
```
