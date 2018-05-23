from  Basepage import *
from  selenium.webdriver.common.by import By


class loginpage(page):


    url="/"

    username_loc=(By.NAME,"username")
    password_loc=(By.NAME,"password")
    submit_loc=(By.NAME,"Submit")

    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

     # 登录按钮元素
        # 登录按钮元素
    def type_submit(self):
        self.find_element(*self.submit_loc).click()

    # 登录功能模块封装
def test_user_login(driver, username, password):
    login_page = loginpage(driver)
    login_page.open()

    login_page.type_username(username)
    login_page.type_password(password)
    login_page.type_submit()


