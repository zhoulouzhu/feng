from selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as gy
from  selenium.webdriver.common.by import By
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#element=WebDriverWait(driver,5,0.5).until(gy.presence_of_element_located((By.__class__,"soutu-btn")))
#element.click()
sleep(3)
driver.find_element_by_css_selector(".soutu-btn").click()
sleep(3)
driver.find_element_by_css_selector(".upload-pic").send_keys(r"D:\123456\140.jpg")
sleep(3)
#driver.quit()