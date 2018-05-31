from funct import read_excel
import requests
import  unittest
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

if __name__ == '__main__':
    unittest.main()


