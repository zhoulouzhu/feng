import unittest
from model import function,myunit
from  LoginPage import *
from time import  sleep
from   shangcheng import *

class LoginTest(myunit.StartEnd):
    # @unittest.skip('skip this case')
    def test_login1_normal(self):
        '''username and passwd is normal'''
        print("test_login1_normal is start test...")
        po=LoginPage(self.driver)
        po.Login_action('狗杨123',"123456")
        sleep(5)

        self.assertEqual(po.type_loginPass_hint(),'我的空间')
        function.insert_img(self.driver,"狗杨121.jpg")
        print("test_login1_normal test end!")

    # @unittest.skip('skip this case')
    def test_login2_PasswdError(self):
        '''username is ok,passwd is error'''
        print("test_login2_passwdError is start test...")
        po=LoginPage(self.driver)
        po.Login_action('zxw',"3333")
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,"狗杨122.jpg")

    def test_login3_empty(self):
        '''username and passwd is empty'''
        print("test_login3_empty is start test...")
        po=LoginPage(self.driver)
        po.Login_action('','')
        sleep(2)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'狗杨123.jpg')
        print("test_login3_empty test end")




class shangchengtest(myunit.StartEnd):
    def test_shangcheng1(self):

        ''''''
        print("test4开始")
        po=shangcheng(self.driver)
        po.shangcheng_action()
        sleep(3)
        self.assertEqual(po.shangcheng_pass_hit(),'加入购物车')

        function.insert_img(self.driver,'shangcheng.jpg')
        print("test4结束")




if __name__ == '__main__':
    unittest.main()