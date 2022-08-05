from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class assign_leave(unittest.TestCase):
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
        driver.find_element(By.LINK_TEXT, 'Leave').click()
        driver.find_element(By.LINK_TEXT, 'Assign Leave').click()

        # Click Add
        edit = driver.find_element(By.ID, 'btnAdd')
        edit.click()
        time.sleep(3)

        # Click Add pay
        emloyname_name = driver.find_element(By.ID, 'assignleave_txtEmployee_empName')
        emloyname_name.clear()
        emloyname_name.send_keys('Peter Mac Anderson')
        time.sleep(1)

        leave_type = driver.find_element(By.ID, 'assignleave_txtLeaveType')
        leave_type.clear()
        leave_type.send_keys('CAN - Bereavement')
        time.sleep(1)

        from_date = driver.find_element(By.CLASS_NAME, 'calendar hasDatepicker validation-error')
        from_date.clear()
        from_date.send_keys('2022-08-03')

        to_date = driver.find_element(By.NAME, 'assignleave[txtToDate]')
        to_date.clear()
        to_date.send_keys('2022-08-03')

        duration = driver.find_element(By.ID, 'assignleave_duration_duration')
        duration.clear()
        duration.send_keys('Full Day')

        comment = driver.find_element(By.NAME, 'assignleave[txtComment]')
        comment.clear()
        comment.send_keys('ok')
        # Click Save
        save = driver.find_element(By.ID, 'assignBtn')
        save.click()
        time.sleep(2)       
        
      #validasi  
    def test_validasi_add_kosong(self):
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
        driver.find_element(By.LINK_TEXT, 'Leave').click()
        driver.find_element(By.LINK_TEXT, 'Assign Leave').click()

      
        # Click Add assign leave
        employname_name = driver.find_element(By.CSS_SELECTOR, '#assignleave_txtLeaveType')
        
        employname_name.send_keys('')
        time.sleep(1)

        leave_type = driver.find_element(By.ID, 'assignleave_txtLeaveType')
        leave_type.send_keys('')
        time.sleep(1)

        comment = driver.find_element(By.NAME, 'assignleave[txtComment]')
        comment.clear()
        comment.send_keys('')
        # Click Save
        save = driver.find_element(By.ID, 'assignBtn')
        save.click()
        time.sleep(2)            

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Required")
        driver.close()

if __name__ == '__main__':
    unittest.main()
