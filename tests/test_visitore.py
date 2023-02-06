from excel_checker.visitorum.components import CWorkbook, CWorksheet, CRow
from excel_checker.visitorum.checker_visitor import CheckerVisitor
from excel_checker import ExcelChecker
from sortedcollections import SortedSet
import excel_checker.visitorum.visitor_config as ic

def test_sets():

    rows : SortedSet(CRow) = SortedSet()
    excel_checker = ExcelChecker("res/sources/test/Cars.xlsx")

    workbook = excel_checker.wrkbk

    wc = CWorkbook(workbook)
    ws1 = wc.addSheet("Cars")
    wc.addSheet("Pollo")
    ws1.addRow(5)
    ws1.addRow(6)
    ws1.addRow(5)
    ws1.addCol(4)
    ws1.addCol(4)
    ws1.addCol(4)
    ws1.addCol(3)
    ws1.addCell(6, 4)
    ws1.addCell(6, 4)
    ws1.addCell(6, 2)
    ws1.addCell(2, 4)


    print(ws1.rows)
    print(ws1.columns)
    print(ws1.cells)

def test_create_from_config():
    wkb = ic.create_structure("res/sources/test/Cars.xlsx", "res/custom-checks/config.yaml")
    print(wkb)

def test_load_from_config():
    wkb = ic.create_structure("res/sources/test/Cars.xlsx", "res/custom-checks/config.yaml")
    ic.load_checks(CheckerVisitor("res.custom-checks", "res/custom-checks/config.yaml"), wkb, "res/custom-checks/config.yaml")


'''def test_vehicle():

    excel_checker = ExcelChecker("res/sources/test/Cars.xlsx")

    workbook = excel_checker.wrkbk

    wc = CWorkbook(workbook)
    ws1 = wc.addSheet("Cars")
    ws2 = wc.addSheet("Pollo")
    r1 = ws1.addRow(5)
    r2 = ws1.addRow(6)
    c1 = ws1.addCol(4)
    c = ws1.addCell(6, 4)

    cv = CheckerVisitor("res.custom-checks", "res/custom-checks/config.yaml")
    wc.accept(cv)'''
