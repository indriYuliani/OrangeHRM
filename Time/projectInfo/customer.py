from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class customer(unittest.TestCase):
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
        driver.find_element(By.LINK_TEXT, 'Customers').click()

         #btn add
        btnadd = driver.find_element(By.CSS_SELECTOR, '#btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add customer
        customer = driver.find_element(By.ID, 'addCustomer_customerName')
        customer.clear()
        customer.send_keys('Ananya')
        time.sleep(1)

        deskripsi = driver.find_element(By.ID, 'addCustomer_description')
        deskripsi.clear()
        deskripsi.send_keys('ok')

       
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
        driver.find_element(By.LINK_TEXT, 'Customers').click()

          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)


        # Click Add customer
        customer = driver.find_element(By.ID, 'addCustomer_customerName')
        customer.clear()
        customer.send_keys('')
        time.sleep(1)

        deskripsi = driver.find_element(By.ID, 'addCustomer_description')
        deskripsi.clear()
        deskripsi.send_keys('ok')

       
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)       
        

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Required")

    def test_hapus(self):
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
        driver.find_element(By.LINK_TEXT, 'Customers').click()

          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)


        # Click Add customer
        customer = driver.find_element(By.ID, 'addCustomer_customerName')
        customer.clear()
        customer.send_keys('')
        time.sleep(1)

        
        

       
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)       



        driver.close()

if __name__ == '__main__':
    unittest.main()
