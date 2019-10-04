# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/comboBox_colorMap.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(130, 30)
        Form.setMinimumSize(QtCore.QSize(130, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(130, 28))
        self.comboBox.setMaximumSize(QtCore.QSize(130, 28))
        self.comboBox.setBaseSize(QtCore.QSize(130, 28))
        self.comboBox.setIconSize(QtCore.QSize(35, 20))
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/colormaps/colormap_gray.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/colormaps/colormap_hot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/colormaps/colormap_winter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/colormaps/colormap_gnuplot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/colormaps/colormap_gnuplot2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon4, "")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/colormaps/colormap_magma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon5, "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/colormaps/colormap_inferno.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon6, "")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/colormaps/colormap_plasma.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon7, "")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/colormaps/colormap_viridis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon8, "")
        self.horizontalLayout.addWidget(self.comboBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setToolTip(_translate("Form", "Lines colormap"))
        self.comboBox.setItemText(0, _translate("Form", "Gray"))
        self.comboBox.setItemText(1, _translate("Form", "Hot"))
        self.comboBox.setItemText(2, _translate("Form", "Winter"))
        self.comboBox.setItemText(3, _translate("Form", "Gnuplot"))
        self.comboBox.setItemText(4, _translate("Form", "Gnuplot2"))
        self.comboBox.setItemText(5, _translate("Form", "Magma"))
        self.comboBox.setItemText(6, _translate("Form", "Inferno"))
        self.comboBox.setItemText(7, _translate("Form", "Plasma"))
        self.comboBox.setItemText(8, _translate("Form", "Viridis"))

import eccw_gui.images.ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

