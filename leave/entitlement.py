from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class entitlement(unittest.TestCase):

    #validasi add
    def test_add_inputan_kosong(self):
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

        # entitlement Link Click
        driver.find_element(By.LINK_TEXT, 'Leave').click()
        driver.find_element(By.LINK_TEXT, 'Entitlements').click()
        driver.find_element(By.LINK_TEXT, 'Add Entitlements').click()

       
        # Click Add entitlement
        emloyname_name = driver.find_element(By.ID, 'entitlements_employee_empName')
        emloyname_name.clear()
        emloyname_name.send_keys('')
        time.sleep(1)
  

        entitlement = driver.find_element(By.NAME, 'entitlements[entitlement]')
        entitlement.clear()
        entitlement.send_keys('')

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)       
        
        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Required")   
    
     #add data
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

        # entitlement Link Click
        driver.find_element(By.LINK_TEXT, 'Leave').click()
        driver.find_element(By.LINK_TEXT, 'Entitlements').click()
        driver.find_element(By.LINK_TEXT, 'Add Entitlements').click()

       
        # Click Add entitlement
        emloyname_name = driver.find_element(By.ID, 'entitlements_employee_empName')
        emloyname_name.clear()
        emloyname_name.send_keys('Ananya Dash')
        time.sleep(1)

        leave_type = driver.find_element(By.ID, 'entitlements_leave_type')
        
        leave_type.send_keys('CAN - Bereavement')
        time.sleep(1)

        leave_period = driver.find_element(By.CLASS_NAME, 'valid')
        leave_period.send_keys('2020-01-01 - 2020-12-31')
        time.sleep(1)
  

        entitlement = driver.find_element(By.NAME, 'entitlements[entitlement]')
       
        entitlement.send_keys('10')

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)   

       
    
        driver.close()

if __name__ == '__main__':
    unittest.main()
