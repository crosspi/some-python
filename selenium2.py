import time

from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

url_the = 'https://tools.miku.ac/pornhub_logo'
aa = input('请输入白字:')
bb = input('请输入黑子:')
options = EdgeOptions()
options.use_chromium = True
# 浏览器的位置
s = Service(r"C:\Users\86138\AppData\Local\Programs\Python\Python310\msedgedriver.exe")
driver = Edge(options=options, service=s)
driver.set_window_size(1920, 1080)
driver.get(url=url_the)
a = driver.find_element(By.XPATH,
                        '//*[@id="__layout"]/div/main/div[1]/div[1]/div[3]/div/div[1]')
b = driver.find_element(By.XPATH,
                        '//*[@id="__layout"]/div/main/div[1]/div[1]/div[3]/div/div[2]')
a.clear()
b.clear()
a.send_keys(aa)
b.send_keys(bb)
buttons = driver.find_element(By.XPATH,
                              '//*[@id="__layout"]/div/main/div[1]/div[1]/button')
buttons.click()
time.sleep(2)
driver.quit()
