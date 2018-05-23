#coding=utf-8
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
from  time import sleep
import time

import os
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'KWG5T16C26014368'
desired_caps['appPackage'] = 'com.xiaomi.shop'  #被测App的包名
desired_caps['appActivity'] = 'com.xiaomi.shop.activity.MainTabActivity' #启动时的Activity
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['newCommandTimeout'] = 7200
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
time.sleep(10)
#os.popen("adb shell am start -n com.xiaomi.shop/com.xiaomi.shop.activity.MainTabActivity ")


a =driver.find_element_by_xpath("//android.widget.LinearLayout[@index='0']")
if a:
    driver.keyevent(4)
driver.find_element_by_id("com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_username").click()
driver.find_element_by_id("com.xiaomi.shop:id/et_account_name").click()
driver.find_element_by_id("com.xiaomi.shop:id/et_account_name").clear()
driver.find_element_by_id("com.xiaomi.shop:id/et_account_name").send_keys("13311483570")
driver.find_element_by_id("com.xiaomi.shop:id/et_account_password").click()
driver.find_element_by_id("com.xiaomi.shop:id/et_account_password").clear()
driver.find_element_by_id("com.xiaomi.shop:id/et_account_password").send_keys("12552163wjj")
driver.find_element_by_id("com.xiaomi.shop:id/btn_login").click()
