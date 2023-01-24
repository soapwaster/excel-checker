from excel_checker.check import Check
from excel_checker.visitorum.components import CCell


class CellCheck(Check):
    def __init__(self, cell: CCell):
        Check.__init__(self, cell.sheet)
        self.cell = cell
