from  time import  sleep
from  zuoer.logom import id,xpath,key_input,yinshi,xpaths,tap1,key
from log import log
def bus_car_ticket(username,id_num):
    log("创建快捷方式")
    yinshi(10)
    try:
        id("android:id/button1").click()
    except:
        print("创建失败")
    sleep(4)
    #tap1()
    log("update")
    key(4)
    log("bus ticker")
    try:
        id("com.mqunar.atom.alexhome:id/atom_alexhome_mod_bus_ticket").click()
    except:
        print("未点击汽车票")
    sleep(4)
    id("com.mqunar.atom.bus:id/atom_bus_tv_dep_city").click()
    id("com.mqunar.patch:id/pub_pat_title_etSearch").click()
    id("com.mqunar.patch:id/pub_pat_title_etSearch").send_keys("苏州")
    print(id("com.mqunar.patch:id/pub_pat_title_etSearch").text)
    id("com.mqunar.patch:id/pub_pat_title_btnSearch").click()
    # 输入起始地址
    id("com.mqunar.atom.bus:id/atom_bus_tv_arr_city").click()

    id("com.mqunar.patch:id/pub_pat_title_etSearch").click()
    id("com.mqunar.patch:id/pub_pat_title_etSearch").send_keys("盐城")
    print(id("com.mqunar.patch:id/pub_pat_title_etSearch").text)
    id("com.mqunar.patch:id/pub_pat_title_btnSearch").click()
    xpath("//android.widget.Button[@text='搜  索']").click()
    sleep(4)
    for i in range(2):
        id("com.mqunar.atom.bus:id/atom_bus_tv_next").click()
        print(i)
    log("车次列表")
    list=xpaths("//android.widget.LinearLayout[@index='5']")
    list.pop(1).click()
    log("汽车票预订")
    sleep(4)

    #name("汽车票预订").click()
    log("订票人姓名")
    sleep(4)
    id('com.mqunar.atom.bus:id/et_passenger_name').clear()



    id("com.mqunar.atom.bus:id/et_passenger_name").send_keys(username)
    sleep(4)
    id('com.mqunar.atom.bus:id/et_passenger_card').clear()


    id("com.mqunar.atom.bus:id/et_passenger_card").send_keys(id_num)
bus_car_ticket("zhoulouzhu", "123456")


