import unittest
class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始﻿ε≡٩(๑>₃<)۶人丑就要多读书 ")
    @classmethod
    def tearDownClass(cls):
        print("测试结束 ஐ٩(๑´ᵕ`)۶ஐ:* 学习使我进步")
    def setUp(self):
        print("Test1 start")
    #@unittest.skipIf(4 > 3, "skip test_c")
    def test_c(self):
        print("test_c")
   # @unittest.skipUnless(2 < 1,"skip test_b")
    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("test end")
#@unittest.skip("skip--Test2")
class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2 start")
    def test_e(self):
        print("test_e")
   # @unittest.expectedFailure
    def test_a(self):
        print("test_a")
    def tearDown(self):
        print("Test2 end")
if __name__ == '__main__':
    unittest.main()