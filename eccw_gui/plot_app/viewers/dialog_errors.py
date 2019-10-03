# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/dialog_errors.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_Errors(object):
    def setupUi(self, Dialog_Errors):
        Dialog_Errors.setObjectName("Dialog_Errors")
        Dialog_Errors.resize(400, 185)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_Errors)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Dialog_Errors)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog_Errors)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog_Errors)
        self.pushButton.clicked.connect(Dialog_Errors.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Errors)

    def retranslateUi(self, Dialog_Errors):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Errors.setWindowTitle(_translate("Dialog_Errors", "Errors"))
        self.pushButton.setText(_translate("Dialog_Errors", "Ok"))
        self.pushButton.setShortcut(_translate("Dialog_Errors", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Errors = QtWidgets.QDialog()
    ui = Ui_Dialog_Errors()
    ui.setupUi(Dialog_Errors)
    Dialog_Errors.show()
    sys.exit(app.exec_())

