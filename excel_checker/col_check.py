from excel_checker.check import Check
from excel_checker.visitorum.components import CCol


class ColCheck(Check):
    def __init__(self, column: CCol):
        Check.__init__(self, column.sheet)
        self.column = column
        self.rows = self._rows_checked()

    # returns the excel codes of the columns to check
    def _rows_checked(self):
        pass
