from excel_checker.visitorum.components import CWorkbook
from excel_checker.visitorum.checker_visitor import CheckerVisitor
from excel_checker import ExcelChecker


def test_vehicle():

    excel_checker = ExcelChecker("res/sources/test/Cars.xlsx")

    workbook = excel_checker.wrkbk

    wc = CWorkbook(workbook)
    ws1 = wc.addSheet("Cars")
    ws2 = wc.addSheet("Pollo")
    r1 = ws1.addRow(5)
    r2 = ws1.addRow(6)
    c1 = ws1.addCol(4)
    c = ws1.addCell(6, 4)

    cv = CheckerVisitor("res.custom-checks")
    wc.accept(cv)
