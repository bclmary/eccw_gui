#!/usr/bin/env python3
# -*-coding:utf-8 -*

"""
Tools and objects dedicated to manage inputs/outputs files.
"""

from collections import OrderedDict
import xmltodict
from xml.parsers.expat import ExpatError
import webbrowser
import sys
import pkg_resources
from pprint import pprint

#from eccw_gui.shared.tools import graph_print
from eccw_gui.documentation import documentation_path


class EccwFile():
    """Read/Write an eccw session file.

    **Usage**

    >>> f = EccwFile("path/to/file.eccw")
    >>> f.show()
    >>> f.save("path/to/newfile.eccw")
    """
    mime = "eccw"

    def __init__(self, data=None, filename=None):
        self.values = data
        if filename is not None:
            self.load(filename)

    def _check_in(self, elt, key):
        if elt[key] == [None]:
            # No elts must be stored as an empty list entry.
            elt[key] = []

    def _check_out(self, elt, key):
        if elt[key] == []:
            # Empty list has to be enlighted to be stored as xml.
            elt[key] = [None]

    def load(self, filename):
        # Keywords that must be present in the result even if empty.
        fl = ('refpoints', 'points', 'curves')
        xmlfile = open(filename, 'r')
        try:
            tmp = xmltodict.parse(xmlfile.read(), force_list=fl)
        except ExpatError:
            self.values = None
            return
        xmlfile.close()
        try:
            self.values = tmp["session"]
            # Replace wrong formated elements by proper values.
            if self.values["calculator"]['results'] is None:
                self.values["calculator"]['results'] = ''
            self._check_in(self.values["plot"], "refpoints")
            self._check_in(self.values["plot"], "curves")
            for i in range(len(self.values["plot"]["curves"])):
                self._check_in(self.values["plot"]["curves"][i], "points")
        except KeyError:
            self.values = None
            return

    def save(self, filename):
        xmlfile = open(filename, 'w')
        xmlfile.write(self.xml())
        xmlfile.close()

    def show(self):
        pprint(self.values)
        #graph_print(self.values)

    def xml(self, pretty=True):
        values = OrderedDict(self.values)
        # Replace empty list elements by [None] for xmltodict.
        self._check_out(self.values["plot"], "refpoints")
        self._check_out(self.values["plot"], "curves")
        for i in range(len(self.values["plot"]["curves"])):
            self._check_out(self.values["plot"]["curves"][i], "points")

        return xmltodict.unparse({"session": values}, pretty=pretty)

def open_documentation():
    webbrowser.open(documentation_path, new=0, autoraise=True)

if __name__ == "__main__":

    f = EccwFile()
    f.load("../../tests/data/test.eccw")
    f.show()
