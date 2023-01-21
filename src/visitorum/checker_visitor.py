from visitor import Visitor
from components import CWorkbook, CCell, CCol, CRow, CWorksheet

class CheckerVisitor(Visitor):

    def __init__(self, pathToChecks) -> None:
        super().__init__()
        self.pathToChecks = pathToChecks #it has to be a module
        self.wbc = []
        self.wsc = []
        self.rc = []
        self.cc = []
        self.cellc = []
        self.res = {}

    def visit_workbook(self, wbk: CWorkbook) -> None:
        for check in self.wbc:
            pass

        for sheet in wbk.sheets:
            self.res[f"SHEET {sheet.getTitle}"] = sheet.accept(self)

    def visit_worksheet(self, wsh: CWorksheet) -> None:
        for row in wsh.rows:
            self.res[f"ROW {row.g}"] = sheet.accept(self)
    
    def visit_row(self, element: CRow) -> None:
        pass

    def visit_col(self, element: CCol) -> None:
        pass

    def visit_cell(self, element: CCell) -> None:
        pass

    def check()