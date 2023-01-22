from check import Check
from visitorum.components import CWorksheet


class C_02(Check):
    def __init__(self, element: CWorksheet):
        self.element = element
        Check.__init__(self, element.wsh)

    def _code(self):
        return "C_02"

    def _columns_checked(self):
        return ["B", "C", "D"]

    # Code to execute during test
    # returns self.correct
    def perform(self):
        return "OKNO"
