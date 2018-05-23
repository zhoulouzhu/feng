import  os
report_dir=r'D:\python scripts\untitled1\.idea'
lists=os.listdir(report_dir)

lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
print(lists)
print("latest report is :"+lists[-1])

#输出最新报告的路径
file=os.path.join(report_dir,lists[-1])
print(file)