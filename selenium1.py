import time

from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

options = EdgeOptions()
options.use_chromium = True
# 浏览器的位置
s = Service(r"C:\Users\86138\AppData\Local\Programs\Python\Python310\msedgedriver.exe")
driver = Edge(options=options, service=s)
driver.maximize_window()
driver.get('https://www.baidu.com')
element = driver.find_element(By.ID, "kw")
element.send_keys("python")
driver.find_element(By.ID, 'kw').submit()
time.sleep(2)
driver.quit()
