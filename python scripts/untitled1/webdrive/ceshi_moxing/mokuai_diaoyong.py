from  denglu_mokuai import *
driver=webdriver.Firefox()
driver.get("http://localhost/")
driver.implicitly_wait(10)
Login().user_login(driver)
Login().tuichu(driver)