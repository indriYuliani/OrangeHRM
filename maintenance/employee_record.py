import unittest
from requests import delete
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class employee_record(unittest.TestCase):
    def employee_record(self):
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
        driver.find_element(By.LINK_TEXT, 'Maintenance').click()
        driver.find_element(By.LINK_TEXT, 'Purge Records').click()
        driver.find_element(By.LINK_TEXT, 'Employee Records').click()
        
        # Click 
        verify_pwd = driver.find_element(By.ID, 'confirm_password')
        verify_pwd.clear()
        verify_pwd.send_keys('admin123')
        time.sleep(1)

        # Click Save
        btn_verify = driver.find_element(By.CSS_SELECTOR, '#frmPurgeEmployeeAuthenticate > div > div > input[type=submit]')
        btn_verify.click()
        time.sleep(2)       
        
        #validasi
        def inputan_kosong(self):
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
        driver.find_element(By.LINK_TEXT, 'Maintenance').click()
        driver.find_element(By.LINK_TEXT, 'Purge Records').click()
        driver.find_element(By.LINK_TEXT, 'Employee Records').click()
        
        # Click 
        verify_pwd = driver.find_element(By.ID, 'confirm_password')
        verify_pwd.clear()
        verify_pwd.send_keys('')
        time.sleep(1)

        # Click Save
        btn_verify = driver.find_element(By.CSS_SELECTOR, '#frmPurgeEmployeeAuthenticate > div > div > input[type=submit]')
        btn_verify.click()
        time.sleep(2)         

        respon_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(respon_data,'Required')


        driver.close()

if __name__ == '__main__':
    unittest.main()