#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets, QtGui

from eccw_gui.plot_app.viewers.plot_window import Ui_PlotWindow

from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


class PlotWindow(QtWidgets.QWidget, Ui_PlotWindow):
    """Widget for software informations display."""

    def __init__(self, figure=None):
        super(PlotWindow, self).__init__()
        self.setupUi(self)
        # self.setWindowTitle("ECCW plot")
        self.figure = figure
        self.axe = self.figure.gca()
        self.plotWidget = FigureCanvas(self.figure)
        self.plotWidget.updateGeometry()
        self.verticalLayout_plot.addWidget(self.plotWidget)
        self.toolbarwidget = NavigationToolbar2QT(self.plotWidget, self)
        self.verticalLayout_toolbox.addWidget(self.toolbarwidget)
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+W"), self, self.close)

    def update(self):
        self.plotWidget.draw()


if __name__ == "__main__":
    import sys
    import random
    from matplotlib.figure import Figure

    app = QtWidgets.QApplication(sys.argv)
    data = [random.random() for i in range(25)]
    figure = Figure(figsize=(5, 4), dpi=100)
    axe = figure.gca()
    axe.plot(data, "r-")
    axe.set_title("PyQt Matplotlib Example")
    myapp = PlotWindow(figure=figure)
    myapp.show()
    sys.exit(app.exec_())
