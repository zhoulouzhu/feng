#coding=utf-8

from appium import webdriver

from time import  sleep
#from data import clear
def driver():
    #driver(edition, device, port):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = '8e649992'
    desired_caps['appPackage'] = 'com.Qunar'  #被测App的包名
    desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity' #启动时的Activity

    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['newCommandTimeout'] = 7200
    desired_caps['noReset'] = True
    #url = 'http://localhost:'+port+'/wd/hub'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #driver=webdriver.Remote(url,desired_caps)
    return driver


#driver('8.0.0','d4fb35f2','4725')
#driver('7.0','8e649992','4723')

