from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from h11 import Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class configuration(unittest.TestCase):
    def test_add(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # Admin Link Click
        driver.find_element(By.LINK_TEXT, 'Time').click()
        driver.find_element(By.LINK_TEXT, 'Attendance').click()
        driver.find_element(By.LINK_TEXT, 'Configuration').click()

        # Click configuration
        Data2 = driver.find_element(By.ID, 'attendance_configuration2')
        Data2.click()

        Data3 = driver.find_element(By.ID, 'attendance_configuration3')
        Data3.click()
       
        # Click Save
        btn_save= driver.find_element(By.ID, 'btnSave')
        btn_save.click()
       
    
        driver.close()

if __name__ == '__main__':
    unittest.main()
