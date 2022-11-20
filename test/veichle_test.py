from checkers.metadata_checker import MetadataChecker
from checkers.row_checker import RowChecker
from checkers.sheet_checker import SheetChecker
from checkers.document_checker import DocumentChecker
from excel_checker import ExcelChecker


def test_vehicle():

    filename = "Cars"
    excel_checker = ExcelChecker(f"res\\sources\\test\\{filename}.xlsx")

    workbook = excel_checker.wrkbk
    sheets = [workbook["Cars"], workbook["Bike"]]

    # the structure will look something like this
    # WorkbookChecker
    # ├── SheetChecker(Cars)
    # │   ├── RowChecker_5
    # │   ├── ...
    # │   ├── RowChecker_9
    # ├── SheetChecker(Bike)
    # │   ├── RowChecker_5
    # │   ├── ...
    # │   ├── RowChecker_9
    # └── MetadataChecker

    wc = DocumentChecker(workbook)

    for sheet in sheets:
        sc = SheetChecker(sheet)
        for i in range(5, 9):
            sc.addChecker(RowChecker(sheet, i, ["C_01"]))
        sc.addChecker(MetadataChecker(sheet, ["C_02"]))
        wc.addChecker(sc)
    wc.check()
    wc.exportCheckResult(f"res\\results\{filename}.txt")
    print(f"{filename} - {wc.checkerErrors}")


test_vehicle()
