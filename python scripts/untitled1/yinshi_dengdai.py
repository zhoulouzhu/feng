from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from  time import sleep,ctime

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(3)
driver.implicitly_wait(5)#隐式等待时间五秒
#检查搜索框是否存在
try:
     print(ctime())
     driver.find_element_by_css_selector("#kw").send_keys("gouyang")
     driver.find_element_by_css_selector("#su").click()
except NoSuchElementException as msg:
     print(msg)

finally:
     print(ctime())
sleep(3)
driver.quit()