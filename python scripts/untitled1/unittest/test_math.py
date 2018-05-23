import unittest

from test_project.calculator import *


class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")
    def test_add(self):
        j=Math(5,10)
        #self.assertEqual(j.add(),15)
        self.assertEqual(j.add(),12)
    def test_add1(self):
        j=Math(5,10)
        self.assertNotEqual(j.add(),12)

    def add_test2(self):
        j = Math(5, 10)
        self.assertTrue(j.add() >10)
    def add_test3(self):
        j=Math("goudan",15)
        self.assertIs("goudan","goudan")
    def add_test4(self):

        self.assertIn("888", "888,ssd ")
        #self.assertIn("888","888")
    def abc(self):
        a=2

        self.assertIsInstance("a","int")

    def assertIn_test(self):
        self.assertIn("888", "888,gouyu")

    def tearDown(self):
        print("test end")

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(TestMath("abc"))


    runer=unittest.TextTestRunner()
    runer.run(suite)