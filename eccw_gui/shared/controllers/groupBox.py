#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

from eccw_gui.shared.viewers.groupBox_context import Ui_Form as UiContext


class GroupBoxContext(QtWidgets.QWidget, UiContext):
    """Check box widget for tectonic context settings.

    Arguments:
    Awaits a single string value among the following list
    * Compression
    * Extension

    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(GroupBoxContext, self).__init__()
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()

    def set_params(self, value):
        if value == "Compression":
            self.checkBox_compression.setChecked(True)
        if value == "Extension":
            self.checkBox_extension.setChecked(True)

    def get_params(self):
        if self.checkBox_compression.isChecked():
            return "Compression"
        if self.checkBox_extension.isChecked():
            return "Extension"

    def get_select(self):
        if self.checkBox_compression.isChecked():
            return "c"
        if self.checkBox_extension.isChecked():
            return "e"


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = GroupBoxContext("Extension")
        sys.exit(app.exec_())
    finally:
        print("params =", myapp.get_params())
        print("select =", myapp.get_select())
