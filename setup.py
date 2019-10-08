#!/usr/bin/env python3
# -*-coding:utf-8 -*

from setuptools import setup, find_packages
import sys
from distutils.command.install_data import install_data
import subprocess
import os.path as osp


def get_data_files():
    """Return data_files in a platform dependent manner"""
    if sys.platform.startswith('linux'):
        data_files = [('share/applications', ['scripts/eccw.desktop']),
                      ('share/pixmaps', [
                        'eccw_gui/images/icon_eccw.svg',
                        #'eccw_gui/images/icon_eccw_16x16.png',
                        #'eccw_gui/images/icon_eccw_24x24.png',
                        #'eccw_gui/images/icon_eccw_32x32.png',
                        #'eccw_gui/images/icon_eccw_48x48.png',
                        #'eccw_gui/images/icon_eccw_128x128.png',
                        #'eccw_gui/images/icon_eccw_256x256.png',
                        #'eccw_gui/images/icon_eccw_512x512.png'
                        ]),
                      ('share/metainfo', ['scripts/eccw.appdata.xml'])]
    else:
        data_files = []
    return data_files


# Make Linux detect ECCW desktop file
class MyInstallData(install_data):
    def run(self):
        install_data.run(self)
        if sys.platform.startswith('linux'):
            try:
                subprocess.call(['update-desktop-database'])
            except:
                print("ERROR: unable to update desktop database",
                      file=sys.stderr)
CMDCLASS = {'install_data': MyInstallData}


setup(
    entry_points={
        'console_scripts': [
            'eccw=eccw_gui.main:launch',
            ],
        },
    data_files=get_data_files(),
    scripts=[osp.join('scripts', 'eccw')],
    cmdclass=CMDCLASS,
    )

