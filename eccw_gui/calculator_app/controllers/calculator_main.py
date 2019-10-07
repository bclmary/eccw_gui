#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui
from collections import OrderedDict

from eccw_gui.calculator_app.viewers.calculator_main import Ui_Form
from eccw_gui.shared.controllers.lineEdit import SwitchScalarRange
from eccw_gui.shared.controllers.groupBox import GroupBoxContext
from eccw_gui.shared.wrappers import Wrapper, WrapperDict
from eccw_gui.shared.tools import graph_print

from eccw import EccwCompute


class CalculatorController(QtWidgets.QWidget, Ui_Form, WrapperDict):
    def __init__(self, **kwargs):
        super(CalculatorController, self).__init__()
        self.setupUi(self)
        # Init local attributs.
        self.n_digit_rounding = 4
        self.alpha = SwitchScalarRange(id="alpha")
        self.beta = SwitchScalarRange(id="beta")
        self.phiB = SwitchScalarRange(id="phiB")
        self.phiD = SwitchScalarRange(id="phiD")
        self.delta_lambdaB = SwitchScalarRange(id="delta_lambdaB")
        self.delta_lambdaD = SwitchScalarRange(id="delta_lambdaD")
        self.rho_f = SwitchScalarRange(id="rho_f")
        self.rho_sr = SwitchScalarRange(id="rho_sr")
        self.range = Wrapper(None)
        self.compute_core = EccwCompute()
        # List for SwitchScalarRange objects control.
        self.params_list_dry = ("alpha", "beta", "phiB", "phiD")
        self.params_list_fluids = ("delta_lambdaB", "delta_lambdaD", "rho_f", "rho_sr")
        self.param_list_all = [
            "alpha",
            "beta",
            "phiB",
            "phiD",
            "delta_lambdaB",
            "delta_lambdaD",
            "rho_f",
            "rho_sr",
        ]
        self.param_object_list = [
            self.alpha,
            self.beta,
            self.phiB,
            self.phiD,
            self.delta_lambdaB,
            self.delta_lambdaD,
            self.rho_f,
            self.rho_sr,
        ]
        self.context = GroupBoxContext()
        self.results = Wrapper("", action=self._init_results_slider_position)
        self.fluids = Wrapper(
            False,
            process=lambda x: eval(str(x)),
            action=self.groupBox_fluids.setChecked,
        )
        self.fluids_flag_list = ["delta_lambdaB", "delta_lambdaD", "rho_f", "rho_sr"]
        # List of radioButton defining focus
        self.focus_object_list = [
            self.checkBox_alpha,
            self.checkBox_beta,
            self.checkBox_phiB,
            self.checkBox_phiD,
        ]
        self.focus_flag_list = ["alpha", "beta", "phiB", "phiD"]
        for elt, txt in zip(self.focus_object_list, self.focus_flag_list):
            elt.ID = txt
        self.focus = Wrapper("alpha", action=self.set_focus)
        # Put them in self
        self.horizontalLayout_alpha.addWidget(self.alpha)
        self.horizontalLayout_beta.addWidget(self.beta)
        self.horizontalLayout_phiB.addWidget(self.phiB)
        self.horizontalLayout_phiD.addWidget(self.phiD)
        self.horizontalLayout_lamdaB.addWidget(self.delta_lambdaB)
        self.horizontalLayout_lamdaD.addWidget(self.delta_lambdaD)
        self.horizontalLayout_rhof.addWidget(self.rho_f)
        self.horizontalLayout_rhosr.addWidget(self.rho_sr)
        # self.verticalLayout_context.addWidget(self.context)
        self.horizontalLayout_context.addWidget(self.context)
        # Define behaviours
        tmp = lambda elt: lambda: self._there_can_be_only_one(elt)
        for elt in self.param_object_list:
            elt.pushButton.clicked.connect(tmp(elt))
        for elt in self.focus_object_list:
            elt.clicked.connect(self._auto_set_focus)
        self.groupBox_fluids.clicked.connect(self._fluidsChanged)
        self.pushButton_Clear.clicked.connect(self._clean_all)
        self.pushButton_Go.clicked.connect(self.click_compute)
        # Shortcuts for edit parameters.
        self._set_switchLineEdit_shortcuts(self.alpha, "Ctrl+1", "Ctrl+Alt+1")
        self._set_switchLineEdit_shortcuts(self.beta, "Ctrl+2", "Ctrl+Alt+2")
        self._set_switchLineEdit_shortcuts(self.phiB, "Ctrl+3", "Ctrl+Alt+3")
        self._set_switchLineEdit_shortcuts(self.phiD, "Ctrl+4", "Ctrl+Alt+4")
        self._set_switchLineEdit_shortcuts(self.delta_lambdaB, "Ctrl+5", "Ctrl+Alt+5")
        self._set_switchLineEdit_shortcuts(self.delta_lambdaD, "Ctrl+6", "Ctrl+Alt+6")
        self._set_switchLineEdit_shortcuts(self.rho_f, "Ctrl+7", "Ctrl+Alt+7")
        self._set_switchLineEdit_shortcuts(self.rho_sr, "Ctrl+8", "Ctrl+Alt+8")
        # Dictionnary (WrapperDict)
        self.dict = OrderedDict(
            [
                ("context", self.context),
                ("fluids", self.fluids),
                ("focus", self.focus),
                ("range", self.range),
                ("alpha", self.alpha),
                ("beta", self.beta),
                ("phiB", self.phiB),
                ("phiD", self.phiD),
                ("delta_lambdaB", self.delta_lambdaB),
                ("delta_lambdaD", self.delta_lambdaD),
                ("rho_f", self.rho_f),
                ("rho_sr", self.rho_sr),
                ("results", self.results),
            ]
        )
        # Additional variables
        self.name_convert = {
            "alpha": "α",
            "beta": "β",
            "phiB": "Φ<sub>B</sub>",
            "phiD": "Φ<sub>D</sub>",
            "delta_lambdaB": "∆λ<sub>B</sub>",
            "delta_lambdaD": "∆λ<sub>D</sub>",
            "rho_f": "ρ<sub>f</sub>",
            "rho_sr": "ρ<sub>sr</sub>",
        }
        self._result_table_header = self._make_result_table_line(
            [self.name_convert[elt] for elt in self.param_list_all]
        )
        # Fill values with kwargs
        if kwargs:
            self.set_params(**kwargs)
        self.show()

    # Methods.

    def _set_switchLineEdit_shortcuts(self, widget, scalar_key, range_key):
        QtWidgets.QShortcut(
            QtGui.QKeySequence(scalar_key), self, widget.set_focus_on_scalar
        )
        QtWidgets.QShortcut(
            QtGui.QKeySequence(range_key),
            self,
            lambda: self._there_can_be_only_one_range_focus(widget),
        )
        widget.pushButton.setToolTip(
            widget.pushButton.toolTip() + f" ({scalar_key} | {range_key})"
        )

    def _init_results_slider_position(self, x):
        self.textEdit_results.setText(x)
        scroll_bar = self.textEdit_results.verticalScrollBar()
        scroll_bar.setSliderPosition(scroll_bar.maximum())

    def _make_result_table_line(self, iterable, arg=""):
        """Format iterable using html tag; return a html table line."""
        td = "<td align='center', " + arg + ">"
        dttd = "</td>" + td
        return "<tr>" + td + dttd.join(iterable) + "</td></tr>"

    def _there_can_be_only_one(self, elt):
        if elt.focus.value == "scalar":
            self.range.value = None
        else:
            self.range.value = elt.id.value
        for Obj in self.param_object_list:
            if Obj is not elt:
                Obj.set_scalar_visible(True)

    def _there_can_be_only_one_range_focus(self, elt):
        elt.set_focus_on_range()
        self._there_can_be_only_one(elt)

    def set_focus(self, arg):
        for elt in self.focus_object_list:
            if elt.ID == arg:
                elt.setChecked(True)
        for elt in self.focus_object_list:
            self.__dict__[elt.ID].setEnabled(not elt.ID == arg)

    def _auto_set_focus(self):
        for elt in self.focus_object_list:
            if elt.isChecked():
                self.focus.value = elt.ID
                break
        for elt in self.focus_object_list:
            self.__dict__[elt.ID].setEnabled(not elt.ID == self.focus.value)

    def _fluidsChanged(self):
        self.fluids.value = self.groupBox_fluids.isChecked()

    def _clean_all(self):
        for elt in self.param_object_list:
            elt.clear()
        self.textEdit_results.clear()

    def click_compute(self):
        txt_result = "<p align='center'>"
        select = self.get_select()
        if select["fluids"]:
            params_list = self.param_list_all
        else:
            params_list = self.params_list_dry
        errors = self._check_arguments(select)
        if errors != "":
            txt_result += errors
        else:
            focus_parameter = self.focus.value
            ranged_parameter = self.range.value
            range_ = (
                [None]
                if ranged_parameter is None or ranged_parameter == focus_parameter
                else select[ranged_parameter]["value"]
            )
            result = []
            try:
                for x in range_:
                    params = {
                        flag: select[flag]["value"] if flag != ranged_parameter else x
                        for flag in params_list
                    }
                    params["context"] = self.context.get_params()
                    self.compute_core.reset()
                    self.compute_core.set_params(**params)
                    result.append(self.compute_core.compute(focus_parameter))
                result = [(i, j, k) for i, (j, k) in zip(range_, result)]
                txt_result += self._format_results(select, result)
            except (TypeError, ValueError) as err:
                txt_result += self._format_raised_error(err)
        txt_result += "<br/></p>"
        self.textEdit_results.append(txt_result)
        self.results.value += txt_result

    def _format_results(self, select, results):
        i = 0 if len(results) > 1 else 1
        txt = self._get_resume_params(select)
        n_rows_max = 5
        n_chars_per_row = 10
        txt += (
            "<table width='"
            + str((n_rows_max - i) * (n_chars_per_row + self.n_digit_rounding))
            + "%'>"
        )
        headers = ("●", "inverse", "normal")
        txt += self._make_result_table_line(headers[i:], arg="style='color: blue'")
        for res in results:
            txt += self._make_result_table_line(
                [
                    self._str_round(elt, self.n_digit_rounding)
                    if elt is not None
                    else "-"
                    for elt in res[i:]
                ]
            )
        txt += "</table>"
        return txt

    def _str_round(self, may_be_iterable, ndigits=None):
        """
        Apply round intrinsic function to
        * floats;
        * iterable containing floats.
        Return a string.
        """
        try:
            return str(round(may_be_iterable, ndigits))
        except TypeError:
            # All this concerns exclusively beta computation.
            if len(may_be_iterable) > 1:
                return ", ".join([str(round(elt, ndigits)) for elt in may_be_iterable])
            elif len(may_be_iterable) == 1:
                return str(round(may_be_iterable[0], ndigits))
            else:
                return "-"

    def _check_arguments(self, select):
        errors = ""
        message = " gets empty or invalid value<br/>"
        focus = self.focus.value
        for p_name in self.focus_flag_list:
            if select[p_name]["value"] is None and p_name != focus:
                errors += self.name_convert[p_name] + message
        if self.fluids.value:
            for p_name in self.fluids_flag_list:
                if select[p_name]["value"] is None:
                    errors += self.name_convert[p_name] + message
        return errors + ""

    def _format_raised_error(self, error):
        error = str(error)[19:]
        i1 = error.find("'")
        i2 = error.find("'", i1 + 1)
        name = self.name_convert[error[i1 + 1 : i2]]
        return error[:i1] + name + error[i2 + 1 :]

    def _get_resume_params(self, select):
        focus = self.focus.value
        context = " " + self.context.get_params() + " "
        n = 50 - len(context)
        title = "-" * n + context + "-" * n
        text = "<table width='100%'>"
        text += self._make_result_table_line(
            [title], arg="colspan='8'," "style='color: blue'"
        )
        text += self._result_table_header
        values = []
        for elt in self.param_list_all:
            value = select[elt]["value"]
            if elt == focus:
                value = "<span style='color: red'>▲</span>"
            elif value is None:
                value = "-"
            elif select[elt]["type"] == "range":
                value = "<span style='color: blue'>●</span>"
            elif not select["fluids"] and elt in self.params_list_fluids:
                value = "-"
            values.append(str(value))
        text += self._make_result_table_line(values)
        text += "</table>"
        return text


if __name__ == "__main__":
    import sys

    try:
        from eccw_gui.shared.file_management import EccwFile

        eccwf = EccwFile(filename="../../../tests/data/test.eccw")
        params = eccwf.values["calculator"]

        app = QtWidgets.QApplication(sys.argv)
        myapp = CalculatorController(**params)
        sys.exit(app.exec_())
    finally:
        print("values :")
        graph_print(myapp.get_select())
