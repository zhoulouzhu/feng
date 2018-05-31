from ddr import driver
from time import sleep
from  function import insert_img
from appium import webdriver
import datetime
driver=driver()
s=driver.get_window_size()
def id(id):
    sleep(3)
    return  driver.find_element_by_id(id)
def name(x):
    sleep(3)
    return  driver.find_element_by_name(x)
def jietu(name):
    sleep(3)
    return  insert_img(driver,name)



def by_class(x):
    element = driver.find_element_by_class_name(x)
    print(element)
    elements = driver.find_element_by_class_name(x)
    elements[1].click()
    element.click()
def yinshi(time):

    return  driver.implicitly_wait(time)
def xpath(xpath):

    return driver.find_element_by_xpath(xpath)
def xpaths(x):

    return driver.find_elements_by_xpath(x)
def window_size():
    return  driver.get_window_size()
def  id_val(id,value):
    sleep(4)
    return  driver.find_element_by_id(id).send_keys(value)
def swip_up():

    driver.swipe(s['width'] * 0.8, s['height'] * 0.6, s['width'] * 0.01, s['height'] * 0.6, 500)
def tap():
    m=s['width']*0.531
    n=s['height'] * 0.822
    driver.tap([(m, n)], 500)
#卓儿音乐app，引导页滑动过后出现的点击按钮，点击一下
def tap1():
    m=s['width']*0.732
    n=s['height']*0.951
    driver.tap([(m,n)],500)
    sleep(2)

#卓儿音乐app，引导页之前的同意或拒绝权限按钮，点击一下
  #driver.tap(s, n, 500)
  #driver.tap([(573, 1475)], 500)
def key(x):
    return driver.keyevent(x)

def zimu_to_shuzi(str):
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
        'z': 54
    }
    return switch.get(str)
def key_input(str):
    for i in  str:
        print(i)
        driver.keyevent(zimu_to_shuzi(i))
def  find_element(str,time):
    time1=datetime.datetime.now()
    tag=False
    while not tag:
        time2=datetime.datetime.now()
        if(time2-time1).seconds<time:
            try:
                driver.find_element_by_id(str).click()
                print ('click ok')
                tag=True
            except:
                print ('not find')
        else:
            break

#find_element('com.mqunar.atom.attemper:id/atom_atte_iv_close',20)