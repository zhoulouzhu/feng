from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
driver=webdriver.Firefox()
driver.get("https://mail.qq.com/")
sleep(3)
driver.find_element_by_css_selector("div#inputOuter>input").send_keys("ssd")

'''driver.find_element_by_name("u").clear()
driver.find_element_by_name("u").send_keys("qdad")'''
