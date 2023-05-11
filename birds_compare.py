import xlrd

file1="D:\\birds_datas\\全国鸟类记录2023年4月16日.xlsx"
file2="D:\\birds_datas\\全国鸟类记录2023年5月10日.xlsx"

book1 = xlrd.open_workbook(file1)
book2 = xlrd.open_workbook(file2)
names = book1.sheet_names()
for name in names:
    sheet1 = book1.sheet_by_name(name)
    sheet2 = book2.sheet_by_name(name)
    print(name,sheet1.nrows,sheet2.nrows)
    print("前有后无:",name,set(sheet1.col_values(2,1))-set(sheet2.col_values(2,1)))
    print("后有前无:",name,set(sheet2.col_values(2,1))-set(sheet1.col_values(2,1)))




