import  xlwt
import  xlrd
import json
import xml.dom.minidom
#定义一个打开并读取excel表格的函数
def read_excel(path,col,index):
    #定义三个变量，第一个path路径，行数，第几个表
    xls = xlrd.open_workbook(path)
    #通过路径读取表格
    # sheet = xls.sheets()[0]
    #sheet = xls.sheet_by_name('工作')
    sheet = xls.sheet_by_index(index)
    #读取第几个表格

   # print(sheet.nrows)
    #print(sheet.ncols)
    #print(sheet.row_values(1)[0])
    list=[]
    #定义一个列表
    for i in range(sheet.nrows):
        #一个for循环输出表格内容，根据表格的行数
        #print(sheet.row_values(i)[0])
        list.append(sheet.row_values(i)[col])
        #逐行读取行数，列数
        #print(sheet.cell(0, i).value)

        # for i in  range(sheet.ncols):
        # print(sheet.row_values(0)[i])
        # print(i)
    return list
    #返回list获取的表格数据
    #print(list)

#print(read_excel(r'D:\python scripts\app\com_data\mycord.xlsx',0,0))
#print(read_excel(r'D:\python scripts\app_jichu\mycord.xlsx',1,0))
#填写，表格的路径，列数，第几个表，第几行
dic=[]
#dic[0]=list
#@print(dic[0])
def write_excel(path):
    #写excel文件

    ex=xlwt.Workbook()
    sheet=ex.add_sheet(u'测')
    sheet.write(0,0,"testl")
    sheet.write(0,2,u"测试")
    ex.save(path)

#write_excel(r'D:\python scripts\app_jichu\__pycache__\ttt1.xls')
def read_json(path):
    #定义一个读取js的函数
    f=open(path,'r')
    return  json.load(f)

#read_json(r'D:\python scripts\app_jichu\test.json')

def write_json(path,js):
    #写js
    f=open(path,'w')
    json.dump(js,f)

def read_xml(path):
    dom = xml.dom.minidom.parse("cc.xml")
    root = dom.documentElement
    list = root.getElementsByTagName('user')
    #print(list[0].getAttribute('id'))
    #print(list.getElementsByTagName("name").childNodes[0].nodeValue)
    list_user=[]
    list_password=[]
    for l in  list:
        list_user.append(l.getElementsByTagName("username")[0].childNodes[0].nodeValue)
        list_password.append(l.getElementsByTagName("username")[0].childNodes[0].nodeValue)
    print(list_user)
    print(list_password)
    return  list_user,list_password

#print(read_excel(r"D:\python scripts\app\mycord.xlsx",'mycord')[0])