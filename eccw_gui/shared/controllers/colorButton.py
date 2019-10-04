#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtGui, QtWidgets

from eccw_gui.shared.viewers.toolButton import Ui_Form
from eccw_gui.shared.tools import float_check
from eccw_gui.shared.wrappers import Wrapper


class ColorButton(QtWidgets.QWidget, Ui_Form, Wrapper):
    """Color button widget.

    Arguments:
    Awaits a tuple of for reals with value in between 0 and 1 (rgba).

    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(ColorButton, self).__init__()
        self.setupUi(self)
        self.action = lambda x: self.change_color(x)
        self.process = lambda x: x
        self.style_sheet = (
            "color: white;"
            "background-color: %s;"
            "border-style: outset;"
            "border-width: 1;"
            "border-color: gray;"
            "border-radius: 4px;"
            "min-width: 26px;"
            "max-width: 26px;"
            "min-height: 26px;"
            "max-height: 26px;"
        )
        self.style_sheet_hover = "background-color: %s;"
        self.style_sheet_clicked = "border-style: inset;"
        self.setToolTip("Color")
        self.toolButton.clicked.connect(self.showDialog)
        # Fill values with args
        if not args:
            args = (0, 0, 0, 1)  # Default color is black
        self.set_params(args)
        self.show()

    def showDialog(self):
        col = QtWidgets.QColorDialog.getColor()
        if col.isValid():
            self.change_color(col)
            self.value = col.getRgbF()

    def lighter_color(self, col, pct=0.5):
        newcol = QtGui.QColor()
        rgba = tuple(
            i + (1 - i) * pct if i + (1 - i) * pct <= 1 else 1 for i in col.getRgbF()
        )
        newcol.setRgbF(*rgba)
        return newcol

    def change_color(self, color):
        """col is an QColor object"""
        if isinstance(color, tuple):
            col = QtGui.QColor()
            col.setRgbF(*color)
        else:
            col = color
        style = self.style_sheet % col.name()
        # QColor.lighter method doesn't do the way I want the following job:
        col_hover = self.lighter_color(col)
        style_hover = self.style_sheet_hover % col_hover.name()
        self.toolButton.setStyleSheet(
            "QWidget {" + style + "} "
            "QWidget:hover {" + style_hover + "}"
            "QWidget:pressed {" + self.style_sheet_clicked + "}"
        )

    def set_params(self, arg):
        errmessage = "ColorButton() gets invalid color format '" + str(arg) + "'."
        try:
            rgba = tuple(float_check(c) for c in arg)
            if all([c <= 1.0 for c in rgba]) and len(rgba) == 4:
                Wrapper.set_params(self, rgba)
            else:
                raise TypeError(errmessage)
        except TypeError:
            raise TypeError(errmessage)


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = ColorButton("0", "1", "0", "1")
        myapp.set_params(("0", "1", "0", "1"))
        sys.exit(app.exec_())
    finally:
        print("params =", myapp.get_params())
        print("select =", myapp.get_select())
