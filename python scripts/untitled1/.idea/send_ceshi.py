import  unittest
from  BSTestRunner import  BSTestRunner
import  time
import  smtplib
from  email.mime.text import  MIMEText
from  email.header import  Header
import  os

def send_mail(latest_report):
    f=open(latest_report,"rb")
    mail_content=f.read()
    f.close()
    smtpserver="smtp.163.com"
    user = "zhoulouzhu@163.com"
    password="zlz123"
    sender="zhoulouzhu@163.com"
    receives=["zhoulouzhu@126.com","936791749@qq.com"]

    subject = "web 123"

    msg = MIMEText(mail_content,"html","utf-8")
    msg["subject"]=Header(subject,"utf-8")
    msg["from"]=sender
    msg["to"]=",".join(receives)

    smtp = smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send Email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send Email end!")


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print(("new report is :" + lists[-1]))

    file = os.path.join(report_dir, lists[-1])
    print(file)
    return file


if __name__ == '__main__':
    test_dir =r, './'
    report_dir = './'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = report_dir + '/' + now + 'result.html'

    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title="Test Report", description="baidu search")
        runner.run(discover)
    f.close()

    # h获取最新测试报告
    latest_report = latest_report(report_dir)
    # 发送邮件报告
    send_mail(latest_report)

