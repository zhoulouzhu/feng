from selenium import webdriver
from time import sleep
import unittest
from HTMLTestRunner import  HTMLTestRunner
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class Baidu(unittest.TestCase):
    def setUp(self):
        self.drive=webdriver.Firefox()
        self.drive.implicitly_wait(10)
        self.base_url = "https://www.baidu.com/"


    def test_baidu_search(self):
        driver = self.drive
        driver.get(self.base_url)
        driver.find_element_by_name("wd").clear()
        driver.find_element_by_name("wd").send_keys("橙子")
        driver.find_element_by_id("su").click()
        sleep(3)

        title=driver.title
        self.assertEqual(title,"橙子_百度搜索")
        driver.find_element_by_partial_link_text("百度百科").click()
        sleep(5)
    def tearDown(self):
        self.drive.quit()



if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    fp = open('./2018-3-26.html', 'wb')

    runner = HTMLTestRunner(stream=fp, title='百度搜素', description='用例执行')
    runner.run(testunit)
    fp.close()

