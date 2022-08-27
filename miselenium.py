import time

import pyautogui
from selenium.webdriver import Edge
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def try_until(the_element, the_name, the_driver, the_time):
    try:
        find_amp = WebDriverWait(the_driver, the_time).until(EC.presence_of_element_located((the_element, the_name)))
        find_amp.click()
        print(find_amp)
        return find_amp
    except IndexError:
        print(555)


username = ""
pwd = ""
url = "http://ehall.xjtu.edu.cn/new/index.html?browser=no"
# from selenium.webdriver.support.relative_locator import with_tag_name
time_begin = time.time()

options = EdgeOptions()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
options.use_chromium = True
# 浏览器的位置
s = Service(r"C:\Users\86138\AppData\Local\Programs\Python\Python310\msedgedriver.exe")
driver = Edge(options=options, service=s)
driver.maximize_window()
driver.get(url)
try_until(the_driver=driver, the_time=10, the_element=By.ID, the_name="ampHasNoLogin")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "username").send_keys(username)
driver.find_element(By.CLASS_NAME, "pwd").send_keys(pwd)
driver.find_element(By.ID, "account_login").click()
try_until(the_driver=driver, the_time=10, the_element=By.XPATH,
          the_name="/html/body/article[5]/section/div[2]/div[1]/div[2]/pc-card-html-5131446170220455-01/amp-w-frame/div/div[2]/div/div[1]/widget-app-item[1]/div/div/div[2]")
time.sleep(2)
pyautogui.click(961, 548, duration=2)
time.sleep(3)
driver.quit()
time_end = time.time()
print(f'耗时{int(time_end - time_begin)}s')
