
import  time
import smtplib
from email.mime.text import  MIMEText

from  email.mime.multipart import  MIMEMultipart

def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(("new report is :" + lists[-1]))

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file




smtpserver="smtp.163.com"
#发送邮箱用户、密码
user="zhoulouzhu@163.com"
password="zlz123"
#发送邮箱
sender="zhoulouzhu@163.com"
#接受邮箱
receivers=["zhoulouzhu@126.com,936791749@qq.com"]
#发送主题
subject="d382"

# 编写HTML类型的邮件正文（把HTML代码写进入）
content="<html><h1  style='color=green'>小毛驴123</h1></html>"

send_file=open(r'D:\python scripts\123.jpg',"rb").read()


att=MIMEText(send_file,"base64","utf-8")
att["content-type"]='application/octet-stream'
att['content-disposition']='attachment;filename="123.jpg"'

msgroot=MIMEMultipart()
msgroot.attach(MIMEText(content,'html',"utf-8"))
msgroot['subject']=subject
msgroot["from"]=sender
msgroot["to"]=",".join(receivers)
msgroot.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("开始发送")
smtp.sendmail(sender,receivers,msgroot.as_string())
smtp.quit()
print("发送完成")

