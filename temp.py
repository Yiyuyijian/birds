import xlrd
from my_sqlite3 import my_sql

book = xlrd.open_workbook("./中国鸟类名录v2.2.xlsx")
sheet = book.sheet_by_index(0)
columns = '''(编号 integer,
中国鸟类野外手册编号,
IUCN红色名录等级,
中文名,
英文名,
学名,
属中文名,
属学名,
科中文名,
科学名,
目中文名,
目学名)'''


sql = my_sql("中国鸟类名录")

sql.create_table("v2_2",columns)
for i in range(2,sheet.nrows):
    print(i)
    sql.insert_row("v2_2",tuple(sheet.row_values(i)))
sql.close()