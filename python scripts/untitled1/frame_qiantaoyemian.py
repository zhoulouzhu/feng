from selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Firefox()
abc=r"D:\123456\123.html"
driver.get(abc)
driver.switch_to.frame("search")
driver.find_element_by_css_selector("#query").send_keys("python")
sleep(3)
driver.find_element_by_css_selector("#stb").click()
sleep(3)
driver.quit()