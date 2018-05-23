from  appium import  webdriver
import  time

def android_driver(self, i):
    capabilities = {
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "deviceName": "f6f1d085",
        "appPackage":"cn.com.open.503mooc",
        "appActivity": "cn.com.open.mocc.component.user.activity.login.MCLoginActivity"






    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    time.sleep(10)
    return driver
