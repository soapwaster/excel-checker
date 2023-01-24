import openpyxl


class ExcelChecker:
    def __init__(self, workbookfilename):
        self.wrkbk = openpyxl.load_workbook(workbookfilename)
