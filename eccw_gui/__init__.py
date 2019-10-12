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

__year__ = 2019

try:
    # wheel distribution
    eccw_provider = pkg_resources.get_distribution("eccw_gui")._provider
    metadata = eval(eccw_provider.get_metadata("metadata.json"))
    __version__ = metadata["version"]
    __license__ = metadata["license"]
    details = metadata["extensions"]["python.details"]
    __url__ = details["project_urls"]["Home"]
    for elt in details["contacts"]:
        if elt["role"] == "author":
            __authors__ = [name.strip() for name in elt["name"].split(",")]
        if elt["role"] == "maintainer":
            __contact__ = elt["email"]
except (pkg_resources.DistributionNotFound, FileNotFoundError):
    # sources distribution
    import os
    from setuptools.config import read_configuration

    parent_path = os.path.dirname(os.path.dirname(__file__))
    metadata = read_configuration(
        os.path.join(parent_path, "setup.cfg")
    )["metadata"]
    __version__ = metadata["version"]
    __license__ = metadata["license"]
    __url__ = metadata["url"]
    __contact__ = metadata["maintainer_email"]
    __authors__ = [name.strip() for name in metadata["author"].split(",")]
except :
    # These infos are not mandatory.
    __version__ = ""
    __license__ = ""
    __url__ = ""
    __authors__ = ""
    __contact__ = ""
