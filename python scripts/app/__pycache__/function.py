from com.dr import driver
from com.com_app import clear
import time

clear()
time.sleep(3)
driver=driver()

time.sleep(10)
def key(num):
    driver.keyevent(num)

key(4)



def id(id):
    time.sleep(4)
#    driver.find_element_by_id(id).click()
    return driver.find_element_by_id(id)

def xpath(x):
    sleep(2)
    return driver.find_element_by_xpath(x)
def xpath_val(x,value):
    sleep(2)
    return driver.find_element_by_xpath(x).send_keys(value)

def sleep(num):
    time.sleep(num)

def login(user,passwd):
    #start()
    #print 'start app'
    time.sleep(10)
    print 'begin'
    id('com.xiaomi.shop.plugin.homepage:id/main_bottom_tab_mine_text').click()
    id('com.xiaomi.shop.plugin.homepage:id/usercentral_listheader_username').click()
    id("com.xiaomi.shop:id/et_account_name").send_keys(user)
    id('com.xiaomi.shop:id/et_account_password').send_keys(passwd)
    id('com.xiaomi.shop:id/btn_login').click()

def char_to_num(str):
    switch={
        'a':29,
        'b':30,
        'c':31,
        'd':32,
        'e':33,
        'f':34,
        'g':35,
        'h':36,
        'i':37,
        'j':38,
        'k':39,
        'l':40,
        'm':41,
        'n':42,
        'o':43,
        'p':44,
        'q':45,
        'r':46,
        's':47,
        't':48,
        'u':49 ,
        'v':50,
        'w':51,
        'x':52,
        'y':53,
        'z':54

    }
    return switch.get(str)

def key_input(str):
    for i in str:
        print i
        driver.keyevent(char_to_num(i))

def window_size():
    return driver.get_window_size()

def swipe_up():
    s=window_size()
    driver.swipe(s['width']*0.3,s['height']*0.7,s['width']*0.3,s['height']*0.3,500)




