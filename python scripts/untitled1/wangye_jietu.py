from selenium import webdriver
from  time import  sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file(r"D:\123456\baidu.jpg")
sleep(3)
driver.quit()