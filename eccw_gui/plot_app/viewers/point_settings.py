# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/point_settings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(465, 28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_beta = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_beta.sizePolicy().hasHeightForWidth())
        self.label_beta.setSizePolicy(sizePolicy)
        self.label_beta.setMaximumSize(QtCore.QSize(12, 24))
        self.label_beta.setText("")
        self.label_beta.setPixmap(QtGui.QPixmap(":/params/params_beta.png"))
        self.label_beta.setScaledContents(True)
        self.label_beta.setObjectName("label_beta")
        self.horizontalLayout.addWidget(self.label_beta)
        self.horizontalLayout_beta = QtWidgets.QHBoxLayout()
        self.horizontalLayout_beta.setObjectName("horizontalLayout_beta")
        self.horizontalLayout.addLayout(self.horizontalLayout_beta)
        self.label_alpha = QtWidgets.QLabel(Form)
        self.label_alpha.setMaximumSize(QtCore.QSize(12, 24))
        self.label_alpha.setText("")
        self.label_alpha.setPixmap(QtGui.QPixmap(":/params/params_alpha.png"))
        self.label_alpha.setScaledContents(True)
        self.label_alpha.setObjectName("label_alpha")
        self.horizontalLayout.addWidget(self.label_alpha)
        self.horizontalLayout_alpha = QtWidgets.QHBoxLayout()
        self.horizontalLayout_alpha.setObjectName("horizontalLayout_alpha")
        self.horizontalLayout.addLayout(self.horizontalLayout_alpha)
        self.horizontalLayout_settings = QtWidgets.QHBoxLayout()
        self.horizontalLayout_settings.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_settings.setObjectName("horizontalLayout_settings")
        self.horizontalLayout.addLayout(self.horizontalLayout_settings)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_kill = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_kill.sizePolicy().hasHeightForWidth())
        self.pushButton_kill.setSizePolicy(sizePolicy)
        self.pushButton_kill.setMinimumSize(QtCore.QSize(28, 28))
        self.pushButton_kill.setMaximumSize(QtCore.QSize(28, 28))
        self.pushButton_kill.setBaseSize(QtCore.QSize(28, 28))
        self.pushButton_kill.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/button_close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_kill.setIcon(icon)
        self.pushButton_kill.setObjectName("pushButton_kill")
        self.horizontalLayout.addWidget(self.pushButton_kill)

        self.retranslateUi(Form)
        self.pushButton_kill.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_beta.setToolTip(_translate("Form", "Basal slope [deg]"))
        self.label_alpha.setToolTip(_translate("Form", "Surface slope [deg]"))
        self.pushButton_kill.setToolTip(_translate("Form", "Delete this point"))

import eccw_gui.images.ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

