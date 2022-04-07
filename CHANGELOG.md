History of changes
==================

Version 1.1.2
-------------

* Convert embedded documentation from pdf to epub. 
  Since early 2022, applications with embdded pdf are forbidden by 
  some Windows™ protections. 
* Replace obsolescent `pkg_resources` by `importlib` package for 
  metadata introspection.

Version 1.1.1
-------------

* all metadatas are now really centralised in setup.cfg
* eccw_gui module is now exectuable with python's option -m
* update and clean graphical ressources
* better pip packaging
  * sdist now really gets all sources
  * bdist gets desktop installation without root rights on linux
  * bdist gets scripts for manual post-installation on Windows
* automatize building of python code from Qt .ui and .qrc files
* automatize building of python distribution
* add CHANGELOG

Version 1.1.0
-------------

* asynchronize main app and plot window 
* reflow keyboard shortcuts
  * give numbers to parameters and associate them to shortcuts
    * 'FX' for selection of parameter to compute
    * 'Crtl+X' for edition of scalar version of parameter
    * 'Crtl+Alt+X' for edition of range version of parameter
  * give 'Crtl' shortcut to all buttons
  * give 'Alt' shortcut to all checkbox and aditional lineEdits
* reflow position of parameters in calculator an plot apps : 
  * context on left (which is now a groupBox of chekables)
  * friction in the middle
  * fluids on right
* better display of results in calculator app
* changes in code:
  * black formating, 
  * cleaning of useless code
  * renamings for clarity and better physical meaning




