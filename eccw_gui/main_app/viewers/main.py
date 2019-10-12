# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../uis/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(714, 528)
        font = QtGui.QFont()
        font.setKerning(True)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon_eccw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.horizontalLayout_topmenu = QtWidgets.QHBoxLayout()
        self.horizontalLayout_topmenu.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_topmenu.setObjectName("horizontalLayout_topmenu")
        self.pushButton_Open = QtWidgets.QPushButton(Form)
        self.pushButton_Open.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_Open.setMaximumSize(QtCore.QSize(80, 28))
        self.pushButton_Open.setBaseSize(QtCore.QSize(80, 28))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/buttons/button_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Open.setIcon(icon1)
        self.pushButton_Open.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.horizontalLayout_topmenu.addWidget(self.pushButton_Open)
        self.pushButton_Save = QtWidgets.QPushButton(Form)
        self.pushButton_Save.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_Save.setMaximumSize(QtCore.QSize(80, 28))
        self.pushButton_Save.setBaseSize(QtCore.QSize(80, 28))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/buttons/button_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Save.setIcon(icon2)
        self.pushButton_Save.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout_topmenu.addWidget(self.pushButton_Save)
        self.line_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_topmenu.addWidget(self.line_2)
        self.pushButton_About = QtWidgets.QPushButton(Form)
        self.pushButton_About.setMinimumSize(QtCore.QSize(80, 28))
        self.pushButton_About.setMaximumSize(QtCore.QSize(80, 28))
        self.pushButton_About.setBaseSize(QtCore.QSize(80, 28))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/buttons/button_about.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_About.setIcon(icon3)
        self.pushButton_About.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_About.setObjectName("pushButton_About")
        self.horizontalLayout_topmenu.addWidget(self.pushButton_About)
        self.pushButton_Documentation = QtWidgets.QPushButton(Form)
        self.pushButton_Documentation.setMinimumSize(QtCore.QSize(140, 28))
        self.pushButton_Documentation.setMaximumSize(QtCore.QSize(140, 28))
        self.pushButton_Documentation.setBaseSize(QtCore.QSize(140, 28))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/buttons/button_documentation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Documentation.setIcon(icon4)
        self.pushButton_Documentation.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Documentation.setObjectName("pushButton_Documentation")
        self.horizontalLayout_topmenu.addWidget(self.pushButton_Documentation)
        self.verticalLayout_18.addLayout(self.horizontalLayout_topmenu)
        self.tabWidget_main = QtWidgets.QTabWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_main.sizePolicy().hasHeightForWidth())
        self.tabWidget_main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_main.setFont(font)
        self.tabWidget_main.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget_main.setAutoFillBackground(True)
        self.tabWidget_main.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget_main.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_main.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget_main.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidget_main.setDocumentMode(True)
        self.tabWidget_main.setTabsClosable(False)
        self.tabWidget_main.setObjectName("tabWidget_main")
        self.tab_calculator = QtWidgets.QWidget()
        self.tab_calculator.setAutoFillBackground(True)
        self.tab_calculator.setObjectName("tab_calculator")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/tabs/tab_calculate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_main.addTab(self.tab_calculator, icon5, "")
        self.tab_plot = QtWidgets.QWidget()
        self.tab_plot.setAutoFillBackground(True)
        self.tab_plot.setObjectName("tab_plot")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/tabs/tab_plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_main.addTab(self.tab_plot, icon6, "")
        self.verticalLayout_18.addWidget(self.tabWidget_main)

        self.retranslateUi(Form)
        self.tabWidget_main.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ECCW"))
        self.pushButton_Open.setToolTip(_translate("Form", "Open previously saved session (Crtl+O)"))
        self.pushButton_Open.setText(_translate("Form", "&Open"))
        self.pushButton_Open.setShortcut(_translate("Form", "Ctrl+O"))
        self.pushButton_Save.setToolTip(_translate("Form", "Save current session (Crtl+S)"))
        self.pushButton_Save.setText(_translate("Form", "&Save"))
        self.pushButton_Save.setShortcut(_translate("Form", "Ctrl+S"))
        self.pushButton_About.setToolTip(_translate("Form", "About ECCW software"))
        self.pushButton_About.setText(_translate("Form", "About"))
        self.pushButton_Documentation.setToolTip(_translate("Form", "Display pdf fulll documentation"))
        self.pushButton_Documentation.setText(_translate("Form", "Documentation"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_calculator), _translate("Form", "Calculator                    "))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_plot), _translate("Form", "Plot                              "))

import eccw_gui.images.ressources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

