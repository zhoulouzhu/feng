from  funct import read_excel
from logom import jietu
import HTMLTestReportCN
import time
import unittest
import requests




class add(unittest.TestCase):


    def setUp(self):
        print("测试开始")

    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"

        #querystring = {"name":"php"}
        a=read_excel("xx.xlsx",0,0)
        for node_name in a:
        #for node_name in ['php',"python","qna"]:


            response = requests.request("GET", url, params={"name":node_name}).json()
            self.assertEqual(response['name'],node_name)
            print(response)
    def test_nade_type(self):


        url = "https://www.apiopen.top/novelSearchApi"

        querystring = {"name": "%E7%9B%98%E9%BE%99"}

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "b249737d-aa24-4592-adf1-d19114f3f567"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)



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
    #now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
   # suiteTest.addTest(unittest.makeSuite(add))
    #filepath=''+now+'.html'
    filepath = '' + 'report.html'

    #filepath='C:\\'+now+'.html'

    fp=open(filepath,'wb')
    #定义测试报告的标题与描述
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'测试报告')
    runner.run(suiteTest)
    fp.close()