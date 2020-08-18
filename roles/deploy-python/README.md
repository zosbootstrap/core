deploy-python
=========

This role can be used to deploy IBM python to a z/OS system.

Requirements
------------

* The python installation pax file will need to be obtained and placed in the _pkg\_path_ directory.
* SFTP must be available on Ansible controller and z/OS target system.

Role Variables
--------------

| Variable            | Definition                                                                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| python_pax_dir      | The directory on the z/OS target system to place the python pax file                                                                                                 |
| python_install_dir  | The directory on the z/OS target system to decompress and extract the python pax file                                                                                |
| python_install_fs   | The underlying file system on the z/OS target system that python will install into                                                                                   |
| python_file_name    | The name of the python pax file in the _pkg\_path_ directory. Do not include the file extension.                                                                     |
| python_space        | The amount of space (in KB) required for the python extracted file system                                                                                            |
| sftp_path           | the absolute path to the SFTP binary on the Ansible control system.                                                                                                  |

Dependencies
------------

None

Example Playbook
----------------

```yaml
  tasks:
    - include_role:
        name: deploy-python
```
