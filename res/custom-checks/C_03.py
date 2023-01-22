from check import Check
from col_check import ColCheck
from visitorum.components import CCol


class C_03(ColCheck):
    def __init__(self, col: CCol):
        ColCheck.__init__(self, col)

    def _code(self):
        return "C_03"

    def _row_checked(self):
        return ["3"]

    # Code to execute during test
    # returns self.correct
    def perform(self):
        self.correct = True
        print(f"Checking column {self.column.j}")
        return self.column.getRowInCol(4)
