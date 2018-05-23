import  xlrd

xls=xlrd.open_workbook(r'D:\python scripts\app_jichu\mycord.xlsx')
#sheet = xls.sheets()[0]
#sheet = xls.sheet_by_name('test')
sheet =xls.sheet_by_index(1)

#print(sheet.nrows)
#print(sheet.ncols)
#print(sheet.row_values(1)[0])

for i in  range(sheet.ncols):
    #print(sheet.row_values(i)[0])
    print(sheet.cell(0,i).value)

#for i in  range(sheet.ncols):
    #print(sheet.row_values(0)[i])
    #print(i)
import xlwt
ex=xlwt.Workbook()
sheet=ex.add_sheet(u'测')
sheet.write(0,2,u"测试")
ex.save(r'D:\python scripts\app_jichu\__pycache__\ttt.xls')