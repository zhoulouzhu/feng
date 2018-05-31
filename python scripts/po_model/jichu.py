from selenium import webdriver


def driver():
    driver=webdriver.Firefox()
    return  driver
driver=driver()
driver.get("http://www.baidu.com")