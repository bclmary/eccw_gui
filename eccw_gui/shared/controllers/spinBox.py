#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

from eccw_gui.shared.viewers.spinBox import Ui_Form
from eccw_gui.shared.tools import float_check


class SpinBox(QtWidgets.QWidget, Ui_Form):
    """Spin box widget.

    Arguments:
    Awaits an integer or a real number that will initiate the state of the
    spin box.

    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(SpinBox, self).__init__()
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()

    def get_params(self):
        return self.doubleSpinBox.value()

    def set_params(self, value):
        errmessage = (
            self.__class__.__name__
            + "() gets invalid size format '"
            + str(value)
            + "'."
        )
        try:
            value = float_check(value, default=None)
            if value < 0:
                raise TypeError(errmessage)
            self.doubleSpinBox.setValue(value)
        except TypeError:
            raise TypeError(errmessage)

    def get_select(self):
        return self.get_params()


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = SpinBox("1.2")
        sys.exit(app.exec_())
    finally:
        print("params =", myapp.get_params())
        print("select =", myapp.get_select())
