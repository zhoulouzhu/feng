from  selenium import  webdriver
from  time import  sleep
class Login():
    def user_login(self,driver,username,password):
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_class_name("inputSub").click()
        sleep(2)
        driver.refresh()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(3)
    def tuichu(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(2)
        driver.switch_to_alert().accept()
        sleep(3)
        driver.refresh()
        sleep(2)
if __name__=="__main__":
    driver=webdriver.Firefox()
    driver.get("http://localhost/")
    driver.implicitly_wait(10)



