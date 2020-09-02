deploy-rocket
=========

This role can be used to deploy select Rocket ported Open Source tools to a z/OS system.

Requirements
------------

* The rocket installation zip/tar files will need to be obtained and placed in the _pkg\_path_ directory.
* SFTP must be available on Ansible controller and z/OS target system.

Role Variables
--------------

| Variable            | Definition                                                                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| rocket_zip_dir      | The directory on the z/OS target system to place the python zip file                                                                          |
| rocket_file_name    | The name (without extension) of the python zip file to upload                                                                                 |
| rocket_space        | The amount of space (in KB) required for the rocket extracted file system                                                                       |

Dependencies
------------

None

Example Playbook
----------------

```yaml
  tasks:
    - include_role:
        name: deploy-rocket
```
