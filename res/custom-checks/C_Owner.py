from excel_checker.col_check import ColCheck


class C_Owner(ColCheck):
    def _code(self):
        return "C_Owner"

    def _row_checked(self):
        return range(7, 11)

    # Code to execute during test
    # returns self.correct
    def perform(self):
        self.correct = True

        for i in range(8, 11):
            po = int(self.column.getRowInCol(i))
            if po > 2:
                self.correct = False
                break
        return self.correct
