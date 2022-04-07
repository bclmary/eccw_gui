#!/usr/bin/env python3
# -*-coding:utf-8 -*

from setuptools import setup 
import sys
from distutils.command.install_data import install_data

import subprocess
import os

def get_data_files():
    """Return data_files in a platform dependent manner"""
    if sys.platform.startswith("linux"):
        data_files = [
            ("share/applications", ["scripts/eccw.desktop"]),
            ("share/pixmaps", ["eccw_gui/images/icon_eccw.png"]),
            ("share/icons", ["eccw_gui/images/icon_eccw.svg"]),
            ("share/metainfo", ["scripts/eccw.appdata.xml"]),
        ]
    else:
        data_files = []
    return data_files

# Make Linux detect ECCW desktop file
class MyInstallData(install_data):
    def run(self):
        install_data.run(self)
        if sys.platform.startswith("linux"):
            try:
                subprocess.call(["update-desktop-database"])
            except:
                print("ERROR: unable to update desktop database", file=sys.stderr)

CMDCLASS = {"install_data": MyInstallData}

#SCRIPTS = ["eccw", "eccw_win_post_install.py"]

setup(
    entry_points={
        "gui_scripts": ["eccw=eccw_gui.__main__:launch"],
        "console_scripts": [
            "eccw_windows_install=eccw_gui.windows.win_post_install:install",
            "eccw_windows_remove=eccw_gui.windows.win_post_install:remove",
        ]
    },
#    scripts=[os.path.join('scripts', fname) for fname in SCRIPTS],
    data_files=get_data_files(),
    package_data={"eccw_gui": [
        "documentation/ECCW.epub",
        "windows/eccw.ico",
    ],},
    cmdclass=CMDCLASS,
)
