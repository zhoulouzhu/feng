import smtplib
from email.mime.text import MIMEText  # MIMEText()定义邮件正文
from email.header import Header  # Header()定义邮件标题

# 发送邮箱服务器
smtpserver = 'smtp.sina.com'

# 发送邮箱用户/密码(登录邮箱操作)
user = "username@sina.com"
password = "password"

# 发送邮箱
sender = "username@sina.com"

# 接收邮箱
receiver = "8888@qq.com"

# 发送主题
subject = 'email by  python'

# 编写HTML类型的邮件正文（把HTML代码写进入）
msg = MIMEText('<html><body><a href="">百度一下</a></p></body></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# 连接发送邮件<strong><span style="color:#ff6666;">（smtplib模块基本使用格式）</span></strong>
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit() 