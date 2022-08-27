# Generated by Selenium IDE
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Test1:
    def setup_method(self, method):
        s = Service(r"C:\Users\86138\AppData\Local\Programs\Python\Python310\msedgedriver.exe")
        self.driver = webdriver.Edge(service=s)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_1(self):
        self.driver.get("http://ehall.xjtu.edu.cn/new/index.html?browser=no")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, ".amp-no-login-zh").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.NAME, "username").click()
        self.driver.find_element(By.NAME, "username").send_keys("2214111424")
        self.driver.find_element(By.NAME, "pwd").send_keys("Mwc11232003")
        self.driver.find_element(By.ID, "account_login").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.vars["win4161"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win4161"])
        self.driver.switch_to.frame(0)
        self.driver.find_element(By.ID, "12aa5b5d-3791-4a69-8fda-6e1768da4d97").click()
