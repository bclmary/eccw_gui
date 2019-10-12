# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/plot_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon_eccw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PlotWindow.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(PlotWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_plot = QtWidgets.QVBoxLayout()
        self.verticalLayout_plot.setObjectName("verticalLayout_plot")
        self.verticalLayout.addLayout(self.verticalLayout_plot)
        self.verticalLayout_toolbox = QtWidgets.QVBoxLayout()
        self.verticalLayout_toolbox.setObjectName("verticalLayout_toolbox")
        self.verticalLayout.addLayout(self.verticalLayout_toolbox)

        self.retranslateUi(PlotWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "ECCW plot"))

import eccw_gui.images.ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotWindow = QtWidgets.QWidget()
    ui = Ui_PlotWindow()
    ui.setupUi(PlotWindow)
    PlotWindow.show()
    sys.exit(app.exec_())

