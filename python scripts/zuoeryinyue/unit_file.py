import  unittest
import   HTMLTestReportCN
import  time
from  funct import  read_excel
import HTMLTestReportCN
import time
import unittest


from car import car_main, car2, car3, car4, car5,car6
if __name__=='__main__':
    suiteTest=unittest.TestSuite()
    test_dir=r"D:\python jiaoben\unit"
    testlist=unittest.defaultTestLoader.discover(test_dir,
                                                 pattern="unit*.py",
                                                 top_level_dir=None)
    #按文件名称执行脚本的方法，和按类，以及按封装单个脚本执行一样，都可以执行

    '''#按顺序执行单个测试用例，若是承上启下脚本，需按顺序执行
    suiteTest.addTest(unittest.makeSuite(add))
    #执行整个类里的所有测试用例
    
   # suiteTest.addTest(unittest.makeSuite(add))'''
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filepath=''+now+'.html'

    #filepath='C:\\'+now+'.html'

    fp=open(filepath,'wb')
    #定义测试报告的标题与描述
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'测试报告')
    runner.run(testlist)
    fp.close()
