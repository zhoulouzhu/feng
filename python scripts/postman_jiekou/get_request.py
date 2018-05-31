import requests
import unittest

class v2exapitestcase(unittest.TestCase):
    def test_node_api(self):


        url = "https://www.v2ex.com/api/topics/hot.json"
        querystring = {"name":"手机"}

        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "f1ded44c-67f5-4d87-9870-d8920fd98df9"
        }

        response = requests.request("GET", url, headers=headers,params=querystring).json()
        #self.assertEqual(response["name"],querystring["name"])

        print("response")


        print(response.text)
if __name__ == '__main__':
    unittest.main()