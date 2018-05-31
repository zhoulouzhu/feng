from logom import id,xpath,window_size,swip_up,tap,yinshi,find_element,tap1
import time
import  datetime
from  time import sleep
#driver=driver()
from data  import  clear
clear()
sleep(4)
yinshi(20)
def login_qidongye(username,password):
    s=window_size()


    sleep(5)

    try:

        a = xpath("//android.widget.RelativeLayout[@index='0']")
    except Exception as rst:
        rst = 0
    else:
        rst = 1

        id("cn.sanfast.zhuoer.student:id/dialog_btn_cancel").click()




    try:
        b=xpath("//android.widget.LinearLayout[@index='0']")


    except Exception as  ret:
        rst=0
    else:
        rst= 1
        tap1()
        tap1()
        tap1()

        #id("com.android.packageinstaller:id/permission_allow_button").click()
        #id("com.android.packageinstaller:id/permission_allow_button").click()
        #id("com.android.packageinstaller:id/permission_allow_button").click()
    swip_up()
    sleep(2)

    swip_up()
    sleep(2)
    swip_up()
    sleep(2)
    #xpath("//android.widget.TextView[@text='进入主页']").click()
    #find_element("cn.sanfast.zhuoer.student:id/enter",20)

    tap()
    id("cn.sanfast.zhuoer.student:id/main_shopping").click()
    id("cn.sanfast.zhuoer.student:id/main_share").click()
    id("cn.sanfast.zhuoer.student:id/et_phone").click()
    id("cn.sanfast.zhuoer.student:id/et_phone").send_keys(username)
    id("cn.sanfast.zhuoer.student:id/et_password").send_keys(password)
    id("cn.sanfast.zhuoer.student:id/btn_login").click()
    #return login1(username,password)
login1(13052821327,123456)

