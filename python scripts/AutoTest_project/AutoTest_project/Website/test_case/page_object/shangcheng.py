from Basepage import  *
from selenium.webdriver.common.by import By

class shangcheng(page):
    url='/shop/'

    shangcheng = (By.LINK_TEXT, '网上商城')
    xiangji = (By.LINK_TEXT,'柯达数码相机C713')



    def type_shangcheng(self):

        self.find_element(*self.shangcheng).click()
    def type_xiangji(self):
        self.find_element(*self.xiangji).click()
    def shangcheng_action(self):
        self.open()
        self.type_shangcheng()
        self.type_xiangji()

    shangcheng_loc=(By.LINK_TEXT,"加入购物车")

    def shangcheng_pass_hit(self):

        return  self.find_element(*self.shangcheng_loc).text



