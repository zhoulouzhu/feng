from calculator import *
from  start_end import *


class Test_add(Setup_tearDown):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)

    def test_add1(self):
        j=Math(7,7)
        self.assertEqual(j.add(),14)