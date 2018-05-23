from logom import id,xpath,window_size,swip_up,tap,yinshi,find_element,tap1,by_class
import time
import  datetime
from  time import sleep
#driver=driver()
from data  import  clear
clear()
sleep(4)
yinshi(20)
def login_ddenglu(username,password):
    s=window_size()


    sleep(5)
    id("cn.sanfast.zhuoer.student:id/main_shopping").click()
    id("cn.sanfast.zhuoer.student:id/main_share").click()
    id("cn.sanfast.zhuoer.student:id/et_phone").click()
    id("cn.sanfast.zhuoer.student:id/et_phone").send_keys(username)
    id("cn.sanfast.zhuoer.student:id/et_password").send_keys(password)
    id("cn.sanfast.zhuoer.student:id/btn_login").click()
    id("cn.sanfast.zhuoer.student:id/main_share").click()
    by_class("android.widget.TextView")
    # return login1(username,password)


login_ddenglu(13052821327, 123456)