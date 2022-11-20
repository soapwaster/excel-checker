from checkers.checker import Checker
from checkertypes import CheckerType

class DocumentChecker(Checker):
    def __init__(self, workbook):
        Checker.__init__(self, workbook, CheckerType.DOCUMENT)
        self.workbook = workbook
