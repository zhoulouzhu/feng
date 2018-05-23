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
desired_caps['appPackage'] = 'com.Qunar'  #被测App的包名
desired_caps['appActivity'] = 'com.mqunar.splash.SplashActivity' #启动时的Activity
#desired_caps['noReset'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['newCommandTimeout'] = 7200
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
time.sleep(10)

#driver.find_element_by_id('android:id/button2').get_attribute()
#driver.keyevent(4)


try:
    a = driver.find_element_by_id("android:id/parentPanel")
except Exception as rst:
    rst=0
else:
    rst=1
    driver.keyevent(4)


#a=driver.find_element_by_id("android:id/parentPanel")





print(a)
    #driver.find_element_by_id("android:id/button2").click()
#判定是否创建快捷方式（否）
time.sleep(5)
s=driver.find_element_by_id('com.mqunar.atom.attemper:id/atom_atte_iv_close')
if s:

    driver.find_element_by_id("com.mqunar.atom.attemper:id/atom_atte_iv_close").click()
#是否更新（否）
time.sleep(5)
s=driver.find_elements_by_class_name('android.view.View')

#s.pop().click() classname定位方式之元素选取第一种
#s[0].click()  第二种

driver.find_element_by_id('com.mqunar.atom.alexhome:id/atom_alexhome_mod_bus_ticket').click()
#选择汽车票\船票
#driver.find_element_by_xpath().click()
driver.find_element_by_id('com.mqunar.atom.bus:id/atom_bus_tv_dep_city').click()
#选择起始地

driver.find_element_by_id('com.mqunar.patch:id/pub_pat_title_etSearch').send_keys("苏州")
def key(num):
    driver.keyevent(num)
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
#print(char_to_num('z'))
'''str='suzhou'

for i in  str:
    print(char_to_num(i))
driver.find_element_by_id('com.mqunar.patch:id/pub_pat_title_etSearch').click()
str='suzhou'
for i in  str:
    key(char_to_num(i))'''

#地址输入苏州
print(driver.find_element_by_id('com.mqunar.patch:id/pub_pat_title_etSearch').text)
driver.find_element_by_id('com.mqunar.patch:id/pub_pat_title_btnSearch').click()
#点击确定
driver.find_element_by_id('com.mqunar.atom.bus:id/atom_bus_tv_arr_city').click()
#地址中止地
driver.find_element_by_id('com.mqunar.patch:id/pub_pat_title_etSearch').send_keys('盐城')
#输入北京
print(driver.find_element_by_id('com.mqunar.patch:id/pub_pat_title_etSearch').text)
driver.find_element_by_id('com.mqunar.patch:id/pub_pat_title_btnSearch').click()
#点击确定
#driver.find_element_by_xpath("//android.widget.LinearLayout[@index='1']").click()
#driver.tap([(136,637)],500)
#driver.find_element_by_id('com.mqunar.atom.bus:id/atom_train_tv_calendar_header').send_keys(30)driver.find_element_by_
##选择日期
driver.find_element_by_id("com.mqunar.atom.bus:id/atom_bus_bt_search").click()
#点击搜索
for i in  range(2):
    driver.find_element_by_id("com.mqunar.atom.bus:id/atom_bus_tv_next").click()

    print(i)
sleep(5)
#选择后两天,在选择车次列表，选择后两天

#driver.find_elements_by_xpath("//android.widget.LinearLayout[@index='4']").


driver.find_element_by_id('com.mqunar.atom.bus:id/atom_bus_ll_line_item').click()

#选择车次
#driver.find_element_by_name(u"汽车票预定").click()
driver.find_element_by_id("com.mqunar.atom.bus:id/atom_bus_tv_booking").click()
#driver.find_element_by_class_name('android.widget.RelativeLayout').click()
#选择价格
driver.find_element_by_id('com.mqunar.atom.bus:id/et_passenger_name').clear()
driver.find_element_by_id('com.mqunar.atom.bus:id/et_passenger_name').send_keys("周楼柱")
#填写乘客姓名
driver.find_element_by_id('com.mqunar.atom.bus:id/et_passenger_card').clear()
driver.find_element_by_id('com.mqunar.atom.bus:id/et_passenger_card').send_keys('320921199310066416')
#填写身份证
driver.find_element_by_id("com.mqunar.atom.bus:id/atom_bus_order_et_ticket_phone").clear()
driver.find_element_by_id("com.mqunar.atom.bus:id/atom_bus_order_ib_ticket_phone_change").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='130 5282 1327']").click()

#传入手机号码
#driver.find_element_by_id("com.mqunar.atom.bus:id/atom_bus_order_et_ticket_phone").send_keys('13052821327')
# 由于传参时 输入的手机号老是错误，解决方法有两个，一个是添加断言后重新传参，但是还是会出错，所以使用第二个。
z=driver.get_window_size()
print(z['width'])
print(z["height"])

#driver.swipe(z['width']*0.3,z["height"]*0.7,z['width']*0.3,z["height"]*0.6,500)
#向上滑是表示x不变，y从大到小，向下相反，向左y不变，x从大变小，向右反之。
#driver.swipe(662,1160,662,1060)
#屏幕滑动，使用swipe方法，两个坐标移动来实现滑屏，既x轴不变，y轴从高变低，来实现'''

driver.find_element_by_id("com.mqunar.atom.bus:id/atom_bus_order_bottom_bt_submit").click()
#driver.install_app()//path 安装app
#print(driver.is_app_installed('com.Qunar'))检查app是否安装
#driver.tap([(909,871)],500) 用tap方法既x轴和y轴坐标定位点击位置（若ui界面改变则会报错）





