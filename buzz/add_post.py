import unittest
from requests import delete
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class add_post(unittest.TestCase):
    def add_post(self):
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
        driver.find_element(By.LINK_TEXT, 'Buzz').click()
        
        # Click edit data
        search = driver.find_element(By.ID, 'createPost_content')
        search.clear()
        search.send_keys('Jumat berkah')
        time.sleep(1)

        # Click Save
        btn_cari = driver.find_element(By.ID, 'postSubmitBtn')
        btn_cari.click()
        time.sleep(2)       
        
        #hapus



        driver.close()

if __name__ == '__main__':
    unittest.main()