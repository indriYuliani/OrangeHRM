from lib2to3.pgen2 import driver
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers"
username="Admin" # username admin
password="admin123" # password admin

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_test_login(self):
        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(3)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

    def test_b_test_search_sukses(self):
        driver = self.driver
        self.test_a_test_login()
        time.sleep(3)
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys(username)
        time.sleep(3)
        driver.find_element(By.ID,"searchBtn").click()
        time.sleep(1)

        

        # Admin Link Click
        driver.find_element(By.LINK_TEXT, 'Admin').click()

        # Click Add
        edit = driver.find_element(By.ID, 'btnAdd')
        edit.click()
        time.sleep(3)

        userrole = driver.find_element(By.ID, 'systemUser_userType')
        sel = Select(userrole)
        sel.select_by_value('1')
        time.sleep(1)
        
        employee_name = driver.find_element(By.XPATH, '//*[@id="systemUser_employeeName_empName"]')
        employee_name.clear()
        employee_name.send_keys('Jarvis Friday Test')
        time.sleep(1)

        usernamenew = driver.find_element(By.XPATH, '//*[@id="systemUser_userName"]')
        usernamenew.clear()
        usernamenew.send_keys('jarvis')
        time.sleep(1)

        status = driver.find_element(By.ID, 'systemUser_status')
        sel = Select(status)
        sel.select_by_value('1')
        time.sleep(1)

        passwordnew = driver.find_element(By.XPATH, '//*[@id="systemUser_password"]')
        passwordnew.clear()
        passwordnew.send_keys('masuk123')
        time.sleep(1)

        passwordconfirm = driver.find_element(By.XPATH, '//*[@id="systemUser_confirmPassword"]')
        passwordconfirm.clear()
        passwordconfirm.send_keys('masuk123')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

    def test_add_user_no_employee(self):
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
        username.send_keys('admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # Admin Link Click
        driver.find_element(By.LINK_TEXT, 'Admin').click()

        # Click Add
        edit = driver.find_element(By.ID, 'btnAdd')
        edit.click()
        time.sleep(3)

        userrole = driver.find_element(By.ID, 'systemUser_userType')
        sel = Select(userrole)
        sel.select_by_value('1')
        time.sleep(1)
        
        employee_name = driver.find_element(By.XPATH, '//*[@id="systemUser_employeeName_empName"]')
        employee_name.clear()
        employee_name.send_keys('Jarvis Test')
        time.sleep(1)
        
        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Employee does not exist")

    def test_add_user_existing_username(self):
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
        username.send_keys('admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # Admin Link Click
        driver.find_element(By.LINK_TEXT, 'Admin').click()

        # Click Add
        edit = driver.find_element(By.ID, 'btnAdd')
        edit.click()
        time.sleep(3)

        userrole = driver.find_element(By.ID, 'systemUser_userType')
        sel = Select(userrole)
        sel.select_by_value('1')
        time.sleep(1)
        
        employee_name = driver.find_element(By.XPATH, '//*[@id="systemUser_employeeName_empName"]')
        employee_name.clear()
        employee_name.send_keys('Jarvis Friday Test')
        time.sleep(1)

        usernamenew = driver.find_element(By.XPATH, '//*[@id="systemUser_userName"]')
        usernamenew.clear()
        usernamenew.send_keys('jarvis')
        time.sleep(1)

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        response_data = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response_data,"Already exists")

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()