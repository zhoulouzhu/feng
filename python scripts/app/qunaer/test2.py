from bus_ticket import  bus_car_ticket
from com_data.funct import  read_excel


s=read_excel('mycord.xlsx',0,0)
n=read_excel('mycord.xlsx',1,0)
bus_car_ticket(s,n)


#print(s=read_excel_dic(r"D:\python jiaoben\app\h.xlsx",0)[0])
#print(d=read_excel_dic(r"D:\python jiaoben\app\h.xlsx",1)[0])
#print (read_excel_dic('h.xlsx',0)[0])
#print (read_excel_dic('h.xlsx',0)[1])