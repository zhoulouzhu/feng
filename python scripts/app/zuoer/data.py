import  os
import time

def clear():
    os.popen('adb shell pm clear com.xiaomi.shop')

def start():
    os.popen("adb shell am start -n cn.sanfast.zhuoer.student/cn.sanfast.zhuoer.student.activity.splash.SplashActivity")

def stop():
    os.popen("adb shell am force-stop cn.sanfast.zhuoer.student")

