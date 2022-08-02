import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class AddUser(unittest.TestCase):
    def test_add_user(self):
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
        driver.find_element(By.LINK_TEXT, 'Admin').click()
        driver.find_element(By.LINK_TEXT, 'Job').click()
        driver.find_element(By.LINK_TEXT, 'Employment Status').click()

        # Click Add
        edit = driver.find_element(By.ID, 'btnAdd')
        edit.click()
        time.sleep(3)

        # Click Add pay
        first_name = driver.find_element(By.ID, 'empStatus_name')
        first_name.clear()
        first_name.send_keys('setengah hari')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)       
        
     #validasi  
    def test_add_user_inputan_kosong(self):
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
        driver.find_element(By.LINK_TEXT, 'Admin').click()
        driver.find_element(By.LINK_TEXT, 'Job').click()
        driver.find_element(By.LINK_TEXT, 'Employment Status').click()

        # Click Add
        edit = driver.find_element(By.ID, 'btnAdd')
        edit.click()
        time.sleep(3)

        # Click Add Employee
        first_name = driver.find_element(By.ID, 'empStatus_name')
        first_name.clear()
        first_name.send_keys('')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)           

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Required")

        driver.close()

if __name__ == '__main__':
    unittest.main()