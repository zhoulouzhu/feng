from selenium import  webdriver



from  time import  sleep
driver=webdriver.Firefox()

driver.get("http://www.51zxw.net/list.aspx?cid=615")
selenium_index=driver.current_window_handle
sleep(3)
driver.find_element_by_partial_link_text('2-1').click()
sleep(3)
driver.switch_to.window(selenium_index)
sleep(3)
driver.find_element_by_partial_link_text("3-1").click()
sleep(3)
driver.quit()
