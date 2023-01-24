from excel_checker.cell_check import CellCheck
from excel_checker.visitorum.components import CCell


class C_04(CellCheck):
    def __init__(self, cell: CCell):
        CellCheck.__init__(self, cell)

    def _code(self):
        return "C_04"

    # Code to execute during test
    # returns self.correct
    def perform(self):
        self.correct = True
        print(
            f"Checking cell {self.cell.getPosition()} in sheet {self.cell.sheet.title} with value {self.cell.getValue()}"
        )
        return self.cell.getValue()
