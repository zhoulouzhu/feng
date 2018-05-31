from  selenium import  webdriver
path="C:\Python36\chromedriver.exe"
mobile={"deviceName":"Apple iPhone 4"}
options =webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation",mobile)
driver = webdriver.Chrome(path,chrome_options=options)

driver.get("http://m.baidu.com")