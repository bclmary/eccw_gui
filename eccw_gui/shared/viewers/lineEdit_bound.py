# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/lineEdit_bound.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(120, 28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QtCore.QSize(200, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_min = QtWidgets.QLineEdit(Form)
        self.lineEdit_min.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_min.sizePolicy().hasHeightForWidth())
        self.lineEdit_min.setSizePolicy(sizePolicy)
        self.lineEdit_min.setMinimumSize(QtCore.QSize(40, 28))
        self.lineEdit_min.setMaximumSize(QtCore.QSize(40, 28))
        self.lineEdit_min.setBaseSize(QtCore.QSize(40, 28))
        self.lineEdit_min.setText("")
        self.lineEdit_min.setObjectName("lineEdit_min")
        self.horizontalLayout.addWidget(self.lineEdit_min)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setMinimumSize(QtCore.QSize(10, 28))
        self.label_1.setMaximumSize(QtCore.QSize(10, 28))
        self.label_1.setBaseSize(QtCore.QSize(10, 28))
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(20, 28))
        self.lineEdit.setMaximumSize(QtCore.QSize(20, 28))
        self.lineEdit.setBaseSize(QtCore.QSize(20, 28))
        self.lineEdit.setToolTip("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(10, 28))
        self.label_2.setMaximumSize(QtCore.QSize(10, 28))
        self.label_2.setBaseSize(QtCore.QSize(10, 28))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_max = QtWidgets.QLineEdit(Form)
        self.lineEdit_max.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_max.sizePolicy().hasHeightForWidth())
        self.lineEdit_max.setSizePolicy(sizePolicy)
        self.lineEdit_max.setMinimumSize(QtCore.QSize(40, 28))
        self.lineEdit_max.setMaximumSize(QtCore.QSize(40, 28))
        self.lineEdit_max.setBaseSize(QtCore.QSize(40, 28))
        self.lineEdit_max.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_max.setText("")
        self.lineEdit_max.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_max.setObjectName("lineEdit_max")
        self.horizontalLayout.addWidget(self.lineEdit_max)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit_min.setToolTip(_translate("Form", "Minimal value"))
        self.label_1.setText(_translate("Form", "<"))
        self.label_2.setText(_translate("Form", "<"))
        self.lineEdit_max.setToolTip(_translate("Form", "Maximal value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

