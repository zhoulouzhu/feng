from selenium import webdriver
from time import  sleep
from  denglu_mokuai import *
driver=webdriver.Firefox()
driver.get("http://localhost/")
driver.implicitly_wait(10)
Login().user_login(driver,"狗杨123","123456")
sleep(3)
Login().tuichu(driver)

Login().user_login(driver,"狗杨","123456")
sleep(3)
Login().tuichu(driver)