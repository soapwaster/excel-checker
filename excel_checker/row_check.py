from excel_checker.check import Check
from excel_checker.visitorum.components import CRow


class RowCheck(Check):
    def __init__(self, row: CRow):
        Check.__init__(self, row.sheet)
        self.row = row
        self.i = row.i
        self.columns = self._columns_checked()

    # returns the excel codes of the columns to check
    def _columns_checked(self):
        pass
