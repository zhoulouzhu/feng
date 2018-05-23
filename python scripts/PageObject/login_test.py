from  Loginpage import  *
from  selenium import  webdriver

driver=webdriver.Firefox()
username="狗杨123"
password="123456"
test_user_login(driver,username,password)

sleep(3)
driver.quit()