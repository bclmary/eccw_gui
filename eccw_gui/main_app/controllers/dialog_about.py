#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets

from eccw_gui.main_app.viewers.dialog_about import Ui_Dialog_About
from eccw_gui import __version__, __authors__, __license__
from eccw_gui import  __url__, __contact__


class About(QtWidgets.QWidget, Ui_Dialog_About):
    """Widget for software informations display."""

    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)
        self.label_version.setText(__version__)
        self.label_authors.setText("\n".join(__authors__))
        self.label_license.setText(__license__)
        color = '#888a85'
        url = "<a href='{}'> GitHub </a>".format(__url__)
        self.label_url.setText(url)
        contact = "<a href='mailto:{}'> {} </a>".format(__contact__, __contact__)
        self.label_contact.setText(contact)
        self.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myapp = About()
    sys.exit(app.exec_())
