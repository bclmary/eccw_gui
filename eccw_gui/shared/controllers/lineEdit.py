#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets
from collections import OrderedDict
from numpy import arange

from eccw_gui.shared.viewers.lineEdit import Ui_Form
from eccw_gui.shared.viewers.lineEdit_bound import Ui_Form as Ui_Form_bound
from eccw_gui.shared.viewers.lineEdit_range import Ui_Form as Ui_Form_range
from eccw_gui.shared.viewers.lineEdit_switch import Ui_Form as Ui_Form_switch
from eccw_gui.shared.tools import float_check, str_check, graph_print
from eccw_gui.shared.wrappers import Wrapper, WrapperDict


class LineEdit(QtWidgets.QWidget, Ui_Form):
    """Line edit widget.

    Arguments:
    Awaits a single argument.
    Any entry will initiate the line edit with a string interpretation
    of the argument.
    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(LineEdit, self).__init__()
        self.id = ""
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


class StringLineEdit(LineEdit):
    """Line edit widget for string entry.

    Arguments:
    Awaits a single string argument.
    Any entry will initiate the line edit with a string interpretation
    of the argument.
    This is a Qt derived object.
    """

    def __init__(self, *args):
        LineEdit.__init__(self, *args)
        self.id = "string"


class ScalarLineEdit(LineEdit):
    """Line edit widget for scalar number entry.

    Arguments:
    Awaits a single number argument.
    Any entry will initiate the line edit with a string interpretation
    of the argument.
    This is a Qt derived object.
    """

    def __init__(self, *args):
        LineEdit.__init__(self, *args)
        self.id = "scalar"

    def get_params(self):
        return float_check(self.lineEdit.text())


class BoundLineEdit(QtWidgets.QWidget, Ui_Form_bound, WrapperDict):
    """Line edit widget for number bounds entry.

    Keyword arguments:
    min -- minimal bounding value
    max -- maximal bounding value

    Any entry will initiate the line edit with a string interpretation
    of the arguments.
    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        super(BoundLineEdit, self).__init__()
        self.id = "bound"
        self.setupUi(self)
        self.min = Wrapper(
            action=lambda x: self.lineEdit_min.setText(str_check(x)),
            process=lambda x: None if x == "-inf" else x,
        )
        self.min.get_params = lambda: float_check(
            self.lineEdit_min.text(), default=-float("inf")
        )
        self.max = Wrapper(
            action=lambda x: self.lineEdit_max.setText(str_check(x)),
            process=lambda x: None if x == "inf" else x,
        )
        self.max.get_params = lambda: float_check(
            self.lineEdit_max.text(), default=float("inf")
        )
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict([("min", self.min), ("max", self.max)])
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        self.show()

    def clear(self):
        self.lineEdit_min.clear()
        self.lineEdit_max.clear()


