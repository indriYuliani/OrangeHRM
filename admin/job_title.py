from lib2to3.pgen2 import driver
import unittest
import time
from urllib import response
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#variable
url="https://opensource-demo.orangehrmlive.com/index.php/admin/saveJobTitle"
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

    # def test_b_test_add_sukses(self):
    #     driver = self.driver
    #     self.test_a_test_login()
    #     time.sleep(3)
    #     driver.find_element(By.ID,"jobTitle_jobTitle").send_keys(" manag ")
    #     time.sleep(1)
    #     driver.find_element(By.ID,"jobTitle_jobDescription").send_keys("Membuat figma")
    #     time.sleep(3)
    #     driver.find_element(By.ID, "jobTitle_note").send_keys("coba saja")
    #     time.sleep(3)
    #     driver.find_element(By.ID, "btnSave").click()
    #     time.sleep(3)

    #     # response_data = driver.find_element(By.CLASS_NAME,"td class='left'").text
    #     # self.assertEqual('CO',response_data)

    #     expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/admin/viewJobTitleList"
    #     self.assertEqual(expected_current_url, driver.current_url)

   

    def test_c_test_add_gagal(self):
        driver = self.driver
        self.test_a_test_login()
        time.sleep(3)
        driver.find_element(By.ID,"jobTitle_jobTitle").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID,"jobTitle_jobDescription").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID, "jobTitle_note").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID, "btnSave").click()
        time.sleep(3)

        response = driver.find_element(By.CLASS_NAME,'validation-error').text
        self.assertIn(response,"Required")
    

   

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()