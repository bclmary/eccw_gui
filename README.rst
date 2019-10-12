|ECCW-GUI|
##########

Exact Critical Coulomb Wedge - Graphical User Interface
=======================================================

**ECCW** and **ECCW-GUI** allow to compute the exact solution of any parameter of critical Coulomb wedge (as Dahlen 1984 and Yuan et al. 2015). They allow to draw any of these solutions in the β vs α domain (basal slope against surface slope). Are availables compressive or extensive geological context and fluid pore pressure.

**ECCW** and **ECCW-GUI** are under GNU GPL-v3 license.


*******************************************************************

Overview
========


General informations
++++++++++++++++++++

* *ECCW* is a *python3* library;
* *ECCW-GUI* is a graphical user interface, written in *python3* and using *Qt*;
* In the GUI, you can save a session and keep it in an xml file (.eccw);
* A pdf documentation is available (see Usage section) including:
    * usage explainations;
    * theoretical explainations 
    * guidelines of the results interpretation;
    * blueprints of the equations implemantation.


Calculator App
++++++++++++++

* Compute the solution of the *Critical Coulomb Wedge* for compressive or extensive tectonic context, with or without fluids overpressure.
* The solution can be computed with one of the four main parameters set as unknown.
* A range of solutions can be computed at once if you set one of the known parameters as a range.

|Screen copy of calculator-app|


Plot App
++++++++

* Plot the solution of the *Critical Coulomb Wedge* in matplotlib windows (includes zooms, exports, and more).
* A range of solutions can be ploted at once if you set one of the known parameters as a range.
* You can explore graphically points on the solution curve, with optional display of a sketch representing orientations and directions of faults.
* Refrences points can be manually added or imported from .csv files.

|Screen copy of plot-app|

|Screen copy of plot-app's plot window|


*******************************************************************

Installation
============


Windows
+++++++

.. note :: Only tested on *Windows 7*.


* Install a **python3** distribution.
  The **miniconda** distribution from https://conda.io/miniconda.html is a good choice.

  *  Download the proper installer (the 64-bit version should be appropriated).

  *  Run the downloaded ``.exe``;

* Intall *ECCW*.

  * Open a shell that can access your python3 distribution, such as the *Windows Power Shell*.
    If you choosed to install **miniconda**, you should use the *Anaconda Prompt*.
    You can access it by typing ``anaconda`` in the main Windows menu.

  * In the shell, type the following command::

      pip install eccw-gui

* ECCW is then available from the main Windows menu by taping ``eccw`` or from a shell by taping ``python -m eccw_gui``.

* Optionally, you can run the ``eccw_windows_install`` command in a shell to install menu and desktop shortcuts. 
  To remove these shortcuts, run the ``eccw_windows_remove`` command.


Linux
+++++

.. note :: Only tested on *Ubuntu 18.04*.

* Install **python3** with **pip** and **tk**. 
  On *Debian* family distributions, you can install these packages using the following command::

      $ sudo apt-get install python3 python3-pip python3-tk

2. Install *ECCW* with the following command::

      $ pip3 install eccw-gui

3. *ECCW* is then available from the main menu under the name **eccw**.


*******************************************************************

Usage
=====


GUI usage
+++++++++

Simply type ``eccw`` in a shell to launch *eccw*.
The GUI should also be available from the main menu.

To obtain help with text based mode, type::

    $ eccw -h

You can access an off-line documentation using the button 'Documentation' in the GUI.
Alternatively, you can use the following command, without the GUI::

    $ eccw -d

You can launch the GUI with the ``-m`` option of python using the canonic syntax::
 
    python -m eccw_gui

Python library usage
++++++++++++++++++++

You can import and use the core objects for computing and plotting *Critical Coulomb Wedge* from a python session as discribed in what follows.

EccwCompute
-----------

This the core object that compute the solutions of the *CCW* problem.
::

    >>> from eccw import EccwCompute
    >>> foo = EccwCompute(phiB=30, phiD=10, beta=0)
    >>> foo.show_params()
    { context       : 'Compression'
      beta          : 0.0
      alpha         : nan
      phiB          : 30.0
      phiD          : 10.0
      rho_f         : 0.0
      rho_sr        : 0.0
      delta_lambdaB : 0.0
      delta_lambdaD : 0.0
    }
    >>> foo.compute("alpha")
    ((3.4365319302835018,), (23.946319406533199,))
    

