import  unittest
import   HTMLTestReportCN
import  time
from  funct import read_excel
from logom import jietu
import HTMLTestReportCN
import time
import unittest


from car import car_main, car2, car3, car4, car5,car6
username=read_excel("h.xlsx",0,0)
card=read_excel("h.xlsx",1,0)


class add(unittest.TestCase):


    def setUp(self):
        print("测试开始")

    def test_01(self):




        self.assertEqual(car_main(),"首页")
        jietu("狗蛋121.png")

        print("首页判断")

    def test_02(self):
        print("搜索判断")
        self.assertEqual(car2(),"搜索")
        jietu("121.png")


    def test_03(self):
        self.assertEqual(car3(),"后一天")
        jietu("124.png")

    def test_04(self):
        self.assertEqual(car4(), "预订")

    def test_05(self):
        self.assertEqual (car5(), "订单填写")
    def test_06(self):
        car6(username,card)

    def tearDown(self):
        print("测试结束")

if __name__=='__main__':
    suiteTest=unittest.TestSuite()
    '''suiteTest.addTest(add("test_01"))
    suiteTest.addTest(add("test_02"))
    suiteTest.addTest(add("test_03"))
    suiteTest.addTest(add("test_04"))
    suiteTest.addTest(add("test_05"))
    suiteTest.addTest(add("test_06"))'''
    #按顺序执行单个测试用例，若是承上启下脚本，需按顺序执行
    suiteTest.addTest(unittest.makeSuite(add))
    #执行整个类里的所有测试用例
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
   # suiteTest.addTest(unittest.makeSuite(add))
    filepath=''+now+'.html'

    #filepath='C:\\'+now+'.html'

    fp=open(filepath,'wb')
    #定义测试报告的标题与描述
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'测试报告')
    runner.run(suiteTest)
    fp.close()

