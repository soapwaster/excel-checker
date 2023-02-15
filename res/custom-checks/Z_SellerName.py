from excel_checker.cell_check import CellCheck
from excel_checker.visitorum.components import CCell


class Z_SellerName(CellCheck):
    
    def _code(self):
        return "SellerName"

    # Code to execute during test
    # returns self.correct
    def perform(self):
        self.correct = True
        print(
            f"Checking cell {self.cell.getPosition()} in sheet {self.cell.sheet.title} with value {self.cell.getValue()}"
        )
        self.correct = self.cell.getValue() == "Alessio Confalonieri"
        return self.cell.getValue()
