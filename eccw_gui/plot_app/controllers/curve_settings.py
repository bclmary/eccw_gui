#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from collections import OrderedDict

from eccw_gui.plot_app.viewers.curve_settings import Ui_Form
from eccw_gui.plot_app.controllers.curve_graphicSettings import (
    SwitchCurveGraphicSettings,
)
from eccw_gui.plot_app.controllers.point_settings import CurvePointSettings
from eccw_gui.shared.controllers.lineEdit import SwitchScalarRange
from eccw_gui.shared.controllers.groupBox import GroupBoxContext
from eccw_gui.shared.controllers.lineEdit import StringLineEdit
from eccw_gui.shared.controllers.label import Label
from eccw_gui.shared.wrappers import Wrapper, WrapperDict, WrapperList
from eccw_gui.shared.tools import graph_print


class CurveController(QtWidgets.QWidget, Ui_Form, WrapperDict):
    """Widget for curve parameters and settings entry.

    Keyword arguments:
    label         -- awaits a string label.
    context       -- awaits a string among 'Compression' and 'Extension'.
    fluids        -- awaits a boolean.
    phiB          -- awaits a dict of keyword arguments for a SwitchScalarRange
                     element.
    phiD          -- awaits a dict of keyword arguments for a SwitchScalarRange
                     element.
    delta_lambdaB -- awaits a dict of keyword arguments for a SwitchScalarRange
                     element.
    delta_lambdaD -- awaits a dict of keyword arguments for a SwitchScalarRange
                     element.
    rho_f         -- awaits a dict of keyword arguments for a SwitchScalarRange
                     element.
    rho_sr        -- awaits a dict of keyword arguments for a SwitchScalarRange
                     element.
    settings      -- awaits a dict of keyword arguments for a
                     SwitchCurveGraphicSettings element.
    points        -- awaits a dict of keyword arguments for a
                     CurvePointSettings element.

    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        super(CurveController, self).__init__()
        self.setupUi(self)
        self.setAutoFillBackground(True)  # Needed by QTabWidget in plot_main.
        # Init local attributs.
        self.closed = False
        # Init additional objects
        # Mechanic.
        self.phiB = SwitchScalarRange(id="phiB")
        self.phiD = SwitchScalarRange(id="phiD")
        # Fluids.
        self.fluids = Wrapper(
            False,
            process=lambda x: eval(str(x)),
            action=self.groupBox_fluids.setChecked,
        )
        self.delta_lambdaB = SwitchScalarRange(id="delta_lambdaB")
        self.delta_lambdaD = SwitchScalarRange(id="delta_lambdaD")
        self.rho_f = SwitchScalarRange(id="rho_f")
        self.rho_sr = SwitchScalarRange(id="rho_sr")
        self.context = GroupBoxContext()
        # store name of ranged parameter if any.
        self.range = Wrapper(None)  # , process=self._set_ranged)
        # Label
        self.label_label = Label("la<u>b</u>el")
        self.label = StringLineEdit()
        # Graphic settings.
        self.settings = SwitchCurveGraphicSettings()
        # Curve points
        self.points = WrapperList()
        # Put additional elements in self.
        self.horizontalLayout_phiB.addWidget(self.phiB)
        self.horizontalLayout_phiD.addWidget(self.phiD)
        self.horizontalLayout_lamdaB.addWidget(self.delta_lambdaB)
        self.horizontalLayout_lamdaD.addWidget(self.delta_lambdaD)
        self.horizontalLayout_rhof.addWidget(self.rho_f)
        self.horizontalLayout_rhosr.addWidget(self.rho_sr)
        self.horizontalLayout_context.addWidget(self.context)
        self.verticalLayout_settings.addWidget(self.settings)
        self.horizontalLayout_label.addWidget(self.label_label)
        self.horizontalLayout_label.addWidget(self.label)
        # Shortcuts
        QtWidgets.QShortcut(
            QtGui.QKeySequence("Alt+B"), self, self.label.lineEdit.setFocus,
        )
        # List for SwitchScalarRange objects control.
        self.param_object_list = [
            self.phiB,
            self.phiD,
            self.delta_lambdaB,
            self.delta_lambdaD,
            self.rho_f,
            self.rho_sr,
        ]
        # Booleans
        self.split_curves = Wrapper(
            False,
            process=lambda x: eval(str(x)),
            action=self.checkBox_splittedCurves.setChecked,
        )
        self.reverse_cmap = Wrapper(
            False,
            process=lambda x: eval(str(x)),
            action=self.checkBox_reverseColormap.setChecked,
        )
        # Define events
        self.pushButton_addCurvePoint.clicked.connect(self.add_curve_point)
        self.pushButton_killAllCurvePoints.clicked.connect(self.kill_all_curve_point)
        self.checkBox_splittedCurves.clicked.connect(self._auto_set_settings)
        self.groupBox_fluids.clicked.connect(self._fluids_changed)
        self.checkBox_splittedCurves.clicked.connect(self._split_curve_changed)
        self.checkBox_reverseColormap.clicked.connect(self._reverse_cm_changed)
        tmp = lambda elt: lambda: self._there_can_be_only_one(elt)
        for elt in self.param_object_list:
            elt.pushButton.clicked.connect(tmp(elt))
        self.pushButton_kill.clicked.connect(self._set_closed)
        # Shortcuts for edit parameters.
        self._set_switchLineEdit_shortcuts(self.phiB, "Ctrl+3", "Ctrl+Alt+3")
        self._set_switchLineEdit_shortcuts(self.phiD, "Ctrl+4", "Ctrl+Alt+4")
        self._set_switchLineEdit_shortcuts(self.delta_lambdaB, "Ctrl+5", "Ctrl+Alt+5")
        self._set_switchLineEdit_shortcuts(self.delta_lambdaD, "Ctrl+6", "Ctrl+Alt+6")
        self._set_switchLineEdit_shortcuts(self.rho_f, "Ctrl+7", "Ctrl+Alt+7")
        self._set_switchLineEdit_shortcuts(self.rho_sr, "Ctrl+8", "Ctrl+Alt+8")
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict(
            [
                ("label", self.label),
                ("context", self.context),
                ("fluids", self.fluids),
                ("range", self.range),
                ("split_curves", self.split_curves),
                ("reverse_cmap", self.reverse_cmap),
                ("phiB", self.phiB),
                ("phiD", self.phiD),
                ("delta_lambdaB", self.delta_lambdaB),
                ("delta_lambdaD", self.delta_lambdaD),
                ("rho_f", self.rho_f),
                ("rho_sr", self.rho_sr),
                ("settings", self.settings),
                ("points", self.points),
            ]
        )
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        self._auto_set_settings()
        self.show()

    def set_params(self, **kwargs):
        # There must be as many points as asked to set.
        self.kill_all_curve_point()
        # Using dict get method allows to pass single parameters.
        N = len(kwargs.get("points", []))
        for i in range(N):
            self.add_curve_point()
        WrapperDict.set_params(self, **kwargs)
        for obj in self.param_object_list:
            if obj.focus.value == "range":
                self._there_can_be_only_one(obj)
                break

    # Events management.

    def _set_switchLineEdit_shortcuts(self, widget, scalar_key, range_key):
        QtWidgets.QShortcut(
            QtGui.QKeySequence(scalar_key),
            self,
            lambda: self._there_can_be_multiple_scalar_focus(widget),
        )
        QtWidgets.QShortcut(
            QtGui.QKeySequence(range_key),
            self,
            lambda: self._there_can_be_only_one_range_focus(widget),
        )
        widget.pushButton.setToolTip(
            widget.pushButton.toolTip() + f" ({scalar_key} | {range_key})"
        )

    def _set_closed(self):
        self.closed = True

    def _is_range_activated(self):
        return not all([Obj.focus.value == "scalar" for Obj in self.param_object_list])

    def _there_can_be_only_one(self, elt):
        if elt.focus.value == "scalar":
            self.range.value = None
        else:
            self.range.value = elt.id.value
        for Obj in self.param_object_list:
            if Obj is not elt:
                Obj.set_scalar_visible(True)
        self._auto_set_settings()

    def _there_can_be_only_one_range_focus(self, elt):
        elt.set_focus_on_range()
        self._there_can_be_only_one(elt)

    def _there_can_be_multiple_scalar_focus(self, elt):
        elt.set_focus_on_scalar()
        self._there_can_be_only_one(elt)

    def _auto_set_settings(self):
        # Next line solves blinking when switching from a focus to another.
        self.settings.set_visible_manual("")
        if self._is_range_activated():
            self.settings.set_visible_manual("range")
            self.checkBox_splittedCurves.setEnabled(False)
            self.checkBox_reverseColormap.setEnabled(True)
        else:
            self.checkBox_splittedCurves.setEnabled(True)
            self.checkBox_reverseColormap.setEnabled(False)
            if self.checkBox_splittedCurves.isChecked():
                self.settings.set_visible_manual("double")
            else:
                self.settings.set_visible_manual("default")

    def _fluids_changed(self):
        self.fluids.value = self.groupBox_fluids.isChecked()

    def _split_curve_changed(self):
        self.split_curves.value = self.checkBox_splittedCurves.isChecked()

    def _reverse_cm_changed(self):
        self.reverse_cmap.value = self.checkBox_reverseColormap.isChecked()

    # Curve Points management.

    def add_curve_point(self):
        if not self.points.list:
            self.pushButton_killAllCurvePoints.setEnabled(True)
        new_curve_point = CurvePointSettings()
        new_curve_point.pushButton_kill.clicked.connect(self.remove_curve_point)
        self.verticalLayout_points_settings.addWidget(new_curve_point)
        self.points.list.append(new_curve_point)

    def remove_curve_point(self):
        """un-list all invisible CurvePointSettings."""
        for elt in list(self.points.list):
            if elt.closed:
                del self.points.list[self.points.list.index(elt)]
        if not self.points.list:
            self.pushButton_killAllCurvePoints.setEnabled(False)

    def kill_all_curve_point(self):
        for elt in list(self.points.list):
            elt.close()
            elt.closed = True
        self.remove_curve_point()


if __name__ == "__main__":
    import sys

    try:
        app = QtWidgets.QApplication(sys.argv)

        phiB = {
            "range": {"begin": 25, "step": 5, "end": 45},
            "scalar": 30,
            "focus": "range",
        }
        point = {
            "alpha": {"bound": {"min": 0, "max": 4}, "scalar": 2, "focus": "bound"},
            "beta": {"bound": {"min": -1, "max": 1}, "scalar": 0, "focus": "scalar"},
            "sketch": True,
            "color": (0, 1, 0, 1),
            "size": 5,
            "style": "square",
            "label": "poulpe",
        }
        params = {
            "fluids": "False",
            "phiB": phiB,
            "label": "poulpe",
            "context": "Extension",
            "points": [point, point],
        }

        from eccw_gui.shared.file_management import EccwFile

        eccwf = EccwFile(filename="../../../tests/data/test.eccw")
        params = eccwf.values["plot"]["curves"][0]
        graph_print(params)

        myapp = CurveController(**params)

        sys.exit(app.exec_())
    finally:
        print("params =")
        graph_print(myapp.get_params(), indent=2)
        print("select =")
        graph_print(myapp.get_select(), indent=2)
