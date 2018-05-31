from appium import   webdriver
from time import  sleep
def driver():
    desired_caps = {}

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.0'
    desired_caps['deviceName'] = 'KWG5T16C26014368'
    desired_caps['appPackage'] = 'com.android.chrome'
    desired_caps['appActivity'] = ''
    desired_caps['browserName'] ='Chrome'
    desired_caps['noRest'] = True
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['newCommandTimeout'] = 7200
    #driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
    return  driver
sleep(5)
driver=driver()
driver.get("https://m.baidu.com/")
driver.find_element_by_id("index-kw").click()
driver.find_element_by_id("index-kw").send_keys("123")