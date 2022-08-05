from optparse import check_choice
from pydoc import describe
from tkinter import SCROLL
from tkinter.ttk import Scrollbar
import unittest
from xml.dom import DOMSTRING_SIZE_ERR
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class leave_list(unittest.TestCase):     
        
     #pencarian  
    def test_a_pencarian(self):
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

        # Leave Link Click
        driver.find_element(By.LINK_TEXT, 'Leave').click()
        driver.find_element(By.LINK_TEXT, 'Leave List').click()
        
        Employee = driver.find_element(By.ID, 'leaveList_txtEmployee_empName')
        Employee.clear()
        Employee.send_keys('Yashviitha chawak Yellapragoda')
        time.sleep(5) 

        # Click Save
        save = driver.find_element(By.ID, 'btnSearch')
        save.click()
        time.sleep(5)            


    # #edit 
    # def test_b_edit_list(self):
    #     base_url = 'https://opensource-demo.orangehrmlive.com/'
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     driver.maximize_window()
    #     driver.get(base_url)

    #     # Find Elements
    #     username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
    #     password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
    #     login_btn = driver.find_element(By.ID, 'btnLogin')

    #     # Login Action
    #     username.clear()
    #     username.send_keys('Admin')

    #     password.clear()
    #     password.send_keys('admin123')

    #     login_btn.click()

    #     # Leave Link Click
    #     driver.find_element(By.LINK_TEXT, 'Leave').click()
    #     driver.find_element(By.LINK_TEXT, 'Leave List').click()
        
        

    #     Employee = driver.find_element(By.CLASS_NAME, 'select_action quotaSelect')
    #     Employee.clear()
    #     Employee.send_keys('Cancel')
    #     time.sleep(5) 

    #     # Click Save
    #     save = driver.find_element(By.ID, 'btnSave')
    #     save.click()
    #     time.sleep(5)       


        driver.close()

if __name__ == '__main__':
    unittest.main()