The result obtained with the ``compute`` method is always a tuple of two tuples.
The first tuple contains results in **inverse** fault mechanism, while the second tuple contains results in **normal** fault mechanism.
These tuples can each contain 0, 1 or 2 values, with a total always equal to 0 or 2.
Here some more examples with computation of beta ``parameter``::
::

    >>> foo.alpha = 3.436532
    >>> foo.compute("beta") 
    ((-1.0516746372768912e-07,), (69.6779628783264,))
    >>> foo.alpha = 20
    >>> foo.compute("beta") 
    ((), (-3.580929608343892, 43.25889259183777))
    >>> foo.alpha = -20
    >>> foo.compute("beta") 
    ((36.74110740816224, 83.58092960834391), ())
    >>> foo.alpha = -35
    >>> foo.compute("beta") 
    ((), ())

Have a look on the plot obtained in next section to understand these results.

EccwPlot
--------

This the core object that plot the solutions of the *CCW* problem. This object inherits from ``EccwCompute``.
::

    >>> from eccw import EccwPlot
    >>> foo = EccwPlot(phiB=30, phiD=10)
    >>> foo.add_curve(inverse={'color':(1,0,0,1), 'label':'inverse'}, 
                      normal={'color':(0,0,1,1), 'label':'normal'})
    >>> foo.add_point(alpha=3.436532)
    >>> foo.add_point(alpha=20, style='*', size=10)
    >>> foo.add_point(alpha=-20, style='s')
    >>> foo.add_legend()
    >>> foo.show()

|Screen copy of EccwPlot's plot|


*******************************************************************

Contributing
============

Additional dependancies
+++++++++++++++++++++++

Some softwares are needed to convert Qt specific files into python code:

* ``pyuic5`` is used to convert form ``.ui`` files into python code calling PyQt;
* ``pyrcc5`` is used to convert Qt ressources files ``.qrc`` into python module.

Both are found in following dependancies (ubuntu / debian):

    | pyqt5-dev-tools

If you want to install Qt-designer for Qt5 on Ubuntu/debian, this app is included in the following package:

    | qttools5-dev-tools

Informations for developpers
++++++++++++++++++++++++++++

* Convert ``.ui`` files created using *Qt-Designer* into python files::

    $ pyuic5 -x xxx.ui -o xxx_Viewer.py

  Some bash scripts located in ``eccw_gui/*/viewers`` folders named ``make_viewers.sh`` automatise this process.
  Some custom corrections of *Qt* objects dimensions are also embedded in some of these script.

* Convert *Qt* ressources ``.qrc`` files created using *Qt-Designer* into python files::

    $ pyrcc5 xxx.qrc -o xxx_rc.py

  These ressources files are a smart way to embed images into source code and solve the access path to these images problem after desktop installation.

* All graphical object (Qt-derived) get the following methods:

  getParams:
    return an OrderedDict that describe the state of the object.
  setParams:   
    set the object with a dict obtained from getParams.
  
  getSelect:
    return an OrderedDict that describe the selected parameters to treat (equal to getParams if the paramters gets single state).








.. _eccw: https://github.com/bclmary/eccw.git

.. _eccw-gui: https://github.com/bclmary/eccw_gui.git


.. |ECCW-GUI| image:: ./eccw_gui/images/eccw-gui_title.png
    :alt: ECCW
    :height: 200

.. |Screen copy of calculator-app| image:: eccw_gui/images/screen-copy_calculator-app.png
    :alt: screen copy of calculator app
    :width: 600

.. |Screen copy of plot-app| image:: eccw_gui/images/screen-copy_plot-app.png
    :alt: screen copy of plot app
    :width: 600

.. |Screen copy of plot-app's plot window| image:: eccw_gui/images/screen-copy_plot-app_plot.png
    :alt: screen copy of plot window of plot app
    :width: 600

.. |Screen copy of EccwPlot's plot| image:: eccw_gui/images/EccwPlot_example.png
    :alt: screen copy of matplotlib window containing ECCW plot
    :width: 600
