from tets1 import driver
from app.tets1 import driver
from time import  sleep
from appium import  webdriver
driver=driver()


def id(id):
    sleep(4)
    return  driver.find_element_by_id(id)


def xpath(x):
    sleep(4)

    #    driver.find_element_by_id(id).click()
    return driver.find_element_by_xpath(x)

def id_val(id,value):
    sleep(4)
    return  driver.find_element_by_id(id).send_keys(value)

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
       # key_input(zimu_to_shuzi(i))
print(zimu_to_shuzi('z'))

def windows_size():
    return driver.get_window_size()

def swip_up():
    s=windows_size()
    driver.swipe(s['width']*0.3,s['height']*0.7,s['width']*0.3,s['height']*0.6,500)

