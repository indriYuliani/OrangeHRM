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
        driver.find_element(By.LINK_TEXT, 'Candidates').click()
        
          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add 
        first_name = driver.find_element(By.ID, 'addCandidate_firstName')
        first_name.clear()
        first_name.send_keys('Andreas')
        time.sleep(1)

        last_name = driver.find_element(By.ID, 'addCandidate_lastName')
        last_name.clear()
        last_name.send_keys('sigit')
        time.sleep(1)

        email = driver.find_element(By.ID, 'addCandidate_email')
        email.clear()
        email.send_keys('sigit@gmail.com')
        time.sleep(1)

        contact = driver.find_element(By.ID, 'addCandidate_contactNo')
        contact.clear()
        contact.send_keys('0857171760090')
        time.sleep(1)

        job_vacancy = driver.find_element(By.ID, 'addCandidate_vacancy')
        job_vacancy.send_keys('Senior QA Lead')
        time.sleep(1)

        keyword = driver.find_element(By.ID, 'addCandidate_keyWords')
        keyword.clear()
        keyword.send_keys('qa')
        time.sleep(1)

        coment = driver.find_element(By.ID, 'addCandidate_comment')
        coment.clear()
        coment.send_keys('oke')
        time.sleep(1)

        date = driver.find_element(By.ID, 'addCandidate_appliedDate')
        date.clear()
        date.send_keys('2022-08-03')
        time.sleep(1)
       
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)       
        
      #validasi  
    def test_add_inputan_all_kosong(self):
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
        driver.find_element(By.LINK_TEXT, 'Candidates').click()
        
          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add 
        first_name = driver.find_element(By.ID, 'addCandidate_firstName')
        first_name.clear()
        first_name.send_keys('')
        time.sleep(1)

        last_name = driver.find_element(By.ID, 'addCandidate_lastName')
        last_name.clear()
        last_name.send_keys('')
        time.sleep(1)

        email = driver.find_element(By.ID, 'addCandidate_email')
        email.clear()
        email.send_keys('')
        time.sleep(1)
    
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2) 

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Required")

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
        driver.find_element(By.LINK_TEXT, 'Candidates').click()
        
          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add 
        first_name = driver.find_element(By.ID, 'addCandidate_firstName')
        first_name.clear()
        first_name.send_keys('gabriela')
        time.sleep(1)

        last_name = driver.find_element(By.ID, 'addCandidate_lastName')
        last_name.clear()
        last_name.send_keys('')
        time.sleep(1)

        email = driver.find_element(By.ID, 'addCandidate_email')
        email.clear()
        email.send_keys('gabriella@gmail.com')
        time.sleep(1)
    
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2) 

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Required")

        #validasi format email
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
        driver.find_element(By.LINK_TEXT, 'Candidates').click()
        
          #btn add
        btnadd = driver.find_element(By.ID, 'btnAdd')
        btnadd.click()
        time.sleep(3)

        # Click Add 
        first_name = driver.find_element(By.ID, 'addCandidate_firstName')
        first_name.clear()
        first_name.send_keys('elisabeth')
        time.sleep(1)

        last_name = driver.find_element(By.ID, 'addCandidate_lastName')
        last_name.clear()
        last_name.send_keys('yulia')
        time.sleep(1)

        email = driver.find_element(By.ID, 'addCandidate_email')
        email.clear()
        email.send_keys('elizabeth')
        time.sleep(1)
    
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2) 

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Expected format: admin@example.com")

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
        driver.find_element(By.LINK_TEXT, 'Candidates').click()
        
        # Click cari
        cari = driver.find_element(By.ID, 'candidateSearch_candidateName')
        cari.clear()
        cari.send_keys('Jennifer Clinton')
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
        driver.find_element(By.LINK_TEXT, 'Candidates').click()
        
        # Click cari
        cari = driver.find_element(By.ID, 'candidateSearch_candidateName')
        cari.clear()
        cari.send_keys('Jnn')
        time.sleep(1)

        # Click Search
        search = driver.find_element(By.ID, 'btnSrch')
        search.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,"validation-error").text
        self.assertIn(response_data,"Invalid")
        
        driver.close()

if __name__ == '__main__':
    unittest.main()
