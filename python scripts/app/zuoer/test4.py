from logom import key,xpaths,id,xpath
from time import sleep
sleep(10)
#key(4)

key(4)
id("com.mqunar.atom.alexhome:id/atom_alexhome_mod_bus_ticket").click()
id("com.mqunar.atom.bus:id/atom_bus_bt_search").click()
#xpath("//android.widget.Button[@text='搜  索']").click()
id("com.mqunar.atom.bus:id/atom_bus_tv_arr").click()
id("com.mqunar.atom.bus:id/atom_bus_tv_booking").click()
id("com.mqunar.atom.bus:id/et_passenger_name").clear()
id("com.mqunar.atom.bus:id/et_passenger_name").send_keys(username)
id("com.mqunar.atom.bus:id/et_passenger_card").clear()
id("com.mqunar.atom.bus:id/et_passenger_card").send_keys(card)
