#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from collections import OrderedDict
from os.path import dirname, realpath
import sys
import webbrowser

from eccw_gui.main_app.viewers.main import Ui_Form
from eccw_gui.main_app.controllers.dialog_about import About
from eccw_gui.calculator_app.controllers.calculator_main import CalculatorController
from eccw_gui.plot_app.controllers.plot_main import PlotController
from eccw_gui.shared.wrappers import WrapperDict
from eccw_gui.shared.file_management import EccwFile, open_documentation
from eccw_gui.shared.tools import graph_print


class MainController(QtWidgets.QWidget, Ui_Form, WrapperDict):
    """Main window of ECCW app."""
    def __init__(self, parent=None, **kwargs):
        super(MainController, self).__init__(parent)
        self.setupUi(self)
        self.current_dir = QtCore.QDir.homePath()
        self.mime_types = ("Fichier eccw (*.%s);;Tout les Fichiers (*.*)"
                           % EccwFile.mime)
        # Set calculator tab.
        self.calculator = CalculatorController()
        layoutC = QtWidgets.QVBoxLayout()
        layoutC.addWidget(self.calculator)
        self.tabWidget_main.widget(0).setLayout(layoutC)
        # Set plot tab.
        self.plot = PlotController()
        #self.plot.plot_window.setWindowIcon(self.app_icon)
        layoutP = QtWidgets.QVBoxLayout()
        layoutP.addWidget(self.plot)
        self.tabWidget_main.widget(1).setLayout(layoutP)
        # Define behaviours
        self.pushButton_Open.clicked.connect(self.load_session)
        self.pushButton_Save.clicked.connect(self.save_session)
        self.pushButton_About.clicked.connect(self.click_about)
        self.pushButton_Documentation.clicked.connect(self.click_doc)
        # Defines keyboard shortcuts.
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)
        TabW = self.tabWidget_main
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Page up"), self,
                        lambda: TabW.setCurrentIndex(TabW.currentIndex()-1))
        QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+Page down"), self,
                        lambda: TabW.setCurrentIndex(TabW.currentIndex()+1))
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict([
            ("calculator", self.calculator),
            ("plot",       self.plot)
        ])
        # Fill values with kwargs.
        if kwargs:
            self.set_params(**kwargs)
        self.show()

    def closeEvent(self, event):
        """Close plot window when closing main window."""
        self.plot.plot_window.close()
        event.accept()

    def click_about(self):
        self.about = About()

    def click_doc(self):
        open_documentation()

    # Save and load file management.

    def load_session(self):
        OpenDialog = QtWidgets.QFileDialog.getOpenFileName
        out_opendialog = OpenDialog(
            self,
            "Open file",
            self.current_dir,
            self.mime_types
            )
        file_name = out_opendialog[0]
        if file_name == "":
            return
        self.current_dir = dirname(realpath(file_name))
        eccwf = EccwFile(filename=file_name)
        if eccwf.values is None:
            message = ("Wrong file type.\n"
                       "Chosen file must be a *.eccw mime type.")
            QtWidgets.QMessageBox.about(self, "Error", message)
            return
        self.set_params(**eccwf.values)

    def save_session(self):
        SaveDialog = QtWidgets.QFileDialog.getSaveFileName
        file_name, _ = SaveDialog(self, "Save file", self.current_dir,
                                  self.mime_types)
        if file_name:
            eccwf = EccwFile(data=self.get_params())
            eccwf.save(file_name)


if __name__ == "__main__":
    eccwf = EccwFile(filename="../../../tests/data/test.eccw")
    params = eccwf.values
    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = MainController(**params)
        myapp.current_dir = "/home/bmary/Programmation/eccw/tests/"
        myapp.plot.current_dir = "/home/bmary/Programmation/eccw/tests/"
        sys.exit(app.exec_())
    finally:
        pass
        print("params =")
        graph_print(myapp.get_select())
