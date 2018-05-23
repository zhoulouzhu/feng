
import smtplib
from email.mime.text import  MIMEText
from  email.mime.multipart import  MIMEMultipart

smtpserver="smtp.163.com"
user="zhoulouzhu@163.com"
password="zlz123"

sender="zhoulouzhu@163.com"
receivers=["zhoulouzhu@126.com,936791749@qq.com"]

subject="d382"
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