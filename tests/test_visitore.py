from excel_checker.visitorum.components import CWorkbook, CWorksheet, CRow, CCell
from excel_checker.visitorum.checker_visitor import CheckerVisitor
from excel_checker import ExcelChecker
from sortedcollections import SortedSet
import excel_checker.visitorum.visitor_config as ic
import json


def test_sets():

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


def test_create_from_config():
    wkb = ic.create_tree_structure(
        "res/sources/test/Cars.xlsx", "res/custom-checks/config.yaml"
    )


def test_create_from_config():
    wkb = ic.create_tree_structure(
        "res/sources/test/Cars.xlsx", "res/custom-checks/config_2.yaml"
    )
    assert "Casio" not in wkb.sheets
    assert len(wkb.sheets) == 2


def test_load_from_config():
    ic.load_checks("res/custom-checks/config.yaml")


def test_vehicle():

    wkb = ic.create_tree_structure(
        "res/sources/test/Cars.xlsx", "res/custom-checks/config.yaml"
    )
    cv = CheckerVisitor("res.custom-checks", "res/custom-checks/config.yaml")
    wkb.accept(cv)


def test_dealer():

    wkb = ic.create_tree_structure(
        "res/sources/test/Car Dealer.xlsx", "res/custom-checks/config_dealer.yaml"
    )
    cv = CheckerVisitor("res.custom-checks", "res/custom-checks/config_dealer.yaml")
    result = wkb.accept(cv)
    print(json.dumps(result, indent=4))


def test_dealer_2():

    excel_checker = ExcelChecker("res/sources/test/Car Dealer.xlsx")

    workbook = excel_checker.wrkbk

    wc = CWorkbook(workbook)
    ws1 = wc.addSheet("New")
    ws2 = wc.addSheet("Old")
    ws1.addRow(5)
    ws1.addRow(6)
    ws1.addRow(5)
    ws2.addRow(5)
    cv = CheckerVisitor("res.custom-checks", "res/custom-checks/config_dealer.yaml")
    result = wc.accept(cv)
    print(json.dumps(result, indent=4))
