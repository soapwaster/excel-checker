from checkers.checker import Checker
from checkertypes import CheckerType
from typing import List


class RowChecker(Checker):
    """
    Leaf checker, that perform checks on a specific row of an Excel sheet

    """

    def __init__(self, sheet, row, checks: List[str]):
        Checker.__init__(self, sheet, CheckerType.ROW)
        self.row = row
        self.checks = self._checksFromList(checks, self.row)

    def __str__(self):
        v = super().__str__()
        return f"Row {self.row}: {v}" if v != "{}" else f"Row {self.row}: < OK >"

    def encode(self):
        return {f"Row {self.row}": super().encode()}
