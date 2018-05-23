import  smtplib
from  email.mime.text import MIMEText
from  email.mime.multipart import MIMEMultipart
#发送邮箱服务器
smtpserver="smtp.163.com"
#发送邮箱用户、密码
user="zhoulouzhu@163.com"
password="zlz123"
#发送邮箱
sender="zhoulouzhu@163.com"
#接受邮箱
receive=["zhoulouzhu@126.com"]
#发送主题
subject="shuk224"
#编写邮件正文
content="<html><h1 style='color=yellow'>程荣刚121</h1></html>"

send_file=open(r'D:\python scripts\123.html',"rb").read()

att=MIMEText(send_file,"base64","utf-8")
att["content-type"]='application/octet-stream'
att['content-disposition']='attachment:filename="123.html"'

msg=MIMEMultipart()
msg.attach(MIMEText(content,"html","utf-8"))
msg["subject"]=subject
msg["form"]=sender
msg["to"]=','.join(receive)
msg.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print("开始发送")

smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("发送完成")