from check import Check
from visitorum.components import CCell


class CellCheck(Check):
    def __init__(self, cell: CCell):
        Check.__init__(self, cell.sheet)
        self.cell = cell