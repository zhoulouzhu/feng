import unittest
class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1 start")

    def test_c(self):
        print("test_c")
    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("test end")
class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2 start")
    def test_e(self):
        print("test_e")
    def test_a(self):
        print("test_a")
    def tearDown(self):
        print("Test2 end")
if __name__ == '__main__':
    unittest.main()