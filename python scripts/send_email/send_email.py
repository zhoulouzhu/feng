import smtplib                           #发送邮件模块
from email.mime.text import MIMEText    #定义邮件内容
from email.header import Header
import  email.mime.multipart
import  email.mime.text

msg = email.mime.multipart.MIMEMultipart()
#定义邮件标题
msg["Subject"]="duanx"
#发送邮箱服务器
smtpserver='smtp.163.com'

#发送邮箱用户名密码
user='zhoulouzhu@163.com'
password="zlz123"

#发送和接收邮箱
sender='zhoulouzhu@163.com'
receive='zhoulouzhu@126.com'

#发送邮件主题和内容
subject='狗蛋致敬'
content='<html><h1 style="color:green">亲爱的狗蛋同学' \
        '吃屎快乐！</h1></html>'

#HTML邮件正文
msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='zhoulouzhu@163.com'
msg['To'] = 'zhoulouzhu@126.com'

#SSL协议端口号要使用465
smtp = smtplib.SMTP_SSL(smtpserver, 465)

#HELO 向服务器标识用户身份
smtp.helo(smtpserver)
#服务器返回结果确认
smtp.ehlo(smtpserver)
#登录邮箱服务器用户名和密码
smtp.login(user,password)

print("开始发送邮件...")
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print("邮件发送完成！")
