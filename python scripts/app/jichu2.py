import os
import csv
path=r'D:\python scripts\app_jichu\123.txt'
print(path)
print(os.getcwd()+'\\'+'jichu2.py')
print(os.listdir(r'D:\python scripts\app_jichu')[0])
#os.remove('123.txt')
f=open(os.getcwd()+'\\'+'123.txt','w')

#print(f.read())
#print(f.read())
#print(f.readline(2))
#f.write('1test')
#s=('那是我的\n','曾经的爱很简单\n',"绽放出美丽不舍泪花")
#f.writelines(s)
#f.close()
#p=r'D:\python scripts\app_jichu\testdata.csv'
#c=csv.reader((p,'rb'))

rows = [['1', '2', '3'], ['4', '5', '6']]
with open('my.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in rows:
        writer.writerow(row)
with open('my.csv', 'r+', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(str(row))
with open('testdata.csv','r+',newline='') as  b:
    reader = csv.reader(b)
    for a in  reader:
        print(str(a))