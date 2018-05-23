import basepage1
class loginpage(basepage1.base):
    def input(self):
        self.base.by_id("kw").send_keys("test")