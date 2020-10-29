# core
Core config to get an ADCD system 'up and running' (work in progress)

Group Variables
--------------

| Variable            | Definition                                                                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pkg_path            | the absolute path to the directory containing packages to upload, on the Ansible control system.                                                                                        |
| sftp_path           | the absolute path to the SFTP binary, on the Ansible control system.                                                                                                                    |
This repository provides Ansible code to:
- upload IBM python (initial prototype done)
- upload bash
- upload git
- upload curl
- upload IBM ZOAU

Sample Invocation
-------------

To update all systems with the latest software:
ansible-playbook -i inventories/zsystem.yml deploy-rocket.yml

Appreciation
------------

My thanks to the members of the IBM Ansible team, especially Blake Becker who answered numerous questions and Bryant Panyarachun, Asif Mahmud, and Omar Elbarmawi for their base code samples I was able to leverage to bootstrap myself.

