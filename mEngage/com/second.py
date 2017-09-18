'''
Created on 11-Sep-2017

@author: sharibimam
'''
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from com import LoginClass
class TestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("Print me once")
        # create a new Firefox session
        firefoxPath="/scratch/tools/geckodriver"
        self.driver = webdriver.Firefox(executable_path="./geckodriver")
        #Loginobj=LoginClass(self.driver)
        #
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://localhost:9000/#/loginScreen")
        
    def runTest(self):
# get the search textbox
        #driver=self.driver
        '''self.Loginobj.loginclassname("sharibimam","E2fyVH1G")'''
        self.search_UserName =self.driver.find_element_by_name("userName")
        self.search_UserName.clear()    
        time.sleep(10)
        self.search_UserName.send_keys("sharibimam")
        self.search_Password =self.driver.find_element_by_name("password")
        self.search_Password.clear()
        time.sleep(10)
        self.search_Password.send_keys("E2fyVH1G")
        time.sleep(10)
        print("Testing2")
        self.click_Remember_me=self.driver.find_element_by_xpath("//label[@class='checkboxLabel']").click()
        time.sleep(10)
        self.click_Login_Button=self.driver.find_element_by_xpath("//input[@type='button']")
        time.sleep(10)
        self.click_Login_Button.click()
        self.runTest11()
    def runTest11(self):
        print("entering1")
        wait = WebDriverWait(self.driver,100)
        self.img=wait.until(EC.presence_of_element_located((By.XPATH,"//img[@src='images/sos.png']"))).click()
        self.keys = wait.until(EC.presence_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[2]/div/div/div[3]/textarea")))
        self.keys.send_keys("sharibimam")
        print("Testing3")
        time.sleep(10)
        self.keys1 = wait.until(EC.presence_of_element_located((By.XPATH,"(//label[text()='OK'])[2]")))
        self.keys1.click()
        print("Testing4")
        time.sleep(10)
        self.keys2= wait.until(EC.presence_of_element_located((By.XPATH,"(//label[text()='OK'])[1]")))
        
        self.keys2.click()
        print("Testing5")
        
        self.keys3 =wait.until(EC.presence_of_element_located((By.XPATH,"//label[@class='fa fa-info info']")))
        self.keys3.click()
        self.keys4 = wait.until(EC.presence_of_element_located((By.XPATH,"(//label[text()='OK'])[1]")))
        self.keys4.click() 
        time.sleep(3)
        self.runTest12()
    def runTest12(self):
        wait = WebDriverWait(self.driver,100)
        self.userrr = wait.until(EC.presence_of_element_located((By.XPATH, " //label[@for='sideMenuControl']")))
        self.userrr.click()
        print("Testing6")
        self.useclick = wait.until(EC.presence_of_element_located((By.XPATH, " //label[@for='sideMenuControl']")))
        self.useclick.click()
        time.sleep(10)
        print("Testing7")
        self.useText= wait.until(EC.presence_of_element_located((By.XPATH, "    //label[@ng-click='getHistory()'] ")))
        self.Text=self.useText.text
        print(self.Text)     
        print("Testing8")
        self.useclickk = wait.until(EC.presence_of_element_located((By.XPATH, " html/body/div[1]/div/div/div[3]/div[2]/ul/li[2]/label")))
        self.useclickk.click()
        
        #self.img=wait.until(EC.presence_of_element_located((By.XPATH,"//img[@src='images/sos.png']"))).click()     
         
        print("complete") 
    @classmethod
    def tearDown(self):
        self.driver.quit()    
        
        
        
          
        
           
if __name__ == '__main__':
     unittest.main(verbosity=2)        