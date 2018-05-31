import  os
def clear():
    os.popen("adb shell pm clear com.xiaomi.shop")

def start():
    os.popen("adb shell am start -n com.xiaomi.shop/com.xiaomi.shop.activity.MainTabActivity ")

def stop():
    os.popen("adb shell am force_stop com.xiaomi.shop")