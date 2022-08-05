from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class project(unittest.TestCase):
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
        driver.find_element(By.LINK_TEXT, 'Project Info').click()
        driver.find_element(By.LINK_TEXT, 'Projects').click()

         #btn add
        btnadd = driver.find_element(By.CSS_SELECTOR, '#btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add customer
        customer = driver.find_element(By.ID, 'addProject_customerName')
        customer.clear()
        customer.send_keys('Internal')
        time.sleep(1)

        nama = driver.find_element(By.ID, 'addProject_projectName')
        nama.clear()
        nama.send_keys('wiwi')

        project_admin = driver.find_element(By.ID, 'addProject_projectAdmin_1')
        project_admin.clear()
        project_admin.send_keys('')

        deskrisi = driver.find_element(By.ID, 'addProject_description')
        deskrisi.clear()
        deskrisi.send_keys('')
       
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)       
        
        #validasi  
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
  
        # Admin Link Click
        driver.find_element(By.LINK_TEXT, 'Time').click()
        driver.find_element(By.LINK_TEXT, 'Project Info').click()
        driver.find_element(By.LINK_TEXT, 'Projects').click()

        #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)


        # Click Add customer
        customer = driver.find_element(By.ID, 'addProject_customerName')
        customer.clear()
        customer.send_keys('')
        time.sleep(1)

        nama = driver.find_element(By.ID, 'addProject_projectName')
        nama.clear()
        nama.send_keys('')

        project_admin = driver.find_element(By.ID, 'addProject_projectAdmin_1')
        project_admin.clear()
        project_admin.send_keys('')

        deskrisi = driver.find_element(By.ID, 'addProject_description')
        deskrisi.clear()
        deskrisi.send_keys('ok')
        time.sleep(3)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2) 

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Required")


        #Pencarian
    def test_pencarian(self):
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
        driver.find_element(By.LINK_TEXT, 'Project Info').click()
        driver.find_element(By.LINK_TEXT, 'Projects').click()

         # Click pencarian customer
        customer = driver.find_element(By.ID, 'searchProject_customer')
        customer.clear()
        customer.send_keys('internal')
        time.sleep(1)
        
        # Click cari
        save = driver.find_element(By.ID, 'btnSearch')
        save.click()
        time.sleep(2) 

        #delete
    def test_pencarian(self):
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
        driver.find_element(By.LINK_TEXT, 'Project Info').click()
        driver.find_element(By.LINK_TEXT, 'Projects').click()

         # Click pencarian customer
        customer_delete = driver.find_element(By.ID, 'ohrmList_chkSelectAll')
        customer_delete.click()
        time.sleep(1)
        
        # Click cari
        delete = driver.find_element(By.ID, 'btnDelete')
        delete.click()
        time.sleep(2) 

        konfirmasi_delete = driver.find_element(By.ID, 'dialogDeleteBtn')
        konfirmasi_delete.click()
        time.sleep(1)

        driver.close()

if __name__ == '__main__':
    unittest.main()
