import yaml
import re
from excel_checker.excel_checker import ExcelChecker
from excel_checker.visitorum.components import CWorkbook, CWorksheet

def create_structure(file, configFile):
    data = {}
    with open(configFile, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    excel_checker = ExcelChecker(file)
    wkb = excel_checker.wrkbk
    wkb = CWorkbook(wkb)
    if "Sheets" in data:
        for sheet in data["Sheets"]:
            ws = wkb.addSheet(sheet["name"])
            if ws is None:
                continue
            if "Rows" in sheet:
                for row in sheet["Rows"]:
                    for i in range(row["from"], row["to"]+1):
                        ws.addRow(i)
            if "Columns" in sheet:
                for col in sheet["Columns"]:
                    for j in range(col["from"], col["to"]+1):
                        ws.addCol(j)
            if "Cells" in sheet:
                for cell in sheet["Cells"]:
                    result = re.search(r"^\((\d+),(\d+)\)$", cell["cell"])
                    if result is not None:
                        i = result.group(1)
                        j = result.group(2)
                        ws.addCell(i,j)
    return wkb

def load_checks(visitor, workbook : CWorkbook, configFile):
    data = {}
    with open(configFile, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    if "Workbook" in data:
        visitor.wbc = data["Workbook"]["checks"]
    if "Sheets" in data:
        for sheet in data["Sheets"]:
            sname = sheet["name"]
            if sname not in workbook.wbk.sheetnames:
                continue
            visitor.wsc[sname] = sheet["checks"]
            if "Rows" in sheet:
                visitor.rc[sname] = {}
                for row in sheet["Rows"]:
                    for i in range(row["from"], row["to"]+1):
                        val = visitor.rc[sname].get(i, [])
                        visitor.rc[sname][i] = val
                        visitor.rc[sname][i].extend(row["checks"])
            if "Columns" in sheet:
                visitor.cc[sname] = {}
                for col in sheet["Columns"]:
                    for j in range(col["from"], col["to"]+1):
                        val = visitor.cc[sname].get(j, [])
                        visitor.cc[sname][j] = val
                        visitor.cc[sname][j].extend(col["checks"])
            if "Cells" in sheet:
                visitor.cellc[sname] = {}
                for cell in sheet["Cells"]:
                    result = re.search(r"^\((\d+),(\d+)\)$", cell["cell"])
                    if result is not None:
                        i = result.group(1)
                        j = result.group(2)
                        val = visitor.cellc[sname].get(cell["cell"], [])
                        visitor.cellc[sname][cell["cell"]] = val
                        visitor.cellc[sname][cell["cell"]].extend(cell["checks"])
    print(visitor.wbc)
    print(visitor.wsc)
    print(visitor.rc)
    print(visitor.cc)
    print(visitor.cellc)


