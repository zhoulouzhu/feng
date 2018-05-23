from selenium import  webdriver
from  selenium.webdriver.common.keys import Keys
from time import  sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("python")
sleep(3)

driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"a")

driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"c")
driver.get("https://www.sogou.com/")
sleep(2)
driver.find_element_by_css_selector("#query").send_keys(Keys.CONTROL,"v")
sleep(3)

driver.find_element_by_css_selector("#stb").click()
sleep(3)
driver.quit()