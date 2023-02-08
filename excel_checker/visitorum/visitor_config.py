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
                        i = int(result.group(1))
                        j = int(result.group(2))
                        ws.addCell(i,j)
    return wkb

def load_checks(configFile):
    data = {}
    wbc = []
    wsc = {}
    rc = {}
    cc = {}
    cellc = {}
    with open(configFile, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    if "Workbook" in data:
        wbc = data["Workbook"]["checks"]
    if "Sheets" in data:
        for sheet in data["Sheets"]:
            sname = sheet["name"]
            wsc[sname] = sheet["checks"]
            if "Rows" in sheet:
                rc[sname] = {}
                for row in sheet["Rows"]:
                    for i in range(row["from"], row["to"]+1):
                        val = rc[sname].get(i, [])
                        rc[sname][i] = val
                        rc[sname][i].extend(row["checks"])
            if "Columns" in sheet:
                cc[sname] = {}
                for col in sheet["Columns"]:
                    for j in range(col["from"], col["to"]+1):
                        val = cc[sname].get(j, [])
                        cc[sname][j] = val
                        cc[sname][j].extend(col["checks"])
            if "Cells" in sheet:
                cellc[sname] = {}
                for cell in sheet["Cells"]:
                    result = re.search(r"^\((\d+),(\d+)\)$", cell["cell"])
                    if result is not None:
                        i = result.group(1)
                        j = result.group(2)
                        val = cellc[sname].get(cell["cell"], [])
                        cellc[sname][cell["cell"]] = val
                        cellc[sname][cell["cell"]].extend(cell["checks"])

    print(wbc)
    print(wsc)
    print(rc)
    print(cc)
    print(cellc)
    print("done")
    return wbc, wsc, rc, cc, cellc

