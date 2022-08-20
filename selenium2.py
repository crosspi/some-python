from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions
import time
url_the = 'https://tools.miku.ac/pornhub_logo'
aa = input('请输入白字:')
bb = input('请输入黑子:')
options = EdgeOptions()
options.use_chromium = True
# 浏览器的位置
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
driver = Edge(options=options,
              executable_path=r"C:\Users\86138\AppData\Local\Programs\Python\Python310\msedgedriver.exe")  # 相应的浏览器的驱动位置
driver.set_window_size(1920, 1080)
driver.get(url=url_the)
a = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div[1]/div[1]/div[3]/div/div[1]')
b = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div[1]/div[1]/div[3]/div/div[2]')
a.clear()
b.clear()
a.send_keys(aa)
b.send_keys(bb)
buttons = driver.find_element_by_xpath(
    '//*[@id="__layout"]/div/main/div[1]/div[1]/button').click()
time.sleep(2)
driver.quit()
