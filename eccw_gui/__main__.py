#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
ECCW
allows to compute the exact solution of critical Coulomb wedge, draw it,
sketch it, with love. Are available compressive or extensive geological
context, with or without fluid pore pressure.

Created on Nov 6 10:58:41 2017
@author: bcl mary
"""

import sys
from PyQt5 import QtWidgets
import argparse


from eccw_gui.main_app.controllers.main import MainController
from eccw_gui.shared.file_management import EccwFile
from eccw_gui.shared.file_management import open_documentation
from eccw_gui import __version__, __authors__, __year__

description = f"""
ECCW - Exact Critical Coulomb Wedge, Version {__version__}

Copyright 2016-{__year__} {__authors__}
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.

ECCW is a Qt interface using python package 'eccw' to
compute and draw the exact solution of critical Coulomb wedge
(as Dahlen 1984 and Yuan et al. 2015)
"""


def options_parser():
    """Parse options given with the execute command line."""

    # Create a parser object.
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False,
        description=description,
    )

    # Optional arguments.
    optarg = parser.add_argument_group(
        title="-" * 30 + "\nOPTIONAL ARGUMENT", description=""
    )

    optarg.add_argument(
        "-h", "--help", action="help", help="show this help message and exit\n\n"
    )

    optarg.add_argument(
        "-V",
        "--version",
        action="version",
        version=__version__,
        help="show program's version number and exit\n\n",
    )

    optarg.add_argument(
        "-d",
        "--doc",
        dest="doc",
        action="store_true",
        help="show complete documentation and exit\n\n",
    )

    optarg.add_argument(
        "-f",
        "--file",
        dest="file",
        metavar=("FILE"),
        type=(str),
        help="re-start session saved in FILE (*.eccw)\n\n",
    )

    # Parse the command line from the shell.
    inputoptions = parser.parse_args()

    # Treat parsed commands.
    if inputoptions.doc is True:
        open_documentation()
        exit()

    return inputoptions.file


def launch():
    out = options_parser()
    app = QtWidgets.QApplication(sys.argv)
    params = dict()
    if out:
        eccwf = EccwFile(filename=out)
        params = eccwf.values
    myapp = MainController(**params)
    sys.exit(app.exec_())


if __name__ == "__main__":
    launch()
