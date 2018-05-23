from calculator import *
from  start_end import *


class Test_sub(Setup_tearDown):
    def test_sub(self):
        i=Math(4,4)
        self.assertEqual(i.sub(),0)

    def test_sub1(self):
        i=Math(7,6)
        self.assertEqual(i.sub(),1)