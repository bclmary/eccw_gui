#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

from eccw_gui.shared.viewers.checkBox import Ui_Form


class CheckBox(QtWidgets.QWidget, Ui_Form):
    """Radio button widget.

    Arguments:
    Awaits a single boolean that will init the radio button state.

    Keyword arguments:
    label -- string to be displayed near by the radio button.

    This is a Qt derived object.
    """

    def __init__(self, *args, **kwargs):
        super(CheckBox, self).__init__()
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        if kwargs:
            self._set_label(**kwargs)
        self.show()

    def _set_label(self, **kwargs):
        label = kwargs.get("label", False)
        if label:
            self.checkBox.setText(label)

    def get_params(self):
        return self.checkBox.isChecked()

    def set_params(self, value):
        if isinstance(value, str):
            value = eval(value)
        self.checkBox.setChecked(value)

    def get_select(self):
        return self.get_params()


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = CheckBoxContext("Extension")
        sys.exit(app.exec_())
    finally:
        print("params =", myapp.get_params())
        print("select =", myapp.get_select())
