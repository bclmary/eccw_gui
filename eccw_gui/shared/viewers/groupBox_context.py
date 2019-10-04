# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/groupBox_context.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(191, 105)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_compression = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_compression.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/button_compression.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_compression.setIcon(icon)
        self.checkBox_compression.setChecked(True)
        self.checkBox_compression.setAutoExclusive(True)
        self.checkBox_compression.setObjectName("checkBox_compression")
        self.verticalLayout_2.addWidget(self.checkBox_compression)
        self.checkBox_extension = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_extension.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons/button_extension.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_extension.setIcon(icon1)
        self.checkBox_extension.setAutoExclusive(True)
        self.checkBox_extension.setObjectName("checkBox_extension")
        self.verticalLayout_2.addWidget(self.checkBox_extension)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Tectonic context"))
        self.checkBox_compression.setToolTip(_translate("Form", "Activate compressive tectonic context (Alt+C)"))
        self.checkBox_compression.setText(_translate("Form", " &Compression"))
        self.checkBox_extension.setToolTip(_translate("Form", "Activate extensive tectonic context (Alt+E)"))
        self.checkBox_extension.setText(_translate("Form", " &Extension"))

import eccw_gui.images.ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

