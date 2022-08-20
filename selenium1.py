from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
import time
options = EdgeOptions()
options.use_chromium = True
# 浏览器的位置
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
driver = Edge(options=options,
              executable_path=r"C:\Users\86138\AppData\Local\Programs\Python\Python310\msedgedriver.exe")  # 相应的浏览器的驱动位置
driver.set_window_size(1920, 1080)
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('kw').submit()
time.sleep(2)

driver.quit()
