#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Exact Critical Coulomb Wedge - Graphical User Interface.
::

    ┏━━by━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓██▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃░░░░░░░░░░░░░░░░░░░░██▓▓▓▓▓▓▓▓▓▓████████░░░░░░░░░░░░░░░░░░┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃░░░░░░░░░░░░░░░░░░██▒▒▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██░░░░░░░░░░░░░░░░┃
    ┃░░░░░░░░░░░░░░░░░░██▒▒▓▓▓▓░░      ▓▓▓▓  ██░░░░░░░░░░░░░░░░┃
    ┃                  ██▒▒▓▓░░    ████░░██  ██                ┃
    ┃                    ██▓▓░░    ████░░██  ██                ┃
    ┃                  ████▓▓░░░░      ░░  ░░██                ┃
    ┃              ████▒▒▒▒██▓▓░░████████░░██████              ┃
    ┃            ██▓▓▒▒▒▒▒▒▒▒██░░░░░░░░░░██▒▒▒▒▓▓██            ┃ 
    ┃            ██▓▓▓▓▒▒▒▒▒▒▒▒██████████▒▒▒▒▓▓▓▓██            ┃
    ┃          ██▓▓▓▓▓▓▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▓▓▓▓▓▓██          ┃
    ┃          ██▓▓▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████▓▓▓▓██          ┃
    ┃          ██▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓██          ┃
    ┃░░░░░░░░░░██▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██░░░░░░░░░░┃
    ┃░░░░░░░░░░░░██████░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░██████░░░░░░░░░░░░┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃░░░░░░░░░░░░░░░░██▓▓▓▓▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▓▓██░░░░░░░░░░░░░░░░┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▒▒██▒▒██▒▒▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓████▒▒▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒██████████████████▒▒▒▒▒▒██████████████████▒▒▒▒▒▒▒▒┃
    ┃▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━bclmary━━┛

"""

import pkg_resources
import os
from setuptools.config import read_configuration


def _extract_metadata(metadata_name):
    """Get metadata from pip installation."""
    return getattr(pkg_resources.get_distribution("eccw_gui"), metadata_name)

try:
    __version__ = _extract_metadata("version")
except pkg_resources.DistributionNotFound:
    _conf = read_configuration(os.path.join(
        os.path.dirname(os.path.dirname(__file__)), 'setup.cfg')
        )
    __version__ = _conf['metadata']["version"]

try:
    __location__ = _extract_metadata("location")
except pkg_resources.DistributionNotFound:
    for path in os.environ['PYTHONPATH'].split(os.pathsep):
        if path.endswith('eccw_gui/') or path.endswith('eccw_gui'):
            __location__ = path

__authors__ = [
    'BCL Mary',
    'Xiaoping Yuan',
    'YM Leroy',
    'Pauline Souloumiac',
    'Chong Wu',
    ]

__license__ = "GNU GPL-v3"

__url__ = "https://github.com/bclmary"

__contact__ = "bclmary@mailoo.org"

