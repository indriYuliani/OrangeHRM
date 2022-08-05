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


class employee_report(unittest.TestCase):
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
        driver.find_element(By.LINK_TEXT, 'Reports').click()
        driver.find_element(By.LINK_TEXT, 'Employee Reports').click()

        # Click configuration
        employee_name = driver.find_element(By.ID, 'employee_empName')
        employee_name.send_keys('Varmaa Rajeshh')

        project_name = driver.find_element(By.ID, 'time_project_name')
        project_name.send_keys('All')

        activity_name = driver.find_element(By.ID, 'time_activity_name')
        activity_name.send_keys('All')
        time.sleep(2)

        project_date_form = driver.find_element(By.ID, 'project_date_range_from_date')
        project_date_form.send_keys('2022-01-01')

        project_date_to = driver.find_element(By.ID, 'project_date_range_to_date')
        project_date_to.send_keys('2022-08-05')
        time.sleep(2)


        # Click Save
        btn_view= driver.find_element(By.ID, 'viewbutton')
        btn_view.click()
       
        #validasi 
        
        

        driver.close()

if __name__ == '__main__':
    unittest.main()
