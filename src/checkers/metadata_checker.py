from checkers.checker import Checker
from checkertypes import CheckerType
from typing import List


class MetadataChecker(Checker):
    """
    Checker used to check metadata of a Workbook

    """

    def __init__(self, workbook, checks: List[str]):
        Checker.__init__(self, workbook, CheckerType.METADATA)
        self.workbook = workbook
        self.checks = self._checksFromList(checks)
