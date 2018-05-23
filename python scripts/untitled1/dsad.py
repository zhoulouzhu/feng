from time import sleep
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector('.s_ipt').send_keys('gouyang')
sleep(3)
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("shadiao")
sleep(3)
driver.find_element_by_id("su").click()