from check import Check
from errortypes import CheckError


class C_01(Check):
    def __init__(self, sheet, row=None):
        self.row = row
        Check.__init__(self, sheet)

    def _code(self):
        return "C_01"

    def _type(self):
        return CheckError.BLOCKING

    def _columns_checked(self):
        return ["B", "C", "D"]

    # Code to execute during test
    # returns self.correct
    def perform(self):
        type = self.sheet.cell(row=self.row, column=2).value
        power = self.sheet.cell(row=self.row, column=3).value
        hp = self.sheet.cell(row=self.row, column=4).value

        inType = type in ["Car", "Bike"]
        goodRatio = hp / power > 1
        self.correct = inType and goodRatio
        if not inType:
            self.error += f"Vechicle type cannot be {type}. "
        if not goodRatio:
            self.error += f"Vehicle HP/Power cannot be <= 1"
