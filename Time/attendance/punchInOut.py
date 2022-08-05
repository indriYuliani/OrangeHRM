from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class punchInOut(unittest.TestCase):
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
        driver.find_element(By.LINK_TEXT, 'Punch In/Out').click()

        # Click Add punch in
        date = driver.find_element(By.ID, 'attendance_date')
        date.clear()
        date.send_keys('2022-08-04')
       

        time = driver.find_element(By.ID, 'attendance_time')
        time.clear()
        time.send_keys('10:35')

        note = driver.find_element(By.ID, 'attendance_note')
        note.clear()
        note.send_keys('ok')
       
        # Click Save
        btn_in = driver.find_element(By.CSS_SELECTOR, '#btnPunch')
        btn_in.click()
             
        #Click add punch out
        date = driver.find_element(By.ID, 'attendance_date')
        date.send_keys('2022-08-04')
        

        time = driver.find_element(By.ID, 'attendance_time')
        time.send_keys('10:35')

        note = driver.find_element(By.ID, 'attendance_note')
        note.clear()
        note.send_keys('ok')
       
        # Click Save
        btn_in = driver.find_element(By.CSS_SELECTOR, '#btnPunch')
        btn_in.click()
       
    
        driver.close()

if __name__ == '__main__':
    unittest.main()
