deploy-zoau
=========

This role can be used to deploy IBM Z Open Automation Utilities to a z/OS system.

Requirements
------------

* The zoau installation pax file will need to be obtained and placed in the _pkg\_path_ directory.
* SFTP must be available on Ansible controller and z/OS target system.

Role Variables
--------------

| Variable            | Definition                                                                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| zoau_pax_dir        | The directory on the z/OS target system to place the python pax file                                                                          |
| zoau_file_name      | The name (without extension) of the python pax file to upload                                                                                 |
| zoau_space          | The amount of space (in KB) required for the zoau extracted file system                                                                       |

Dependencies
------------

None

Example Playbook
----------------

```yaml
  tasks:
    - include_role:
        name: deploy-zoau
```
