from time import  sleep
from log import log
from  logom import key,id,xpaths,xpath,yinshi



def car_main():

    log("update")

    
    sleep(10)
    key(4)
    sleep(3)
    print(id("com.mqunar.atom.alexhome:id/atom_alexhome_textview").get_attribute("text"))
    sleep(3)
    return  id("com.mqunar.atom.alexhome:id/atom_alexhome_textview").get_attribute("text")

def car2():
    sleep(3)
    log("买汽车票")
    id("com.mqunar.atom.alexhome:id/atom_alexhome_mod_bus_ticket").click()
    sleep(3)
    return  xpath("//android.widget.Button[@text='搜  索']").get_attribute("text")

def car3():
    sleep(3)
    log("车次列表")
    id("com.mqunar.atom.bus:id/atom_bus_bt_search").click()
    log("汽车票预订")
    sleep(4)
    return  id("com.mqunar.atom.bus:id/atom_bus_tv_next").get_attribute("text")

def car4():
    sleep(3)
    log("车次详情")
    id("com.mqunar.atom.bus:id/atom_bus_tv_arr").click()
    #list=xpaths("//android.widget.RelativeLayout[@index='1']")
    #list.pop(4).click()

    return id("com.mqunar.atom.bus:id/atom_bus_tv_booking").get_attribute("text")
def car5():
    sleep(3)
    log("订单详情")
    id("com.mqunar.atom.bus:id/atom_bus_tv_booking").click()

    return  id("com.mqunar.atom.bus:id/atom_bus_order_tv_main_title").get_attribute("text")
def car6(username,card):
    sleep(3)
    id("com.mqunar.atom.bus:id/et_passenger_name").clear()
    id("com.mqunar.atom.bus:id/et_passenger_name").send_keys(username)
    id("com.mqunar.atom.bus:id/et_passenger_card").clear()
    id("com.mqunar.atom.bus:id/et_passenger_card").send_keys(card)







