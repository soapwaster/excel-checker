from excel_checker.checkers.checker import Checker
from excel_checker.checkertypes import CheckerType


class DocumentChecker(Checker):
    def __init__(self, workbook):
        Checker.__init__(self, workbook, CheckerType.DOCUMENT)
        self.workbook = workbook
