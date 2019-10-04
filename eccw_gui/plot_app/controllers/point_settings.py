#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from collections import OrderedDict

from eccw_gui.plot_app.viewers.point_settings import Ui_Form
from eccw_gui.shared.controllers.lineEdit import ScalarLineEdit
from eccw_gui.shared.controllers.lineEdit import StringLineEdit
from eccw_gui.shared.controllers.lineEdit import SwitchScalarBound
from eccw_gui.shared.controllers.spinBox import SpinBox
from eccw_gui.shared.controllers.colorButton import ColorButton
from eccw_gui.shared.controllers.comboBox import ComboBoxPoint
from eccw_gui.shared.controllers.label import Label
from eccw_gui.shared.controllers.checkBox import CheckBox
from eccw_gui.shared.wrappers import WrapperDict
from eccw_gui.shared.tools import graph_print


class PointSettings(QtWidgets.QWidget, Ui_Form, WrapperDict):
    """Abstract class."""

    def __init__(self, **kwargs):
        super(PointSettings, self).__init__()
        self.setupUi(self)
        # Init local attributs.
        self.closed = False
        # Init additional objects
        self.labelSize = Label("size")
        self.size = SpinBox(5)
        self.color = ColorButton()
        self.style = ComboBoxPoint()
        self.labelLabel = Label("label")
        self.label = StringLineEdit()
        # Put them in self
        self.horizontalLayout_settings.addWidget(self.labelSize)
        self.horizontalLayout_settings.addWidget(self.size)
        self.horizontalLayout_settings.addWidget(self.color)
        self.horizontalLayout_settings.addWidget(self.style)
        self.horizontalLayout_settings.addWidget(self.labelLabel)
        self.horizontalLayout_settings.addWidget(self.label)
        # Define events
        self.pushButton_kill.clicked.connect(self._setClosed)
        # Dictionnary
        self.dict = OrderedDict(
            [
                ("size", self.size),
                ("color", self.color),
                ("style", self.style),
                ("label", self.label),
            ]
        )

    def _setClosed(self):
        self.closed = True


class RefPointSettings(PointSettings):
    """Widget for reference points parameters and settings entry.

    Keyword arguments:
    beta  -- awaits a dict of keyword arguments for a ScalarLineEdit element.
    alpha -- awaits a dict of keyword arguments for a ScalarLineEdit element.
    size  -- awaits a dict of keyword arguments for a SpinBox element.
    color -- awaits a dict of keyword arguments for a ColorBox element.
    style -- awaits a dict of keyword arguments for a ComboBoxPoint element.
    label -- awaits a dict of keyword arguments for a StringLineEdit element.

    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        PointSettings.__init__(self, **kwargs)
        self.beta = ScalarLineEdit()
        self.alpha = ScalarLineEdit()
        self.horizontalLayout_beta.addWidget(self.beta)
        self.horizontalLayout_alpha.addWidget(self.alpha)
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict(
            [("beta", self.beta), ("alpha", self.alpha)], **self.dict
        )
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        self.show()


class CurvePointSettings(PointSettings):
    """Widget for points on curve parameters and settings entry.

    Keyword arguments:
    beta  -- awaits a dict of keyword arguments for a SwitchScalarBound
             element.
    alpha -- awaits a dict of keyword arguments for a SwitchScalarBound
             element.
    size  -- awaits a dict of keyword arguments for a SpinBox element.
    color -- awaits a dict of keyword arguments for a ColorBox element.
    style -- awaits a dict of keyword arguments for a ComboBoxPoint element.
    label -- awaits a dict of keyword arguments for a StringLineEdit element.

    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        PointSettings.__init__(self, **kwargs)
        self.beta = SwitchScalarBound()
        self.alpha = SwitchScalarBound()
        self.sketch = CheckBox(label="sketch")
        self.horizontalLayout_beta.addWidget(self.beta)
        self.horizontalLayout_alpha.addWidget(self.alpha)
        self.horizontalLayout_settings.addWidget(self.sketch)
        # Set initial state
        self.beta.set_scalar_visible(True)
        self.alpha.set_bound_visible(True)
        # Define pushButton behaviours
        self.beta.pushButton.clicked.connect(
            lambda: self._there_must_be_one(self.beta, self.alpha)
        )
        self.alpha.pushButton.clicked.connect(
            lambda: self._there_must_be_one(self.alpha, self.beta)
        )
        # Dictionnary
        self.dict = OrderedDict(
            [("beta", self.beta), ("alpha", self.alpha)], **self.dict
        )
        self.dict.update([("sketch", self.sketch)])
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        self.show()

    def _there_must_be_one(self, elt, other):
        if elt.pushButton.isChecked():
            elt.set_bound_visible(True)
            other.set_scalar_visible(True)
        else:
            elt.set_scalar_visible(True)
            other.set_bound_visible(True)


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)

        params = {
            "beta": "0",
            "alpha": "3.12",
            "color": ("0", "1", "0", "1"),
            "size": "5",
            "style": "*",
            "label": "poulpe",
        }
        myapp1 = RefPointSettings(**params)

        params = {
            "alpha": {
                "bound": {"min": "0", "max": "4"},
                "scalar": "2",
                "focus": "bound",
            },
            "beta": {
                "bound": {"min": "-1", "max": "1"},
                "scalar": "0",
                "focus": "scalar",
            },
            "sketch": "True",
            "color": ("0", "1", "0", "1"),
            "size": "5",
            "style": "s",
            "label": "poulpe",
        }
        myapp2 = CurvePointSettings(**params)

        sys.exit(app.exec_())
    finally:
        if myapp1:
            print("RefPointSettings")
            print("params =")
            graph_print(myapp1.get_params(), indent=2)
            print("select =")
            graph_print(myapp1.get_select(), indent=2)
        print()
        if myapp2:
            print("CurvePointSettings")
            print("params =")
            graph_print(myapp2.get_params(), indent=2)
            print("select =")
            graph_print(myapp2.get_select(), indent=2)
