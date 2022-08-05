from ast import keyword
from importlib.metadata import distribution
import unittest
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class candidate(unittest.TestCase):

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
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()
        driver.find_element(By.LINK_TEXT, 'Vacancies').click()
        
          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add 
        job_title = driver.find_element(By.ID, 'addJobVacancy_jobTitle')
        job_title.send_keys('Chief Executive Officer')
        time.sleep(1)

        vacancy_name = driver.find_element(By.ID, 'addJobVacancy_name')
        vacancy_name.clear()
        vacancy_name.send_keys('andreas')
        time.sleep(1)

        hiring_manager = driver.find_element(By.ID, 'addJobVacancy_hiringManager')
        hiring_manager.clear()
        hiring_manager.send_keys('Ananya Dash')
        time.sleep(1)

        position = driver.find_element(By.ID, 'addJobVacancy_noOfPositions')
        position.clear()
        position.send_keys('1')
        time.sleep(1)

        deskripsi = driver.find_element(By.ID, 'addJobVacancy_description')
        deskripsi.send_keys('ok')
        time.sleep(1)

        
       
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)       
        
        # validasi salah satu kosong
    def test_add_inputan_salah_satu_kosong(self):
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
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()
        driver.find_element(By.LINK_TEXT, 'Vacancies').click()
        
          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add 
        job_title = driver.find_element(By.ID, 'addJobVacancy_jobTitle')
        job_title.send_keys('BTest')
        time.sleep(1)

        vacancy_name = driver.find_element(By.ID, 'addJobVacancy_name')
        vacancy_name.clear()
        vacancy_name.send_keys('')
        time.sleep(1)

        hiring_manager = driver.find_element(By.ID, 'addJobVacancy_hiringManager')
        hiring_manager.clear()
        hiring_manager.send_keys('Anthony Nolan')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Required")

        #pencarian
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
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()
        driver.find_element(By.LINK_TEXT, 'Vacancies').click()
        
        # Click cari
        cari = driver.find_element(By.ID, 'vacancySearch_jobTitle')
        cari.send_keys('Chief Financial Officer')
        time.sleep(1)

        # Click Search
        search = driver.find_element(By.ID, 'btnSrch')
        search.click()
        time.sleep(2)

        #validasi penarian
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
        driver.find_element(By.LINK_TEXT, 'Recruitment').click()
        driver.find_element(By.LINK_TEXT, 'Vacancies').click()
        
        # Click cari
        cari = driver.find_element(By.ID, 'vacancySearch_jobTitle')
        cari.send_keys('BTest')
        time.sleep(1)

        # Click Search
        search = driver.find_element(By.ID, 'btnSrch')
        search.click()
        time.sleep(2)

        response_data = driver.find_element(By.CSS_SELECTOR,'#resultTable > tbody > tr > td').text
        self.assertIn(response_data,'No Records Found')
        
        driver.close()

if __name__ == '__main__':
    unittest.main()
