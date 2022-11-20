from check import Check
from errortypes import CheckError


class C_02(Check):
    def __init__(self, sheet, row=None):
        Check.__init__(self, sheet)

    def _code(self):
        return "C_02"

    def _type(self):
        return CheckError.BLOCKING

    def _columns_checked(self):
        return []

    # Code to execute during test
    # returns self.correct
    def perform(self):
        sheetProtection = self.sheet.protection.enabled
        self.correct = sheetProtection
        if not sheetProtection:
            self.error += f"Sheet is not protected"
