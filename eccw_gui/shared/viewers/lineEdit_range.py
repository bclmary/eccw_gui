# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/lineEdit_range.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(120, 28)
        Form.setMaximumSize(QtCore.QSize(120, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_begin = QtWidgets.QLineEdit(Form)
        self.lineEdit_begin.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_begin.sizePolicy().hasHeightForWidth())
        self.lineEdit_begin.setSizePolicy(sizePolicy)
        self.lineEdit_begin.setMinimumSize(QtCore.QSize(40, 28))
        self.lineEdit_begin.setMaximumSize(QtCore.QSize(40, 28))
        self.lineEdit_begin.setBaseSize(QtCore.QSize(40, 28))
        self.lineEdit_begin.setWhatsThis("")
        self.lineEdit_begin.setText("")
        self.lineEdit_begin.setObjectName("lineEdit_begin")
        self.horizontalLayout.addWidget(self.lineEdit_begin)
        self.lineEdit_step = QtWidgets.QLineEdit(Form)
        self.lineEdit_step.setMinimumSize(QtCore.QSize(40, 28))
        self.lineEdit_step.setMaximumSize(QtCore.QSize(40, 28))
        self.lineEdit_step.setBaseSize(QtCore.QSize(40, 28))
        self.lineEdit_step.setText("")
        self.lineEdit_step.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_step.setObjectName("lineEdit_step")
        self.horizontalLayout.addWidget(self.lineEdit_step)
        self.lineEdit_end = QtWidgets.QLineEdit(Form)
        self.lineEdit_end.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_end.sizePolicy().hasHeightForWidth())
        self.lineEdit_end.setSizePolicy(sizePolicy)
        self.lineEdit_end.setMinimumSize(QtCore.QSize(40, 28))
        self.lineEdit_end.setMaximumSize(QtCore.QSize(40, 28))
        self.lineEdit_end.setBaseSize(QtCore.QSize(40, 28))
        self.lineEdit_end.setText("")
        self.lineEdit_end.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_end.setObjectName("lineEdit_end")
        self.horizontalLayout.addWidget(self.lineEdit_end)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_begin.setToolTip(_translate("Form", "Interval begin"))
        self.lineEdit_step.setToolTip(_translate("Form", "Interval step"))
        self.lineEdit_end.setToolTip(_translate("Form", "Interval end"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

