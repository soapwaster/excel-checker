from check import Check
from row_check import RowCheck
from visitorum.components import CRow


class C_01(RowCheck):
    def __init__(self, row: CRow):
        RowCheck.__init__(self, row)

    def _code(self):
        return "C_01"

    def _columns_checked(self):
        return ["B"]

    # Code to execute during test
    # returns self.correct
    def perform(self):
        self.correct = True
        print(f"Checking row {self.row.getRowNum()}")
        return self.row.getColInRow(3)
