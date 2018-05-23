from time import  sleep
from selenium import webdriver

class page():
#初始化
    def __init__(self,driver):
        self.base_url="http://localhost/"
        self.driver=driver
        self.timeout=10
#打开不同的子页面
    def _open(self,url):
        url_=self.base_url+url
        print("Test page is: %s"%url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        assert  self.driver.current_url == url_ ,'did ont land on %s'%url_
    def  open(self):
        self._open(self.url)

    #元素定位方法封装
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
