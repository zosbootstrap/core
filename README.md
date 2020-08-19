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

My thanks to the members of the IBM Ansible team, especially Blake Becker and Bryant Panyarachun who answered numerous questions as well as Asif Mahmud, and Omar Elbarmawi for their base code samples I was able to leverage to bootstrap myself.
