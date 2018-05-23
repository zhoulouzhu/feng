from  selenium import webdriver
from time import  sleep
driver=webdriver.Firefox()
driver.get("https://www.baidu.com/s?cl=3&tn=baidutop10&fr=top1000&wd=%E7%BB%99%E8%80%81%E5%85%AC500%E7%AE%97%E5%AE%B6%E6%9A%B4&rsv_idx=2")
sleep(2)
js="var action=document.document.scrollTop=10000"
driver.execute_script(js)
sleep(2)
js="var action=document.document.scrollTop=0"
driver.execute_script(js)
sleep(3)
driver.quit()