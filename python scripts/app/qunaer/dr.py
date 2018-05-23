#coding=utf-8
from appium import webdriver
from time import sleep
def driver():

    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'KWG5T16C26014368'
    desired_caps['appPackage'] = 'cn.sanfast.zhuoer.student'  #被测App的包名
    desired_caps['appActivity'] = 'cn.sanfast.zhuoer.student.activity.splash.SplashActivity' #启动时的Activity
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['newCommandTimeout'] = 7200
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return  driver
sleep(15)
driver=driver()
try:
    a = driver.find_element_by_xpath("//android.widget.FrameLayout[@index='0']")

except Exception as rst:
    rst=0
else:
    rst=1
    driver.find_element_by_id("cn.sanfast.zhuoer.student:id/dialog_btn_cancel").click()




driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").clear()
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").clear()