class RangeLineEdit(QtWidgets.QWidget, Ui_Form_range, WrapperDict):
    """Line edit widget for number range entry.

    Keyword arguments:
    begin -- begin value of the range
    step -- step value of the range
    end -- ending value of the range

    Any entry will initiate the line edit with a string interpretation
    of the arguments.
    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        super(RangeLineEdit, self).__init__()
        self.id = "range"
        self.setupUi(self)
        self.begin = Wrapper(action=lambda x: self.lineEdit_begin.setText(str_check(x)))
        self.begin.get_params = lambda: float_check(self.lineEdit_begin.text())
        self.step = Wrapper(action=lambda x: self.lineEdit_step.setText(str_check(x)))
        self.step.get_params = lambda: float_check(self.lineEdit_step.text())
        self.end = Wrapper(action=lambda x: self.lineEdit_end.setText(str_check(x)))
        self.end.get_params = lambda: float_check(self.lineEdit_end.text())
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict(
            [("begin", self.begin), ("step", self.step), ("end", self.end)]
        )
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        self.show()

    def get_select(self):
        b, s, e = self.get_params().values()
        s = 1 if s is None else s
        try:
            e = e + s if (e - b) % s == 0 else e
            return arange(b, e, s)
        except TypeError:
            return None

    def clear(self):
        self.lineEdit_begin.clear()
        self.lineEdit_step.clear()
        self.lineEdit_end.clear()


class SwitchLineEdit(QtWidgets.QWidget, Ui_Form_switch, WrapperDict):
    """Abstract class."""

    def __init__(self, multiLineEdit, **kwargs):
        super(SwitchLineEdit, self).__init__()
        self.setupUi(self)
        # Init lineEdit objects
        self.scalar = ScalarLineEdit()
        self.multi = multiLineEdit()
        self.focus = Wrapper(self.scalar.id)
        self.id = Wrapper(None)
        # Put them in self
        self.verticalLayout.addWidget(self.scalar)
        self.verticalLayout.addWidget(self.multi)
        # Set initial state
        self._auto_set_visible()
        # Define pushButton behaviour
        self.pushButton.clicked.connect(self._auto_set_visible)
        # Dictionnary
        self.dict = OrderedDict(
            [
                (self.scalar.id, self.scalar),
                (self.multi.id, self.multi),
                ("focus", self.focus),
                ("id", self.id),
            ]
        )
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        self.show()

    def _auto_set_visible(self):
        if self.pushButton.isChecked():
            self.scalar.setVisible(False)
            self.multi.setVisible(True)
            self.focus.set_params(self.multi.id)
        else:
            self.multi.setVisible(False)
            self.scalar.setVisible(True)
            self.focus.set_params(self.scalar.id)

    def set_scalar_visible(self, value=True):
        self.pushButton.setChecked(not value)
        self._auto_set_visible()

    def set_focus_on_scalar(self):
        self.set_scalar_visible(True)
        self.scalar.lineEdit.setFocus()

    def set_params(self, **kwargs):
        # self.id = kwargs.get('id', '')
        WrapperDict.set_params(self, **kwargs)
        if self.focus.value == self.scalar.id:
            self.pushButton.setChecked(False)
        else:
            self.pushButton.setChecked(True)
        self._auto_set_visible()

    def get_select(self):
        params = WrapperDict.get_select(self)
        ID = params["focus"]
        return OrderedDict([("id", params["id"]), ("type", ID), ("value", params[ID])])

    def clear(self):
        self.scalar.clear()
        self.multi.clear()


class SwitchScalarBound(SwitchLineEdit):
    """Switcher widget.

    Allows to switch between ScalarLineEdit and BoundLineEdit widgets.

    Keyword arguments:
    scalar -- awaits a dict of keyword arguments for ScalarLineEdit element.
    bound  -- awaits a dict of keyword arguments for BoundLineEdit element.

    Any entry will initiate the line edit elements with a string interpretation
    of the arguments.
    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        SwitchLineEdit.__init__(self, BoundLineEdit, **kwargs)

    def set_bound_visible(self, value=True):
        self.pushButton.setChecked(value)
        self._auto_set_visible()

    def set_focus_on_bound(self):
        self.set_bound_visible(True)
        self.multi.lineEdit_min.setFocus()


class SwitchScalarRange(SwitchLineEdit):
    """Switcher widget.

    Allows to switch between ScalarLineEdit and RangeLineEdit widgets.

    Keyword arguments:
    scalar -- awaits a dict of keyword arguments for ScalarLineEdit element.
    range  -- awaits a dict of keyword arguments for RangeLineEdit element.

    Any entry will initiate the line edit elements with a string interpretation
    of the arguments.
    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        SwitchLineEdit.__init__(self, RangeLineEdit, **kwargs)

    def set_range_visible(self, value=True):
        self.pushButton.setChecked(value)
        self._auto_set_visible()

    def set_focus_on_range(self):
        self.set_range_visible(True)
        self.multi.lineEdit_begin.setFocus()


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)

        #        myapp = LineEdit(10)

        #        myapp = StringLineEdit("poulpe")

        #        params = {"min":-1, "max":1}
        #        myapp = BoundLineEdit(**params)

        #        params = {"begin": 1, "end": 8, "step": 2}
        #        myapp = RangeLineEdit(**params)

        #        params = {"bound": {"min": -1, "max": 1},
        #                  "scalar": 5, "focus": "bound"}
        #        params = {"bound": {"min": '-inf', "max": 'inf'},
        #                  "scalar": 5, "focus": "bound"}
        #        myapp = SwitchScalarBound(**params)

        params = {
            "range": {"begin": 1, "step": None, "end": 8},
            "scalar": 5,
            "focus": "range",
            "id": "my id",
        }
        myapp = SwitchScalarRange(**params)

        sys.exit(app.exec_())
    finally:
        print("params=")
        graph_print(myapp.get_params(), indent=2)
        print("select=")
        graph_print(myapp.get_select(), indent=2)
