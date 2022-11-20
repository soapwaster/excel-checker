from checkers.checker import Checker
from checkertypes import CheckerType


class SheetChecker(Checker):
    def __init__(self, sheet):
        Checker.__init__(self, sheet, CheckerType.SHEET)

    def __str__(self):
        v = super().__str__()
        return f" {self.sheet.title}: {v}"

    def encode(self):
        return {f"{self.sheet.title}": super().encode()}
