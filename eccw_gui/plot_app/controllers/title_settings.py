#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

from eccw_gui.plot_app.viewers.title_settings import Ui_Form
from eccw_gui.shared.tools import str_check, graph_print


class TitleEdit(QtWidgets.QWidget, Ui_Form):
    """Title edit widget.

    Arguments:
    Awaits a single argument.
    Any entry will initiate the line edit with a string interpretation
    of the argument.
    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(TitleEdit, self).__init__()
        self.id = "title"
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()

    def get_params(self):
        return self.lineEdit.text()

    def set_params(self, arg):
        self.lineEdit.setText(str_check(arg))

    def get_select(self):
        return self.get_params()

    def clear(self):
        self.lineEdit.clear()


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)

        myapp = TitleEdit("Random Title")
        sys.exit(app.exec_())
    finally:
        print("params=")
        graph_print(myapp.get_params(), indent=2)
        print("select=")
        graph_print(myapp.get_select(), indent=2)
