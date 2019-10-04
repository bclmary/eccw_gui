#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets

from eccw_gui.shared.viewers.verticalLayout import Ui_Form as UiV
from eccw_gui.shared.viewers.horizontalLayout import Ui_Form as UiH


class VerticalLayout(QtWidgets.QWidget, UiV):
    """Vertical layout widget.
    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(VerticalLayout, self).__init__()
        self.setupUi(self)
        self.show()


class HorizontalLayout(QtWidgets.QWidget, UiH):
    """Horizontal layout widget.
    This is a Qt derived object.
    """

    def __init__(self, *args):
        super(HorizontalLayout, self).__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = VerticalLayout()
    sys.exit(app.exec_())
