import time

from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

# from selenium.webdriver.support.relative_locator import with_tag_name

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
# password = driver.find_element(By.ID, "password")  # 通过id定位 密码输入框
# emailAddress = driver.find_element(with_tag_name("input").above(password))  # 通过相对定位定位邮箱地址输入框
# password = driver.find_element(with_tag_name("input").below(emailAddress))
# cancelButton = driver.find_element(with_tag_name("button").to_left_of(submitButton))
# submitButton = driver.find_element(with_tag_name("button").to_right_of(cancelButton))
# emailAddressField = driver.find_element(with_tag_name("input").near(emailAddressLabel))
