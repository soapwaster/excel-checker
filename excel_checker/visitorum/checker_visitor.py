import importlib
from typing import Any
import yaml
import excel_checker.visitorum.visitor_config as ic
from excel_checker.visitorum.visitor import Visitor
from excel_checker.visitorum.components import CWorkbook, CCell, CCol, CRow, CWorksheet


class CheckerVisitor(Visitor):
    def __init__(self, pathToChecks, checkConfig) -> None:
        super().__init__()
        self.pathToChecks = pathToChecks  # it has to be a module
        self.checkConfig = checkConfig  # yaml file containing check configurations
        self.wbc = []
        self.wsc = {}
        self.rc = {}
        self.cc = {}
        self.cellc = {}
        self.res = {}

    def visit_workbook(self, wbk: CWorkbook) -> None:
        val = {}
        self.load_checks(wbk)
        checks = self.__instantiate_checks(self.wbc, wbk)
        val[f"WORKBOOK-CHECKS"] = self.run_checks(checks)
        for sheet in wbk.sheets:
            val[f"SHEET - {sheet.getTitle()}"] = sheet.accept(self)
        print(val)

    def visit_worksheet(self, wsh: CWorksheet) -> None:
        val = {}
        checks = self.__instantiate_checks(self.wsc[wsh.getTitle()], wsh)
        val[f"SHEET-CHECKS"] = self.run_checks(checks)
        for row in wsh.rows:
            val[f"ROW {row.i}"] = row.accept(self)
        for col in wsh.columns:
            val[f"COL {col.j}"] = col.accept(self)
        for cell in wsh.cells:
            val[f"CELL {cell.getPosition()}"] = cell.accept(self)
        return val

    def visit_row(self, element: CRow) -> Any:
        checks = self.__instantiate_checks(self.rc[element.i], element)
        return self.run_checks(checks)

    def visit_column(self, element: CCol) -> Any:
        checks = self.__instantiate_checks(self.cc[element.j], element)
        return self.run_checks(checks)

    def visit_cell(self, element: CCell) -> Any:
        checks = self.__instantiate_checks(self.cellc, element)
        return self.run_checks(checks)

    def __instantiate_checks(self, type_of_checks, element):
        checks = []
        for check in type_of_checks:
            module = importlib.import_module(f"{self.pathToChecks}.{check}")
            class_ = getattr(module, check)
            instance = class_(
                element
            )  # here i would add the element so that they are specific to the element
            checks.append(instance)
        return checks

    def load_checks(self, wkb):
        ic.load_checks(self, wkb, self.checkConfig)

    def run_checks(self, checks):
        val = {}
        for check in checks:
            val[f"{check._code()}"] = check.perform()
        return val
