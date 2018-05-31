#coding=utf-8

from appium import webdriver

from time import  sleep
#from data import clear
def driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = '8e649992 '
    desired_caps['appPackage'] = 'cn.sanfast.zhuoer.student'  #被测App的包名
    desired_caps['appActivity'] = 'cn.sanfast.zhuoer.student.activity.splash.SplashActivity' #启动时的Activity

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['newCommandTimeout'] = 7200
    desired_caps['noReset'] = True
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    return driver
driver=driver()
driver.implicitly_wait(20)

#print(driver.contexts)
#print(driver.context)
#for context in  driver.contexts:
    #print(context)
#driver.switch_to.context('WEBVIEW_1')

#driver.find_element_by_accessibility_id("唱山歌可以减肥？").click()

#driver.tap([(254,1088),500])


driver.find_element_by_xpath("//android.view.View[@content-desc=' 69 0 ']").click()
#driver.find_element_by_xpath("//android.view.View[@index='0']").click()
