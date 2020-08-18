# core
Core config to get an ADCD system 'up and running' (work in progress)

This repository provides Ansible code to:
- upload IBM python (initial prototype done)
- upload bash
- upload git
- upload curl
- upload IBM ZOAU

Group Variables
---------------

| Variable            | Definition                                                                                                                                                                              |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pkg_path            | The directory on the localhost that various packages (pax, zip, tar) reside 

Appreciation
------------

My thanks to the members of the IBM Ansible team, especially Blake Becker who answered numerous questions and Bryant Panyarachun, Asif Mahmud, and Omar Elbarmawi for their base code samples I was able to leverage to bootstrap myself.
