deploy-python
=========

This role can be used to deploy IBM python to a z/OS system.

Requirements
------------

* The python installation pax file will need to be obtained and placed in the _files_ folder for this role.
* SFTP must be available on Ansible controller and z/OS target system.

Role Variables
--------------

| Variable            | Definition                                                                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| copy_dir            | The directory on the z/OS target system to place the compressed python install archive.                                                                                                 |
| gzip_path           | The path to gzip on z/OS target system                                                                                                                                                  |
| install_dir         | The directory on the z/OS target system to decompress and extract the compressed python install archive                                                                                 |
| python_file_name    | The name of the python pax file in the _pkg_path_ directory. Do not include the file extension. i                                                                                       |
| python_release_name | The base name for the archive stored in the _files_ folder of the role. (python)                                                                                                        |
| python_release_type | The release version of python ( i.e. py36 ). Most likely the end of python_file_name after the final hyphen                                                                             |
| sftp_path           | the absolute path to the SFTP binary on the Ansible control system.                                                                                                                     |

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
