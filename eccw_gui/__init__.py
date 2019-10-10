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

try:
    eccw_distrib = pkg_resources.get_distribution("eccw_gui")
    __location__ = eccw_distrib.location
    eccw_provider = eccw_distrib._provider
    eccw_metadata = eval(eccw_provider.get_metadata("metadata.json"))
    __version__ = eccw_metadata["version"]
    __license__ = eccw_metadata["license"]
    details = eccw_metadata["extensions"]["python.details"]
    __url__ = details["project_urls"]["Home"]
    for elt in details["contacts"]:
        if elt["role"] == "author":
            __authors__ = [name.strip() for name in elt["name"].split(",")]
        if elt["role"] == "maintainer":
            __contact__ = elt["email"]
except (pkg_resources.DistributionNotFound, FileNotFoundError):
    import os
    from setuptools.config import read_configuration

    metadata = read_configuration(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "setup.cfg")
    )["metadata"]
    __version__ = metadata["version"]
    __license__ = metadata["license"]
    __url__ = metadata["url"]
    __contact__ = metadata["maintainer_email"]
    __authors__ = [name.strip() for name in metadata["author"].split(",")]
    for path in os.environ["PYTHONPATH"].split(os.pathsep):
        if path.endswith("eccw_gui/") or path.endswith("eccw_gui"):
            __location__ = path
