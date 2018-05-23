from  selenium import webdriver
from  selenium.webdriver.common.by import  By
from  time import  sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.implicitly_wait(5)

driver.find_element(By.ID,"kw").clear()
driver.find_element(By.NAME,"wd").send_keys("selenium")
driver.find_element(By.CLASS_NAME,"s_ipt").send_keys("我的")
driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("python")

sleep(3)
driver.find_element(By.ID,"su").click()
