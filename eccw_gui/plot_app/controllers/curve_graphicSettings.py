#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from collections import OrderedDict

from eccw_gui.plot_app.viewers.curve_graphicSettings import Ui_Form
from eccw_gui.shared.controllers.label import Label
from eccw_gui.shared.controllers.spinBox import SpinBox
from eccw_gui.shared.controllers.colorButton import ColorButton
from eccw_gui.shared.controllers.layout import VerticalLayout
from eccw_gui.shared.controllers.comboBox import ComboBoxLine, ComboBoxColorMap
from eccw_gui.shared.wrappers import Wrapper, WrapperDict
from eccw_gui.shared.tools import graph_print


class CurveGraphicSettings(QtWidgets.QWidget, Ui_Form, WrapperDict):
    """Widget for curve settings entry.

    Keyword arguments:
    thickness -- awaits a dict of keyword arguments for a ScalarLineEdit
                 element.
    color     -- awaits a dict of keyword arguments for a ColorButton element.
    colormap  -- awaits a dict of keyword arguments for a ColorBoxColorMap
                 element.
    style     -- awaits a dict of keyword arguments for a ComboBoxLine element.

    note: color and colormap keyword arguments are exclusives.
    This is a Qt derived object.
    """

    def __init__(self, label=False, **kwargs):
        super(CurveGraphicSettings, self).__init__()
        self.setupUi(self)
        # Init additional objects
        if kwargs:
            colormap = kwargs.get("colormap", False)
            color = kwargs.get("color", False)
        else:
            color, colormap = False, False
        if color and colormap:
            raise TypeError(
                "CurveGraphicSettings() awaits 'color' OR"
                "'colomap' arguments, not both."
            )
        self.labelThick = Label("thickness")
        self.size = SpinBox()
        if colormap:
            self.color = ComboBoxColorMap()
        else:
            self.color = ColorButton()
        self.style = ComboBoxLine()
        # Put them in self
        self.horizontalLayout.addWidget(self.labelThick)
        self.horizontalLayout.addWidget(self.size)
        self.horizontalLayout.addWidget(self.color)
        self.horizontalLayout.addWidget(self.style)
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict(
            [
                ("thickness", self.size),
                ("colormap" if colormap else "color", self.color),
                ("style", self.style),
            ]
        )
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        if label:
            self.flagLabel = Label(label, bold=True)
            self.horizontalLayout.addWidget(self.flagLabel)
        self.show()


class CurveDoubleGraphicSettings(VerticalLayout, WrapperDict):
    """Widget for a two parts curve settings entry.

    Keyword arguments:
    normal  -- awaits a dict of keyword arguments for a CurveGraphicSettings
               element (with 'color' kwarg).
    inverse -- awaits a dict of keyword arguments for a CurveGraphicSettings
               element (with 'color' kwarg).

    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        VerticalLayout.__init__(self)
        self.normal = CurveGraphicSettings(label="normal", color=(0, 0, 1, 1))
        self.inverse = CurveGraphicSettings(label="inverse", color=(1, 0, 0, 1))
        self.verticalLayout.addWidget(self.normal)
        self.verticalLayout.addWidget(self.inverse)
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict([("normal", self.normal), ("inverse", self.inverse)])
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)


class SwitchCurveGraphicSettings(VerticalLayout, WrapperDict):
    """Switcher widget.

    Allows to switch between the following elements:
    * CurveGraphicSettings with 'color' element,
    * CurveGraphicSettings with 'colormap' element,
    * CurveDoubleGraphicSettings.

    Keyword arguments:
    focus   -- awaits a string among 'default', 'double', 'range'.
    default -- awaits a dict of keyword arguments for CurveGraphicSettings
               element with color element.
    double  -- awaits a dict of keyword arguments for
               CurveDoubleGraphicSettings element.
    range   -- awaits a dict of keyword arguments for CurveGraphicSettings
               element with colormap element.

    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        VerticalLayout.__init__(self)
        # Init additional objects
        self.focus = Wrapper()
        self.default = CurveGraphicSettings()
        self.range = CurveGraphicSettings(colormap="Gray")
        self.double = CurveDoubleGraphicSettings()
        # Put them in self
        self.verticalLayout.addWidget(self.default)
        self.verticalLayout.addWidget(self.double)
        self.verticalLayout.addWidget(self.range)
        # Initial state
        self.set_visible_manual("default")
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict(
            [
                ("focus", self.focus),
                ("default", self.default),
                ("double", self.double),
                ("range", self.range),
            ]
        )
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)

    def set_visible_manual(self, arg):
        self.default.setVisible(arg == "default")
        self.double.setVisible(arg == "double")
        self.range.setVisible(arg == "range")
        # self.setGeometry(10, 10, 300, 200)
        self.focus.set_params(arg)

    def set_params(self, **kwargs):
        WrapperDict.set_params(self, **kwargs)
        self.set_visible_manual(self.focus.value)

    def get_select(self):
        params = WrapperDict.get_select(self)
        ID = params["focus"]
        return OrderedDict([("type", ID), ("value", params[ID])])


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)

        p1 = {"thickness": 3.0, "style": "dashed", "color": (1, 0, 0, 1)}
        p2 = {"thickness": 3.0, "style": "dotted", "color": (1, 0, 1, 1)}
        # myapp = CurveGraphicSettings(**p1, label="poulpe")

        pr = {"thickness": 3.0, "style": "dashed", "colormap": "Inferno"}
        # myapp = CurveGraphicSettings(**pr)

        pd = {"normal": p1, "inverse": p2}
        # myapp = CurveDoubleGraphicSettings(**pd)

        params = {"default": p1, "range": pr, "double": pd, "focus": "double"}
        myapp = SwitchCurveGraphicSettings(**params)
        sys.exit(app.exec_())
    finally:
        print("params =")
        graph_print(myapp.get_params())
        print("select =")
        graph_print(myapp.get_select())
