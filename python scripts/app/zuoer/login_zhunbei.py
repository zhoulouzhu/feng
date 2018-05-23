
#coding=utf-8

from time import sleep

from appium import webdriver

from data import clear


def logom(username,passwrod):
    clear()
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'KWG5T16C26014368'
    desired_caps['appPackage'] = 'cn.sanfast.zhuoer.student'  # 被测App的包名
    desired_caps['appActivity'] = 'cn.sanfast.zhuoer.student.activity.splash.SplashActivity'  # 启动时的Activity
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['newCommandTimeout'] = 7200
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(5)
    driver.implicitly_wait(5)

    a=driver.find_element_by_xpath("//android.widget.FrameLayout[@index='0']")
    if a:
        driver.find_element_by_id("cn.sanfast.zhuoer.student:id/dialog_btn_cancel").click()

    b=driver.find_element_by_xpath("//android.widget.FrameLayout[@index='0']")
    if b:
        driver.find_element_by_id("android:id/button1").click()
        driver.find_element_by_id("android:id/button1").click()
        driver.find_element_by_id("android:id/button1").click()

    s=driver.get_window_size()

    driver.swipe(s['width'] * 0.8, s['height'] * 0.6, s['width'] * 0.01, s['height'] * 0.6, 500)
    driver.swipe(s['width'] * 0.8, s['height'] * 0.6, s['width'] * 0.01, s['height'] * 0.6, 500)
    driver.swipe(s['width'] * 0.8, s['height'] * 0.6, s['width'] * 0.01, s['height'] * 0.6, 500)
    driver.tap([(593,1555)],500)
    driver.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()
    driver.find_element_by_id("cn.sanfast.zhuoer.student:id/et_phone").click()
    driver.find_element_by_id("cn.sanfast.zhuoer.student:id/et_phone").send_keys("13052821327")
    driver.find_element_by_id("cn.sanfast.zhuoer.student:id/et_password").click()
    driver.find_element_by_id("cn.sanfast.zhuoer.student:id/et_password").send_keys("123456")
    driver.find_element_by_id("cn.sanfast.zhuoer.student:id/btn_login").click()



