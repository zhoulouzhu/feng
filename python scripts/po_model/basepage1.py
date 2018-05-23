class base (object):
    def  __init__(self,driver):


        self.driver=driver
  #      pass
    def by_id(self,id):
        return  self.driver.find_element_by_id(id)
