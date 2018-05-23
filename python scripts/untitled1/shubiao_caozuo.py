from selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_css_selector("#kw").send_keys("gouyang")

#huoqusousuokuangyuansuduixiang
element=driver.find_element_by_css_selector("#kw")
sleep(3)
#shuangji
#ActionChains(driver).double_click(element).perform()
sleep(3)
#youjicaozuo
ActionChains(driver).double_click(element).perform()
sleep(3)
#shubiaoxuantin
above=driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(above).perform()
sleep(4)
driver.quit()