from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class employee_record(unittest.TestCase):
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
        driver.find_element(By.LINK_TEXT, 'Employee Records').click()

        # Click Add employee
        emloyname_name = driver.find_element(By.ID, 'attendance_employeeName_empName')
        emloyname_name.clear()
        emloyname_name.send_keys('Ananya Dash')
        time.sleep(1)

        from_date = driver.find_element(By.ID, 'attendance_date')
        from_date.clear()
        from_date.send_keys('2022-08-03')

       
        # Click Save
        save = driver.find_element(By.ID, 'btView')
        save.click()
        time.sleep(2)       
        
      #validasi  
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
        driver.find_element(By.LINK_TEXT, 'Employee Records').click()

        # Click Add employee
        emloyname_name = driver.find_element(By.ID, 'attendance_employeeName_empName')
        emloyname_name.clear()
        emloyname_name.send_keys('Ananya Dash')
        time.sleep(1)

        from_date = driver.find_element(By.ID, 'attendance_date')
        from_date.clear()
        from_date.send_keys('')

       
        # Click Save
        save = driver.find_element(By.ID, 'btView')
        save.click()
        time.sleep(2) 

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Should be a valid date in yyyy-mm-dd format")
        driver.close()

if __name__ == '__main__':
    unittest.main()
