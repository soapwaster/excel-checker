from excel_checker.checkers.checker import Checker
from excel_checker.checkertypes import CheckerType
from typing import List


class MetadataChecker(Checker):
    """
    Checker used to check metadata of a Workbook

    """

    def __init__(self, workbook, checks: List[str]):
        Checker.__init__(self, workbook, CheckerType.METADATA)
        self.workbook = workbook
        self.checks = self._checksFromList(checks)
