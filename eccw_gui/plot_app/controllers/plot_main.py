#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os.path import dirname, realpath
from PyQt5 import QtCore, QtWidgets, QtGui
from collections import OrderedDict
from matplotlib.cm import get_cmap
import csv

from eccw_gui.plot_app.viewers.plot_main import Ui_Form
from eccw_gui.plot_app.controllers.curve_settings import CurveController
from eccw_gui.plot_app.controllers.point_settings import RefPointSettings
from eccw_gui.plot_app.controllers.title_settings import TitleEdit
from eccw_gui.plot_app.controllers.dialog_errors import Errors
from eccw_gui.plot_app.controllers.plot_window import PlotWindow
from eccw_gui.shared.wrappers import Wrapper, WrapperDict, WrapperList
from eccw_gui.shared.tools import graph_print

from eccw import EccwPlot


class PlotController(QtWidgets.QWidget, Ui_Form, WrapperDict):
    """Main widget for plotting curve and points.

    Keyword arguments:
    curves    -- awaits a dict of keyword arguments for a CurveController
                 element.
    refpoints -- awaits a dict of keyword arguments for a RefPointSettings
                 element.
    legend    -- awaits a boolean.
    title     -- awaits a boolean.

    This is a Qt derived object.
    """

    def __init__(self, **kwargs):
        super(PlotController, self).__init__()
        self.setupUi(self)
        self.plot_core = EccwPlot()
        self.plot_window = PlotWindow(self.plot_core.figure)
        self.current_dir = QtCore.QDir.homePath()
        self.import_mimetypes = (
            "Fichiers texte (*.txt *.dat *.csv);;" "Tout les Fichiers (*.*)"
        )
        # Init local attributs.
        self.curve_count = 0
        self.curves = WrapperList()
        self.refpoints = WrapperList()
        self.legend = Wrapper(
            False,
            process=lambda x: eval(str(x)),
            action=self.checkBox_legend.setChecked,
        )
        self.range_point = Wrapper(
            False,
            process=lambda x: eval(str(x)),
            action=self.checkBox_pointRange.setChecked,
        )
        self.title = TitleEdit()
        self.horizontalLayout_title.addWidget(self.title)
        # Init events
        self.pushButton_addRefPoint.clicked.connect(self.add_ref_point)
        self.pushButton_killAllRefPoints.clicked.connect(self.kill_all_refpoints)
        self.pushButton_openRefPoints.clicked.connect(self.import_ref_points)
        self.pushButton_addCurve.clicked.connect(self.add_curve_tab)
        self.pushButton_killAllCurves.clicked.connect(self.kill_all_curves)
        self.checkBox_legend.clicked.connect(self._set_legend)
        self.checkBox_pointRange.clicked.connect(self._set_range_point)
        # self.radioButton_title.clicked.connect(self._set_title)
        self.pushButton_plotOne.clicked.connect(self.plot_one)
        self.pushButton_plotAll.clicked.connect(self.plot_all)
        self.tabWidget.tabBar().tabMoved.connect(self._tab_moved)
        # Shortcuts
        TabW = self.tabWidget
        QtWidgets.QShortcut(
            QtGui.QKeySequence("Alt+Page up"),
            self,
            lambda: TabW.setCurrentIndex(TabW.currentIndex() - 1),
        )
        QtWidgets.QShortcut(
            QtGui.QKeySequence("Alt+Page down"),
            self,
            lambda: TabW.setCurrentIndex(TabW.currentIndex() + 1),
        )
        QtWidgets.QShortcut(
            QtGui.QKeySequence("Alt+T"), self, self.title.lineEdit.setFocus,
        )
        # Parameters list for dry and fluids cases.
        self.params_list_dry = ("phiB", "phiD")
        self.params_list_fluids = (
            "phiB",
            "phiD",
            "delta_lambdaB",
            "delta_lambdaD",
            "rho_f",
            "rho_sr",
        )
        self.params_list_refpoints = ("alpha", "beta")
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict(
            [
                ("curves", self.curves),
                ("refpoints", self.refpoints),
                ("legend", self.legend),
                ("range_point", self.range_point),
                ("title", self.title),
            ]
        )
        # Additional variables
        self.latex_convert = {
            "alpha": r"$\alpha$",
            "beta": r"$\beta$",
            "phiB": r"$\phi_{B}$",
            "phiD": r"$\phi_{D}$",
            "delta_lambdaB": r"$\Delta \lambda_{B}$",
            "delta_lambdaD": r"$\Delta \lambda_{D}$",
            "rho_f": r"\rho_{f}$",
            "rho_sr": r"\rho_{sr}$",
        }
        self.html_convert = {
            "alpha": "α",
            "beta": "β",
            "phiB": "Φ<sub>B</sub>",
            "phiD": "Φ<sub>D</sub>",
            "delta_lambdaB": "∆λ<sub>B</sub>",
            "delta_lambdaD": "∆λ<sub>D</sub>",
            "rho_f": "ρ<sub>f</sub>",
            "rho_sr": "ρ<sub>sr</sub>",
        }
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        if self.curve_count == 0:
            self.add_curve_tab()
        self.show()

    def closeEvent(self, event):
        """Close plot window when closing plot_main."""
        self.plot_window.close()
        event.accept()

    def set_params(self, **kwargs):
        # There must be as many curves and refpoints as asked to set.
        self.kill_all_curves()
        self.kill_all_refpoints()
        N = len(kwargs["curves"])
        for i in range(N):
            self.add_curve_tab(label=kwargs["curves"][i]["label"])
        N = len(kwargs["refpoints"])
        for i in range(N):
            self.add_ref_point()
        WrapperDict.set_params(self, **kwargs)

    def _set_legend(self):
        self.legend.value = self.checkBox_legend.isChecked()

    def _set_range_point(self):
        self.range_point.value = self.checkBox_pointRange.isChecked()

    def _tab_moved(self):
        self.curves.list = [
            self.tabWidget.widget(i) for i in range(self.tabWidget.count())
        ]

    def import_ref_points(self):
        """Add ref points using data from csv file.

        Awaited format:
        beta, alpha, size, style, label, red, green, blue, alpha_chanel

        beta in deg
        alpha in deg
        size in pixels
        style among ['c', 's', 'd', 't', '*', '+', 'p']
        label is any string value
        rgba color channels red, green , blue and alpha are floats in [0:1]
        """
        OpenDialog = QtWidgets.QFileDialog.getOpenFileName
        out_opendialog = OpenDialog(
            self, "Import from csv file", self.current_dir, self.import_mimetypes
        )
        file_name = out_opendialog[0]
        if file_name == "":
            return None  # Squip if no file selected.
        self.current_dir = dirname(realpath(file_name))
        with open(file_name, "r") as csvfile:
            parsed_data = csv.reader(csvfile)  # , dialect)
            errors = [
                "datas from file<br>%s<br> gets wrong items at lines:"
                "<br>" % file_name
            ]
            for i, row in enumerate(parsed_data):
                row = [elt.strip() for elt in row]
                if len(row) < 2:
                    errors.append("%s, " % (i + 1))
                    continue
                self.add_ref_point()
                params = {}
                params["beta"] = row[0]
                params["alpha"] = row[1]
                params["size"] = row[2] or 3.0 if len(row) > 2 else 3.0
                params["style"] = row[3] or "c" if len(row) > 3 else "circle"
                params["label"] = row[4] if len(row) > 4 else ""
                params["color"] = row[5:9] if len(row) > 8 else (0, 0, 0, 1)
                try:
                    self.refpoints.list[-1].set_params(**params)
                except TypeError:
                    errors.append("%s, " % (i + 1))
            if len(errors) > 1:
                errors.append(
                    "<br><br><b>Awaited parameters:</b><br>"
                    "beta, alpha, [size, style, label, color]<br>"
                    "<br><b>Awaited format:</b>"
                    "<table>"
                    "<tr><td>beta</th><td>float</th></tr>"
                    "<tr><td>alpha      </td><td>float</td></tr>"
                    "<tr><td>size</td><td>float &gt; 0</td></tr>"
                    "<tr><td>style</td><td>caracter in [c s d t * +"
                    " p]</td></tr>"
                    "<tr><td>label</td><td>string</td></tr>"
                    "<tr><td>color</td><td>4 floats in [0:1]</td>"
                    "</tr></table>"
                )
                QtWidgets.QMessageBox.about(self, "Warning", "".join(errors))

    # Curve tab management.

    def add_curve_tab(self, label=None):
        self.curve_count += 1
        name = "Curve " + str(self.curve_count) if label in (None, False) else label
        newCurve = CurveController(label=name)
        self.curves.list.append(newCurve)
        ncurve = len(self.curves.list)
        newCurve.pushButton_kill.clicked.connect(self.kill_curve_tab)
        # Single curve : put in frame widget
        if ncurve == 1:
            self.set_single_curve(newCurve)
            self.pushButton_killAllCurves.setEnabled(True)
        # Second curve : switch to tab widget
        elif ncurve == 2:
            firstCurve = self.curves.list[0]
            firstname = firstCurve.label.get_params()
            firstCurve.label.lineEdit.textChanged.connect(self._edit_tab_title)
            self.tabWidget.setVisible(True)
            self.tabWidget.addTab(firstCurve, firstname)
            self.frame_singleCurve.setVisible(False)
            firstCurve.setVisible(False)
        if ncurve > 1:
            self.tabWidget.addTab(newCurve, name)
            self.tabWidget.setCurrentWidget(newCurve)
            newCurve.label.lineEdit.textChanged.connect(self._edit_tab_title)

    def set_single_curve(self, curve):
        self.tabWidget.removeTab(0)
        self.tabWidget.setVisible(False)
        self.verticalLayout_singleCurve.addWidget(curve)
        curve.setVisible(True)
        self.frame_singleCurve.setVisible(True)

    def kill_curve_tab(self):
        for elt in list(self.curves.list):
            if elt.closed:
                i = self.tabWidget.indexOf(elt)
                self.tabWidget.setCurrentIndex(i - 1)
                self.tabWidget.removeTab(i)
                del self.curves.list[self.curves.list.index(elt)]
                break
        if len(self.curves.list) == 1:
            singlecurve = self.curves.list[0]
            self.set_single_curve(singlecurve)
            singlecurve.label.lineEdit.textChanged.disconnect(self._edit_tab_title)
        elif len(self.curves.list) == 0:
            self.pushButton_killAllCurves.setEnabled(False)

    def kill_all_curves(self):
        if len(self.curves.list) == 1:
            self.curves.list[0].close()
            self.curves.list[0].closed = True
            self.kill_curve_tab()
        else:
            for elt in list(self.curves.list):
                i = self.tabWidget.indexOf(elt)
                self.tabWidget.removeTab(i)
                del self.curves.list[self.curves.list.index(elt)]
        self.frame_singleCurve.setVisible(True)
        self.tabWidget.setVisible(False)
        self.pushButton_killAllCurves.setEnabled(False)

    def _edit_tab_title(self):
        i = self.tabWidget.currentIndex()
        title = self.tabWidget.currentWidget().label.get_params()
        self.tabWidget.setTabText(i, title)

    # RefPoint management.

    def add_ref_point(self):
        if not self.refpoints.list:
            self.pushButton_killAllRefPoints.setEnabled(True)
        newRefPoint = RefPointSettings()
        newRefPoint.pushButton_kill.clicked.connect(self.remove_ref_point)
        self.verticalLayout_points_settings.addWidget(newRefPoint)
        self.refpoints.list.append(newRefPoint)

    def remove_ref_point(self):
        for elt in list(self.refpoints.list):
            if elt.closed:
                del self.refpoints.list[self.refpoints.list.index(elt)]
        if not self.refpoints.list:
            self.pushButton_killAllRefPoints.setEnabled(False)

    def kill_all_refpoints(self):
        for elt in list(self.refpoints.list):
            elt.close()
            elt.closed = True
        self.remove_ref_point()
        self.pushButton_killAllRefPoints.setEnabled(False)

    # Main action !

    def plot_all(self):
        if len(self.curves.list) > 0:
            self.plot_core.reset_figure()
            selected_params = self.get_select()
            errors = self._check_params(selected_params)
            if not errors:
                for curve in selected_params["curves"]:
                    out = self._plot_curve(curve)
                    if out is not None:
                        self.plot_core.figure.clear()
                        self.errors = Errors(out)
                        return
                self._plot_other_stuffs(selected_params)
                self.plot_window.update()
                self.plot_window.show()
            else:
                self.errors = Errors(errors)

    def plot_one(self):
        if len(self.curves.list) > 0:
            self.plot_core.reset_figure()
            selected_params = self.get_select()
            i = self.tabWidget.currentIndex()
            curve = selected_params["curves"][i]
            errors = self._check_params(selected_params, index=i)
            if not errors:
                out = self._plot_curve(curve)
                if out is not None:
                    self.plot_core.figure.clear()
                    self.errors = Errors(out)
                    return
                self._plot_other_stuffs(selected_params)
                self.plot_window.update()
                self.plot_window.show()
            else:
                self.errors = Errors(errors)

    def _check_params(self, selected_params, index=None):
        errors = ""
        message = " gets empty or invalid value<br/>"
        iterable = [index] if index is not None else range(len(self.curves.list))
        for i in iterable:
            error = ""
            curve = selected_params["curves"][i]
            if curve["fluids"]:
                params_list = self.params_list_fluids
            else:
                params_list = self.params_list_dry
            for p_name in params_list:
                if curve[p_name]["value"] is None:
                    error += self.html_convert[p_name] + message
            if error:
                errors += "<b>" + curve["label"] + "</b><br/>" + error
        for i, refpoints in enumerate(selected_params["refpoints"]):
            error = ""
            for p_name in self.params_list_refpoints:
                if refpoints[p_name] is None:
                    error += self.html_convert[p_name] + message
            if error:
                label = refpoints["label"] or i + 1
                errors += "<b>Reference points %s</b><br/>" % (label) + error
        return errors

    def _plot_other_stuffs(self, selected_params, index=None):
        for refpoint in selected_params["refpoints"]:
            self.plot_core.add_refpoint(**refpoint)
        if selected_params["legend"]:
            self.plot_core.add_legend()
        if selected_params["title"]:
            self.plot_core.add_title(selected_params["title"])

    def _format_point_params(self, point_params, no_label=False):
        if point_params["beta"]["type"] == "scalar":
            params = {
                **point_params,
                "beta": point_params["beta"]["value"],
                "alpha": None,
                "alpha_min": point_params["alpha"]["value"]["min"],
                "alpha_max": point_params["alpha"]["value"]["max"],
            }
        if point_params["alpha"]["type"] == "scalar":
            params = {
                **point_params,
                "beta": None,
                "beta_min": point_params["beta"]["value"]["min"],
                "beta_max": point_params["beta"]["value"]["max"],
                "alpha": point_params["alpha"]["value"],
            }
        if no_label:
            params.pop("label")
        return params

    def _plot_curve(self, selected_params):
        settings_type = selected_params["settings"]["type"]
        if settings_type in ("default", "double"):
            out = self._plot_single_curve(selected_params)
        elif settings_type == "range":
            out = self._plot_ranged_curves(selected_params)
        return out

    def _plot_single_curve(self, selected_params):
        if selected_params["fluids"]:
            params_list = self.params_list_fluids
        else:
            params_list = self.params_list_dry
            self.plot_core.set_no_fluids()
        params = {
            "context": selected_params["context"],
            **{param: selected_params[param]["value"] for param in params_list},
        }
        graphic_settings = {
            "label": selected_params["label"],
            **selected_params["settings"]["value"],
        }
        self.plot_core.reset()
        self.plot_core.set_params(**params)
        # TEST
        errors = self.plot_core.check_params()
        if errors:
            return errors
        # END TEST
        self.plot_core.add_curve(**graphic_settings)
        # try:
        #     self.plot_core.set_params(**params)
        #     self.plot_core.add_curve(**graphic_settings)
        # except ValueError:
        #     self.errors = Errors("")
        #     return False
        # Draw points on line
        # and vertical or horizontal lines that visualize point intervals.
        for point in selected_params["points"]:
            params = self._format_point_params(point)
            self.plot_core.add_point(**params)
            if self.range_point.value is True:
                self.plot_core.add_line(**params)

    def _plot_ranged_curves(self, selected_params):
        if selected_params["fluids"]:
            params_list = self.params_list_fluids
        else:
            params_list = self.params_list_dry
            self.plot_core.set_no_fluids()
        graphic_settings = selected_params["settings"]["value"]
        ranged_parameter = selected_params["range"]
        latex_ranged_parameter = self.latex_convert[ranged_parameter]
        range_ = selected_params[ranged_parameter]["value"]
        if selected_params["reverse_cmap"]:
            cmap = get_cmap(graphic_settings.pop("colormap") + "_r")
        else:
            cmap = get_cmap(graphic_settings.pop("colormap"))
        number_of_color = len(range_) - 1
        # Ghost element that will be used as a title in the legend.
        self.plot_core.add_point(style="", label=selected_params["label"])
        # Draw ranged curves.
        for i, x in enumerate(range_):
            params = {
                "context": selected_params["context"],
                **{
                    param: selected_params[param]["value"]
                    if param != ranged_parameter
                    else x
                    for param in params_list
                },
            }
            self.plot_core.set_params(**params)
            # graphic_settings['color'] = cmap(i/number_of_color)
            graphic_settings.update(
                {
                    "label": (
                        latex_ranged_parameter + " = " + str(x)
                        if selected_params["label"]
                        else ""
                    ),
                    "color": cmap(i / number_of_color),
                }
            )
            self.plot_core.add_curve(**graphic_settings)
            for point in selected_params["points"]:
                params = self._format_point_params(point, no_label=True)
                try:  # DEBUG
                    self.plot_core.add_point(**params)
                except RuntimeError:
                    pass
        for point in selected_params["points"]:
            params = self._format_point_params(point)
            # Dummy element that will be used as legend for points to avoid
            # repetition.
            try:  # DEBUG
                self.plot_core.add_point(**params)
            except RuntimeError:
                pass
            # Draw vertical or horizontal lines that visualize point intervals
            if self.range_point.value is True:
                self.plot_core.add_line(**params)


if __name__ == "__main__":
    import sys
    from eccw_gui.shared.file_management import EccwFile

    eccwf = EccwFile(filename="../../../tests/data/test.eccw")
    # eccwf.show()
    params = eccwf.values["plot"]

    try:
        app = QtWidgets.QApplication(sys.argv)
        myapp = PlotController(**params)
        myapp.current_dir = "/home/bmary/Programmation/eccw/tests/"
        sys.exit(app.exec_())
    finally:
        print("params =")
        # graph_print(myapp.get_params())
        graph_print(myapp.get_select())
