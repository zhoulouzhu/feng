#coding=utf-8
from model.function import insert_img
from appium import webdriver
#from appium.webdriver.mobilecommand import MobileCommand
from time import  sleep
#from data import clear
def driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'KWG5T16C26014368'
    desired_caps['appPackage'] = 'com.Qunar'  #被测App的包名
    desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity' #启动时的Activity
    desired_caps['noReset'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['newCommandTimeout'] = 7200
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    return driver

