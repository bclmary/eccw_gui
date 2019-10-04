#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets


from eccw_gui.shared.viewers.comboBox_line import Ui_Form as UiLine
from eccw_gui.shared.viewers.comboBox_point import Ui_Form as UiPoint
from eccw_gui.shared.viewers.comboBox_colorMap import Ui_Form as UiCmap


class ComboBox(object):
    """Abstract class."""

    parser = dict()

    def get_params(self):
        return self.comboBox.currentText()

    def set_params(self, value):
        i = self.comboBox.findText(str(value))
        if i >= 0:
            self.comboBox.setCurrentIndex(i)
        else:
            raise TypeError(
                self.__class__.__name__
                + "() gets unknown style argument '"
                + str(value)
                + "'."
            )

    def get_select(self):
        return self.parser[self.get_params()]


class ComboBoxLine(QtWidgets.QWidget, UiLine, ComboBox):
    """Combo box widget for line style settings.

    Arguments:
    Awaits a single string value among the following list:
    * continuous
    * dotted
    * dashed
    * dash dotted

    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(ComboBoxLine, self).__init__()
        self.parser = {
            "continuous": "-",
            "dotted": ":",
            "dashed": "--",
            "dash dotted": "-.",
        }
        self.setupUi(self)
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()


class ComboBoxPoint(QtWidgets.QWidget, UiPoint, ComboBox):
    """Combo box widget for point style settings.

    Arguments:
    Awaits a single string value among the following list:
    * circle   or c
    * square   or s
    * diamond  or d
    * triangle or t
    * star     or *
    * cross    or +
    * pentagon or p

    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(ComboBoxPoint, self).__init__()
        self.setupUi(self)
        # Fill values with args
        self.shortcuts_parser = {
            "c": "circle",
            "s": "square",
            "d": "diamond",
            "t": "triangle",
            "*": "star",
            "+": "cross",
            "p": "pentagon",
        }
        self.parser = {
            "circle": "o",
            "square": "s",
            "diamond": "D",
            "triangle": "^",
            "star": "*",
            "cross": "+",
            "pentagon": "p",
        }
        if args:
            self.set_params(*args)
        self.show()

    def set_params(self, value):
        value = self.shortcuts_parser.get(value, value)
        ComboBoxLine.set_params(self, value)


class ComboBoxColorMap(QtWidgets.QWidget, UiCmap, ComboBox):
    """Combo box widget for colormap settings.

    Arguments:
    Awaits a single string value among the following list
    (All are matplotlib colormaps):
    * Gray
    * Hot
    * Winter
    * Gnuplot
    * Gnuplot2
    * Magma
    * Inferno
    * Plasma
    * Viridis

    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(ComboBoxColorMap, self).__init__()
        self.setupUi(self)
        self.parser = {
            "Gray": "Greys",
            "Hot": "hot",
            "Winter": "winter",
            "Gnuplot": "gnuplot",
            "Gnuplot2": "gnuplot2",
            "Magma": "magma",
            "Inferno": "inferno",
            "Plasma": "plasma",
            "Viridis": "viridis",
        }
        # Fill values with args
        if args:
            self.set_params(*args)
        self.show()


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = ComboBoxColorMap("Inferno")
        #        myapp = ComboBoxPoint('*')
        #        myapp = ComboBoxLine("dashed")
        sys.exit(app.exec_())
    finally:
        print("params =", myapp.get_params())
        print("select =", myapp.get_select())
