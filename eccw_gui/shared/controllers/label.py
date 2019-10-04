#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets

from eccw_gui.shared.viewers.label import Ui_Form


class Label(QtWidgets.QWidget, Ui_Form):
    """Label widget.

    Arguments:
    Awaits any string value.

    This is a Qt derived object.
    """

    def __init__(self, *args, **kwargs):
        super(Label, self).__init__()
        self.id = "scalar"
        self.setupUi(self)
        if kwargs.get("bold", False):
            self.setBold(kwargs["bold"])
        # Fill values with args
        if args:
            self.set_params(args[0])
        self.show()

    def setBold(self, arg):
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(arg)
        self.label.setFont(font)

    def get_params(self):
        return self.label.text()

    def set_params(self, value):
        self.label.setText(str(value))

    def get_select(self):
        return self.get_params()

    def clear(self):
        self.label.clear()


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = Label("poulpe", bold=True)
        sys.exit(app.exec_())
    finally:
        print("params =", myapp.get_params())
        print("select =", myapp.get_select())
