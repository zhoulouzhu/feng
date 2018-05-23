import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
''''' 
最后终于还是找到解决办法了：邮件主题为‘test’的时候就会出现错误，换成其他词就好了。。我也不知道这是什么奇葩的原因 
'''
msg['Subject'] = 'duanx'
msg['From'] = 'zhoulouzhu@163.com'
msg['To'] = '936791749@qq.com'
content = '<html><h1 style="color:red">你好，小明</h1></html>'


txt = email.mime.text.MIMEText(content)  
msg.attach(txt)  

#smtp = smtplib  
smtp = smtplib.SMTP()  
smtp.connect('smtp.126.com', '25')  
smtp.login('zhoulouzhu@163.com', '12552163wjj')
smtp.sendmail('936791749@qq.com', '936791749@qq.com', msg.as_string())
smtp.quit()  
print('邮件发送成功email has send out !')