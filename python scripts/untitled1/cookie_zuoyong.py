from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#huoqucookie
cookie=driver.get_cookies()
#dayin
#print(cookie)
#dayindiyizu
#print(cookie[0])
#添加cookie
driver.add_cookie({"name":"nidaye","value":"www.baidu.com"})
for cookie in  driver.get_cookies():
    print("%s---%s"%(cookie["name"],cookie["value"]))
driver.quit()