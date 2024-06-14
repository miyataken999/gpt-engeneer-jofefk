import openpyxl

class ExcelParser:
    def parse(self, file):
        wb = openpyxl.load_workbook(file)
        data = []
        for sheet in wb:
            for row in sheet.iter_rows(values_only=True):
                data.append(row)
        return data