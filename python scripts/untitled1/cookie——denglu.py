from selenium import  webdriver
from  time import  sleep
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.add_cookie({"name":"BAIDUID","value":"BAIDUID=59B377B148A5F78D7A5287EDC9CEA8A7:FG=1 "})
driver.add_cookie({"name":"BDUSS","value":"BDUSS=BHb3lkS2RZbmJmaE5sSUcyRDd1NGVWZUFJM2FxVENIdzNyY1NEOHhXN3J5Y1ZhQVFBQUFBJCQAAAAAAAAAAAEAAACUcCHAztLQxMDvztK8x7XDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOs8nlrrPJ5aVH"})
sleep(2)
driver.refresh()
sleep(3)
#driver.quit()