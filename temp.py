import xlrd
from my_sqlite3 import my_sql
import openpyxl


def table_to_db():
    book = xlrd.open_workbook("./中国鸟类名录v10.0.xlsx")
    sheet = book.sheet_by_index(0)
    columns = '''(编号 INT PRIMARY KEY NOT NULL,
    中国鸟类野外手册编号 TEXT,
    IUCN红色名录等级 TEXT,
    中文名 TEXT NOT NULL,
    英文名 TEXT NOT NULL,
    学名 TEXT NOT NULL,
    属中文名 TEXT NOT NULL,
    属学名 TEXT NOT NULL,
    科中文名 TEXT,
    科学名 TEXT,
    目中文名 TEXT,
    目学名 TEXT,
    国家保护动物等级 TEXT)'''

    sql = my_sql("China_birds_checklist")

    sql.create_table("v10_0",columns)
    for i in range(2,sheet.nrows):
        row_datas:list = sheet.row_values(i)
        row_datas.insert(0,int(row_datas.pop(0)))
        #row_datas.append("-")
        row_datas.pop()
        sql.insert_row("v10_0",tuple(row_datas))
    sql.close()

def temp():
    book = openpyxl.load_workbook("./中国鸟类名录v10.0.xlsx")
    sheet = book.worksheets[0]
    cells = sheet["B"][2:]
    for cell in cells:
        if type(cell.value) == int:
            v = str(cell.value)
            v = v.rjust(4,"0")
            v = v + "#"
            cell.value = v
    book.save("./中国鸟类名录v10.0.xlsx")

if __name__ == "__main__":
    table_to_db()
