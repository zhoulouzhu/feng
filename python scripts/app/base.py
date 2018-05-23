#coding=utf-8
from appium import webdriver
from appium.webdriver.mobilecommand import MobileCommand
import time
import os
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.1'
desired_caps['deviceName'] = 'ce0817180c67606d0d7e'
desired_caps['appPackage'] = 'com.Qunar'  #被测App的包名
desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity' #启动时的Activity
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['newCommandTimeout'] = 7200
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
'''def sum(a,b):
    print(a+b)
sum(2,4)

def sum(a,b):
    return  a+b
print(sum(3,4))'''
def key(num):
    driver.keyevent(num)
'''str="aB"
print(str.upper())
print(str.lower())
dic={'a':29,
     'b': 30,}
print( dic.get('b'))'''
def char_to_num(str):
    switch={
        'a': 29,
        'b': 30,
        'c': 31,
        'd': 32,
        'e': 33,
        'f': 34,
        'g': 35,
        'h': 36,
        'i': 37,
        'j': 38,
        'k': 39,
        'l': 40,
        'm': 41,
        'n': 42,
        'o': 43,
        'p': 44,
        'q': 45,
        'r': 46,
        's': 47,
        't': 48,
        'u': 49,
        'v': 50,
        'w': 51,
        'x': 52,
        'y': 53,
        'z': 54,

    }
    return switch.get(str)
print(char_to_num('z'))
str='suzhou'

for i in  str:
    print(char_to_num(i))

