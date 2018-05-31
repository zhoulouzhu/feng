from funct import read_excel
import requests
import  unittest
import HTMLTestReportCN
class v2exapi(unittest.TestCase):
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


if __name__ == '__main__':
    #unittest.main()
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(unittest.makeSuite(v2exapi))
    filepath = '' + 'report.html'

    # filepath='C:\\'+now+'.html'

    fp = open(filepath, 'wb')
    # 定义测试报告的标题与描述
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'测试报告')
    runner.run(suiteTest)
    fp.close()




#print(type(list1))