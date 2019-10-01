# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/calculator_main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(985, 837)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_draw = QtWidgets.QHBoxLayout()
        self.horizontalLayout_draw.setObjectName("horizontalLayout_draw")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_draw.addItem(spacerItem)
        self.label_draw = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_draw.sizePolicy().hasHeightForWidth())
        self.label_draw.setSizePolicy(sizePolicy)
        self.label_draw.setMaximumSize(QtCore.QSize(600, 250))
        self.label_draw.setFrameShape(QtWidgets.QFrame.Box)
        self.label_draw.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_draw.setText("")
        self.label_draw.setPixmap(QtGui.QPixmap(":/illustrations/illustration_calculator.png"))
        self.label_draw.setScaledContents(True)
        self.label_draw.setObjectName("label_draw")
        self.horizontalLayout_draw.addWidget(self.label_draw)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_draw.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_draw)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(19, 107, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.groupBox_parameters = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_parameters.sizePolicy().hasHeightForWidth())
        self.groupBox_parameters.setSizePolicy(sizePolicy)
        self.groupBox_parameters.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_parameters.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_parameters.setFont(font)
        self.groupBox_parameters.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_parameters)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_beta = QtWidgets.QHBoxLayout()
        self.horizontalLayout_beta.setSpacing(0)
        self.horizontalLayout_beta.setObjectName("horizontalLayout_beta")
        self.gridLayout.addLayout(self.horizontalLayout_beta, 1, 4, 1, 1)
        self.radioButton_alpha = QtWidgets.QRadioButton(self.groupBox_parameters)
        self.radioButton_alpha.setMaximumSize(QtCore.QSize(20, 16777215))
        self.radioButton_alpha.setText("")
        self.radioButton_alpha.setChecked(True)
        self.radioButton_alpha.setObjectName("radioButton_alpha")
        self.gridLayout.addWidget(self.radioButton_alpha, 0, 0, 1, 1)
        self.radioButton_beta = QtWidgets.QRadioButton(self.groupBox_parameters)
        self.radioButton_beta.setMaximumSize(QtCore.QSize(20, 16777215))
        self.radioButton_beta.setText("")
        self.radioButton_beta.setObjectName("radioButton_beta")
        self.gridLayout.addWidget(self.radioButton_beta, 1, 0, 1, 1)
        self.radioButton_phiD = QtWidgets.QRadioButton(self.groupBox_parameters)
        self.radioButton_phiD.setMaximumSize(QtCore.QSize(20, 16777215))
        self.radioButton_phiD.setText("")
        self.radioButton_phiD.setObjectName("radioButton_phiD")
        self.gridLayout.addWidget(self.radioButton_phiD, 1, 5, 1, 1)
        self.horizontalLayout_alpha = QtWidgets.QHBoxLayout()
        self.horizontalLayout_alpha.setSpacing(0)
        self.horizontalLayout_alpha.setObjectName("horizontalLayout_alpha")
        self.gridLayout.addLayout(self.horizontalLayout_alpha, 0, 4, 1, 1)
        self.radioButton_phiB = QtWidgets.QRadioButton(self.groupBox_parameters)
        self.radioButton_phiB.setMaximumSize(QtCore.QSize(20, 16777215))
        self.radioButton_phiB.setText("")
        self.radioButton_phiB.setObjectName("radioButton_phiB")
        self.gridLayout.addWidget(self.radioButton_phiB, 0, 5, 1, 1)
        self.label_phiD = QtWidgets.QLabel(self.groupBox_parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phiD.sizePolicy().hasHeightForWidth())
        self.label_phiD.setSizePolicy(sizePolicy)
        self.label_phiD.setMaximumSize(QtCore.QSize(20, 24))
        self.label_phiD.setPixmap(QtGui.QPixmap(":/params/params_phiD.png"))
        self.label_phiD.setScaledContents(True)
        self.label_phiD.setObjectName("label_phiD")
        self.gridLayout.addWidget(self.label_phiD, 1, 6, 1, 1)
        self.label_phiB = QtWidgets.QLabel(self.groupBox_parameters)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_phiB.sizePolicy().hasHeightForWidth())
        self.label_phiB.setSizePolicy(sizePolicy)
        self.label_phiB.setMaximumSize(QtCore.QSize(20, 24))
        self.label_phiB.setText("")
        self.label_phiB.setPixmap(QtGui.QPixmap(":/params/params_phiB.png"))
        self.label_phiB.setScaledContents(True)
        self.label_phiB.setObjectName("label_phiB")
        self.gridLayout.addWidget(self.label_phiB, 0, 6, 1, 1)
        self.horizontalLayout_phiD = QtWidgets.QHBoxLayout()
        self.horizontalLayout_phiD.setSpacing(0)
        self.horizontalLayout_phiD.setObjectName("horizontalLayout_phiD")
        self.gridLayout.addLayout(self.horizontalLayout_phiD, 1, 7, 1, 1)
        self.horizontalLayout_phiB = QtWidgets.QHBoxLayout()
        self.horizontalLayout_phiB.setSpacing(0)
        self.horizontalLayout_phiB.setObjectName("horizontalLayout_phiB")
        self.gridLayout.addLayout(self.horizontalLayout_phiB, 0, 7, 1, 1)
        self.label_alpha = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_alpha.setMaximumSize(QtCore.QSize(12, 24))
        self.label_alpha.setText("")
        self.label_alpha.setPixmap(QtGui.QPixmap(":/params/params_alpha.png"))
        self.label_alpha.setScaledContents(True)
        self.label_alpha.setObjectName("label_alpha")
        self.gridLayout.addWidget(self.label_alpha, 0, 1, 1, 1)
        self.label_beta = QtWidgets.QLabel(self.groupBox_parameters)
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
        self.gridLayout.addWidget(self.label_beta, 1, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_parameters)
        self.groupBox_fluids = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_fluids.sizePolicy().hasHeightForWidth())
        self.groupBox_fluids.setSizePolicy(sizePolicy)
        self.groupBox_fluids.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_fluids.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_fluids.setFont(font)
        self.groupBox_fluids.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_fluids.setCheckable(True)
        self.groupBox_fluids.setChecked(False)
        self.groupBox_fluids.setObjectName("groupBox_fluids")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_fluids)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_lamdaB = QtWidgets.QLabel(self.groupBox_fluids)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lamdaB.sizePolicy().hasHeightForWidth())
        self.label_lamdaB.setSizePolicy(sizePolicy)
        self.label_lamdaB.setMaximumSize(QtCore.QSize(30, 24))
        self.label_lamdaB.setPixmap(QtGui.QPixmap(":/params/params_lamdaB.png"))
        self.label_lamdaB.setScaledContents(True)
        self.label_lamdaB.setObjectName("label_lamdaB")
        self.gridLayout_2.addWidget(self.label_lamdaB, 0, 0, 1, 1)
        self.horizontalLayout_lamdaB = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lamdaB.setSpacing(0)
        self.horizontalLayout_lamdaB.setObjectName("horizontalLayout_lamdaB")
        self.gridLayout_2.addLayout(self.horizontalLayout_lamdaB, 0, 1, 1, 1)
        self.label_rhof = QtWidgets.QLabel(self.groupBox_fluids)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rhof.sizePolicy().hasHeightForWidth())
        self.label_rhof.setSizePolicy(sizePolicy)
        self.label_rhof.setMaximumSize(QtCore.QSize(24, 24))
        self.label_rhof.setText("")
        self.label_rhof.setPixmap(QtGui.QPixmap(":/params/params_rhof.png"))
        self.label_rhof.setScaledContents(True)
        self.label_rhof.setObjectName("label_rhof")
        self.gridLayout_2.addWidget(self.label_rhof, 0, 2, 1, 1)
        self.horizontalLayout_rhof = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rhof.setSpacing(0)
        self.horizontalLayout_rhof.setObjectName("horizontalLayout_rhof")
        self.gridLayout_2.addLayout(self.horizontalLayout_rhof, 0, 3, 1, 1)
        self.label_lamdaD = QtWidgets.QLabel(self.groupBox_fluids)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_lamdaD.sizePolicy().hasHeightForWidth())
        self.label_lamdaD.setSizePolicy(sizePolicy)
        self.label_lamdaD.setMaximumSize(QtCore.QSize(30, 24))
        self.label_lamdaD.setText("")
        self.label_lamdaD.setPixmap(QtGui.QPixmap(":/params/params_lamdaD.png"))
        self.label_lamdaD.setScaledContents(True)
        self.label_lamdaD.setObjectName("label_lamdaD")
        self.gridLayout_2.addWidget(self.label_lamdaD, 1, 0, 1, 1)
        self.horizontalLayout_lamdaD = QtWidgets.QHBoxLayout()
        self.horizontalLayout_lamdaD.setSpacing(0)
        self.horizontalLayout_lamdaD.setObjectName("horizontalLayout_lamdaD")
        self.gridLayout_2.addLayout(self.horizontalLayout_lamdaD, 1, 1, 1, 1)
        self.label_rhosr = QtWidgets.QLabel(self.groupBox_fluids)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_rhosr.sizePolicy().hasHeightForWidth())
        self.label_rhosr.setSizePolicy(sizePolicy)
        self.label_rhosr.setMaximumSize(QtCore.QSize(24, 24))
        self.label_rhosr.setText("")
        self.label_rhosr.setPixmap(QtGui.QPixmap(":/params/params_rhosr.png"))
        self.label_rhosr.setScaledContents(True)
        self.label_rhosr.setObjectName("label_rhosr")
        self.gridLayout_2.addWidget(self.label_rhosr, 1, 2, 1, 1)
        self.horizontalLayout_rhosr = QtWidgets.QHBoxLayout()
        self.horizontalLayout_rhosr.setSpacing(0)
        self.horizontalLayout_rhosr.setObjectName("horizontalLayout_rhosr")
        self.gridLayout_2.addLayout(self.horizontalLayout_rhosr, 1, 3, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_fluids)
        spacerItem4 = QtWidgets.QSpacerItem(20, 107, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_context = QtWidgets.QHBoxLayout()
        self.horizontalLayout_context.setObjectName("horizontalLayout_context")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_context.addItem(spacerItem5)
        self.verticalLayout_context = QtWidgets.QVBoxLayout()
        self.verticalLayout_context.setObjectName("verticalLayout_context")
        self.horizontalLayout_context.addLayout(self.verticalLayout_context)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_context.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_context)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_GoClear = QtWidgets.QHBoxLayout()
        self.horizontalLayout_GoClear.setObjectName("horizontalLayout_GoClear")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_GoClear.addItem(spacerItem8)
        self.pushButton_Go = QtWidgets.QPushButton(Form)
        self.pushButton_Go.setMinimumSize(QtCore.QSize(80, 32))
        self.pushButton_Go.setMaximumSize(QtCore.QSize(80, 32))
        self.pushButton_Go.setBaseSize(QtCore.QSize(80, 32))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/buttons/button_compute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Go.setIcon(icon)
        self.pushButton_Go.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Go.setObjectName("pushButton_Go")
        self.horizontalLayout_GoClear.addWidget(self.pushButton_Go)
        self.pushButton_Clear = QtWidgets.QPushButton(Form)
        self.pushButton_Clear.setMinimumSize(QtCore.QSize(54, 32))
        self.pushButton_Clear.setMaximumSize(QtCore.QSize(54, 32))
        self.pushButton_Clear.setBaseSize(QtCore.QSize(54, 32))
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.horizontalLayout_GoClear.addWidget(self.pushButton_Clear)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_GoClear.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_GoClear)
        self.horizontalLayout_Results = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Results.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_Results.setObjectName("horizontalLayout_Results")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Results.addItem(spacerItem10)
        self.textEdit_results = QtWidgets.QTextEdit(Form)
        self.textEdit_results.setMinimumSize(QtCore.QSize(600, 200))
        self.textEdit_results.setMaximumSize(QtCore.QSize(600, 16777215))
        self.textEdit_results.setToolTip("")
        self.textEdit_results.setReadOnly(True)
        self.textEdit_results.setObjectName("textEdit_results")
        self.horizontalLayout_Results.addWidget(self.textEdit_results)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Results.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_Results)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_parameters.setTitle(_translate("Form", "Select parameter to calculate"))
        self.radioButton_alpha.setToolTip(_translate("Form", "Check for calculate critical surface slope"))
        self.radioButton_beta.setToolTip(_translate("Form", "Check for calculate basal slope"))
        self.radioButton_phiD.setToolTip(_translate("Form", "Check for calculate basal friction angle"))
        self.radioButton_phiB.setToolTip(_translate("Form", "Check for calculate bulk friction angle"))
        self.label_phiD.setToolTip(_translate("Form", "Basal friction angle [deg]"))
        self.label_phiB.setToolTip(_translate("Form", "Bulk friction angle [deg]"))
        self.label_alpha.setToolTip(_translate("Form", "Critical surface slope [deg]"))
        self.label_beta.setToolTip(_translate("Form", "Basal slope [deg]"))
        self.groupBox_fluids.setToolTip(_translate("Form", "Check to activate fluids pore pressure parameters"))
        self.groupBox_fluids.setTitle(_translate("Form", "F&luids pore pressure"))
        self.label_lamdaB.setToolTip(_translate("Form", "Bulk fluids overpressure ratio"))
        self.label_rhof.setToolTip(_translate("Form", "Volumetric mass density of fluids"))
        self.label_lamdaD.setToolTip(_translate("Form", "Bulk fluids overpressure ratio"))
        self.label_rhosr.setToolTip(_translate("Form", "Volumetric mass density of saturated rock"))
        self.pushButton_Go.setToolTip(_translate("Form", "Launch calculation (Crtl+G)"))
        self.pushButton_Go.setText(_translate("Form", "Go"))
        self.pushButton_Go.setShortcut(_translate("Form", "Ctrl+G"))
        self.pushButton_Clear.setToolTip(_translate("Form", "Clear inputs and results fields"))
        self.pushButton_Clear.setText(_translate("Form", "Clear"))
        self.textEdit_results.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

import eccw_gui.images.ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
