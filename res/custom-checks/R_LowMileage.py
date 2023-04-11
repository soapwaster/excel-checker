from excel_checker.row_check import RowCheck


class R_LowMileage(RowCheck):
    def _code(self):
        return "R_LowMileage"

    def _columns_checked(self):
        return ["D", "E"]

    # Code to execute
    # returns self.correct
    def perform(self):
        self.correct = True

        year = int(self.row.getColInRow(4))
        kms = int(self.row.getColInRow(5))

        if year > 2000 and kms > 120000:
            self.correct = False

        return self.correct

        return self.correct