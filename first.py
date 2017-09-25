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

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        '''
        Setting Path For GeckoDriver And 
        Initiallizing Firefox Then 
        We Are Passing Url of the Application
        
        ''' 
        #print("Print me once")
        # create a new Firefox session
        firefoxPath="/scratch/tools/geckodriver"
        self.driver = webdriver.Firefox(executable_path=firefoxPath)
        #
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://localhost:9000/#/loginScreen")
        
        
        
    def runTest(self):
# get the search textbox
        '''
        Login Page will be shown with mEngage Logo and  With 
        UserName And PassWord TextField Should Be Shown Then We 
        Are Passing UserName And PassWord Using Send Keyword Of Selenium 
        
        '''
        self.search_UserName = self.driver.find_element_by_name("userName")
        self.search_UserName.clear()    
        self.search_UserName.send_keys("sharibimam")
        self.search_Password =self.driver.find_element_by_name("password")
        self.search_Password.clear()
        self.search_Password.send_keys("E2fyVH1G")
        print("Testing1")
        self.click_Remember_me=self.driver.find_element_by_xpath("//label[@class='checkboxLabel']").click()
        self.click_Login_Button=self.driver.find_element_by_xpath("//input[@type='button']")
        self.click_Login_Button.click()
        self.runTest1()
        
    def runTest1(self):
        '''
        Checking Text Size Of How much you rate for CTC & Benefits in Mirafra?
        And Clicking On Rating System One BY One
        And parallely Checking Smiley is enabled or not for each rating button
        And Finally I Will Click on Commenting Button To Write Some Text There 
        '''
        #print("1nd test case")
        self.Text=self.driver.find_element_by_xpath("//p[text()='How much you rate for CTC & Benefits in Mirafra?']") 
        print(self.Text.size)
        time.sleep(10)
        self.elem1 = self.driver.find_element_by_xpath("(//label[@class='rating_1'])[1]")
        time.sleep(10)
        self.elemt2 =self.driver.find_element_by_xpath("(//label[@class='rating_2'])[1]")
        time.sleep(10)
        self.elemt3=self.driver.find_element_by_xpath("(//label[@class='rating_4'])[1]")
        self.elemt4 = self.driver.find_element_by_xpath("(//label[@class='rating_3'])[1]")
        
        
       
        
        print("Testing2")  
    
        
                
 
        if self.elem1.is_displayed()and  self.elem1.is_enabled() and self.elemt2.is_displayed() and self.elemt2.is_displayed \
                    and self.elemt2.is_enabled() and self.elemt3.is_displayed() and self.elemt3.is_enabled and self.elemt4.is_displayed() and self.elemt4.is_enabled() :
                    
                    
                    
                
                
                     
                    self.elem1.click()
                    self.elemt2.click()
                    self.elemt3.click()
                    self.elemt4.click() # this will click the element if it is there
                    
                    print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
                    
        
        print("Able to click the element")
        
       
        wait = WebDriverWait(self.driver,200)
        print("Testing3")
        self.elemt5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[starts-with(@for,'commentBox_rangeForCTC')]")))
        self.elemt5.click()
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "(//textarea[starts-with(@class,'ng-pristine ng-untouched ng-valid ng-empty')])[1]")))
        self.user.send_keys("first data is completed")
        
        
        
        self.runTest2()
        
    def runTest2(self):   
        '''
        Checking Text Size Of How much you rate for rate for Growth in Mirafra?
        And Clicking On Rating System One BY One
        And parallely Checking Smiley is enabled or not for each rating button
        And Finally I Will Click on Commenting Button To Write Some Text There 
        '''
        
        #print("3rd module")
        self.Text=self.driver.find_element_by_xpath("//p[text()='How much you rate for Growth in Mirafra?']") 
        print(self.Text.size)
        self.elem1 = self.driver.find_element_by_xpath("(//label[@class='rating_1'])[2]")
        self.elemt2 =self.driver.find_element_by_xpath("(//label[@class='rating_2'])[2]")
        self.elemt3= self.driver.find_element_by_xpath("(//label[@class='rating_4'])[2]")
        self.elemt4 = self.driver.find_element_by_xpath("(//label[@class='rating_3'])[2]") 
        if self.elem1.is_displayed() \
                    and self.elem1.is_enabled() \
                    and self.elemt2.is_displayed \
                    and self.elemt2.is_enabled() \
                    and self.elemt3.is_displayed() \
                    and self.elemt3.is_enabled \
                    and self.elemt4.is_displayed()\
                    and self.elemt4.is_enabled() :
                    self.elem1.click()
                    self.elemt2.click()
                    self.elemt3.click()
                    self.elemt4.click() # this will click the element if it is there
                    
                    print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
                    
        print("Able to click 2Nd row element")     
        wait = WebDriverWait(self.driver, 100)       
        self.elemt5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[starts-with(@for,'commentBox_rangeForGrowth')]")))
        self.elemt5.click()
        print('champ')
        print("Testing4")
        self.user1 = wait.until(EC.visibility_of_element_located((By.XPATH, "html/body/div[1]/div/div/form/ul/li[2]/div[4]/textarea")))
        self.user1.send_keys("secound data is completed")
        self.Test3()
        
    def runTest3(self):
        '''
        Checking Text Size Of How much you rate for rate for for CTC & Benefits in Mirafra?
        And Clicking On Rating System One BY One
        And parallely Checking Smiley is enabled or not for each rating button
        And Finally I Will Click on Commenting Button To Write Some Text There 
        '''
        #print("4rd module")  
        self.Text=self.driver.find_element_by_xpath("//p[text()='How much you rate for CTC & Benefits in Mirafra?']") 
        print(self.Text.size)
        self.elem1 = self.driver.find_element_by_xpath("(//label[@class='rating_1'])[3]")
        self.elemt2 =self.driver.find_element_by_xpath("(//label[@class='rating_2'])[3]")
        self.elemt3=self.driver.find_element_by_xpath("(//label[@class='rating_4'])[3]")
        self.elemt4 = self.driver.find_element_by_xpath("(//label[@class='rating_3'])[3]") 
        if self.elem1.is_displayed()\
                    and  self.elem1.is_enabled()\
                    and self.elemt2.is_displayed()\
                    and self.elemt2.is_displayed \
                    and self.elemt2.is_enabled()\
                    and self.elemt3.is_displayed()\
                    and self.elemt3.is_enabled\
                    and self.elemt4.is_displayed()\
                    and self.elemt4.is_enabled() : 
                    self.elem1.click()
                    self.elemt2.click()
                    self.elemt3.click()
                    self.elemt4.click()
                    print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
        print("Testing5")
        print("able to click the element")  
        wait = WebDriverWait(self.driver,100)       
        self.elemt5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[starts-with(@for,'commentBox_rangeForWork')]")))
        self.elemt5.click()
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/div/div/form/ul/li[3]/div[4]/textarea")))
        self.user.send_keys("data is completed")
        print("entering the 4th row")
        self.runTest4()
        
    def runTest4(self):
        '''
        Checking Text Size Of How much you rate for rate for for Rewards & recognition in Mirafra?
        And Clicking On Rating System One BY One
        And parallely Checking Smiley is enabled or not for each rating button
        And Finally I Will Click on Commenting Button To Write Some Text There 
        '''
        #print("5thmodule")
        self.Text=self.driver.find_element_by_xpath("//p[text()='How much you rate for Rewards & recognition in Mirafra?']") 
        print(self.Text.size)
        self.elem1 = self.driver.find_element_by_xpath("(//label[@class='rating_1'])[4]")
        self.elemt2 =self.driver.find_element_by_xpath("(//label[@class='rating_2'])[4]")
        self.elemt3=self.driver.find_element_by_xpath("(//label[@class='rating_4'])[4]")
        self.elemt4 = self.driver.find_element_by_xpath("(//label[@class='rating_3'])[4]") 
        if self.elem1.is_displayed()\
                    and  self.elem1.is_enabled()\
                    and self.elemt2.is_displayed()\
                    and self.elemt2.is_displayed \
                    and self.elemt2.is_enabled()\
                    and self.elemt3.is_displayed()\
                    and self.elemt3.is_enabled\
                    and self.elemt4.is_displayed()\
                    and self.elemt4.is_enabled() : 
                    self.elem1.click()
                    self.elemt2.click()
                    self.elemt3.click()
                    self.elemt4.click()
                    print("FOUND THE LINK CREATE ACTIVITY! and Clicked it!")
                    print("Testing6")
        print("able to click the element")  
        wait = WebDriverWait(self.driver,100)       
        self.elemt5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[starts-with(@for,'commentBox_rangeForRewards')]")))
        self.elemt5.click()
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/div/div/form/ul/li[4]/div[4]/textarea")))
        self.user.send_keys(" 4th data is completed")
        print("entering the 5th row")            
        self.runTest5()
    def runTest5(self):
        '''
        Checking Text Size Of How much you rate for rate for Chances of Staying with Mirafra?
        And Clicking On Rating System One BY One
        And parallely Checking Smiley is enabled or not for each rating button
        And Finally I Will Click on Commenting Button To Write Some Text There 
        '''
        #print("6th module")
        self.Text=self.driver.find_element_by_xpath("//p[text()='How much you rate for Chances of Staying with Mirafra?']") 
        print(self.Text.size)
        self.elem1 = self.driver.find_element_by_xpath("(//label[@class='rating_1'])[5]")
        self.elemt2 =self.driver.find_element_by_xpath("(//label[@class='rating_2'])[5]")
        self.elemt3=self.driver.find_element_by_xpath("(//label[@class='rating_4'])[5]")
        self.elemt4 = self.driver.find_element_by_xpath("(//label[@class='rating_3'])[5]") 
        if self.elem1.is_displayed()\
                    and  self.elem1.is_enabled()\
                    and self.elemt2.is_displayed()\
                    and self.elemt2.is_displayed \
                    and self.elemt2.is_enabled()\
                    and self.elemt3.is_displayed()\
                    and self.elemt3.is_enabled\
                    and self.elemt4.is_displayed()\
                    and self.elemt4.is_enabled() : 
                    self.elem1.click()
                    self.elemt2.click()
                    self.elemt3.click()
                    self.elemt4.click()
        print("able to click the element")
        print("Testing7")  
        wait = WebDriverWait(self.driver,100)       
        self.elemt5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[starts-with(@for,'commentBox_rangeForStaying')]")))
        self.elemt5.click()
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/div/div/form/ul/li[5]/div[4]/textarea")))
        self.user.send_keys(" 5th data is completed")
        print("entering the 6th row")      
        self.runTest6()
    def runTest6(self):
        '''
        Checking Text Size Of How much you rate for rate for Onsite Opportunities in Mirafra?
        And Clicking On Rating System One BY One
        And parallely Checking Smiley is enabled or not for each rating button
        And Finally I Will Click on Commenting Button To Write Some Text There 
        '''
        #print("7th module")
        self.Text=self.driver.find_element_by_xpath("//p[text()='How much you rate for Onsite Opportunities in Mirafra?']") 
        print(self.Text.size)
        self.elem1 = self.driver.find_element_by_xpath("(//label[@class='rating_1'])[6]")
        self.elemt2 =self.driver.find_element_by_xpath("(//label[@class='rating_2'])[6]")
        self.elemt3=self.driver.find_element_by_xpath("(//label[@class='rating_4'])[6]")
        self.elemt4 = self.driver.find_element_by_xpath("(//label[@class='rating_3'])[6]") 
        if self.elem1.is_displayed()\
                    and  self.elem1.is_enabled()\
                    and self.elemt2.is_displayed()\
                    and self.elemt2.is_displayed \
                    and self.elemt2.is_enabled()\
                    and self.elemt3.is_displayed()\
                    and self.elemt3.is_enabled\
                    and self.elemt4.is_displayed()\
                    and self.elemt4.is_enabled() :
                    self.elem1.click()
                    self.elemt2.click()
                    self.elemt3.click()
                    self.elemt4.click()
        print("able to clicsharibimam@mirafra.com k the element")  
        print("Testing8")
        wait = WebDriverWait(self.driver,100)       
        self.elemt5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[starts-with(@for,'commentBox_rangeForOnsite')]")))
        self.elemt5.click()
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/div/div/form/ul/li[6]/div[4]/textarea")))
        self.user.send_keys(" 6th data is completed")
        print("entering the 7th row") 
        self.runTest7()
    def runTest7(self):
        '''
        Checking Text Size Of How much you rate for feeling happy to be part of his/her Team in Mirafra?']"
        And Clicking On Rating System One BY One
        And parallely Checking Smiley is enabled or not for each rating button
        And Finally I Will Click on Commenting Button To Write Some Text There 
        '''
        #print("8th module")
        self.Text=self.driver.find_element_by_xpath("//p[text()='How much you rate for feeling happy to be part of his/her Team in Mirafra?']") 
        print(self.Text.size)
        self.elem1 = self.driver.find_element_by_xpath("(//label[@class='rating_1'])[7]")
        self.elemt2 =self.driver.find_element_by_xpath("(//label[@class='rating_2'])[7]")
        self.elemt3=self.driver.find_element_by_xpath("(//label[@class='rating_4'])[7]")
        self.elemt4 = self.driver.find_element_by_xpath("(//label[@class='rating_3'])[7]") 
        if self.elem1.is_displayed()\
                    and  self.elem1.is_enabled()\
                    and self.elemt2.is_displayed()\
                    and self.elemt2.is_displayed \
                    and self.elemt2.is_enabled()\
                    and self.elemt3.is_displayed()\
                    and self.elemt3.is_enabled\
                    and self.elemt4.is_displayed()\
                    and self.elemt4.is_enabled() :
                    self.elem1.click()
                    self.elemt2.click()
                    self.elemt3.click()
                    self.elemt4.click()
        print("able to click the element")  
        print("Testing9")
        wait = WebDriverWait(self.driver,100)       
        self.elemt5 = wait.until(EC.visibility_of_element_located((By.XPATH, "//label[starts-with(@for,'commentBox_rangeForHappy')]")))
        self.elemt5.click()
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/div/div/form/ul/li[7]/div[4]/textarea")))
        self.user.send_keys(" 7th data is completed")
        print("entering the 8th row")   
        self.runTest8()
    def runTest8(self):
        '''
        Entering Data in last text Section
        And Then We are clicking on Sos .png
        Entering Text In Text Field  and clicking on
        Ok button
        ''' 
        #print("9th module")
        wait = WebDriverWait(self.driver,100)
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "html/body/div[1]/div/div/form/ul/li[8]/div/textarea")))
        self.user.send_keys(" 7th data is completed")
        #self.img=wait.until(EC.presence_of_element_located((By.XPATH,"//img[@src='images/sos.png']"))).click()
        #self.keys = wait.until(EC.presence_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[2]/div/div/div[3]/textarea")))
        #self.keys.send_keys("sharibimam")
       # self.keys1 = wait.until(EC.presence_of_element_located((By.XPATH,"(//label[text()='OK'])[2]")))
        #self.keys1.click()sharibimam@mirafra.com 
        #self.keys1 = wait.until(EC.presence_of_element_located((By.XPATH,"html/body/div[1]/div/div/div[2]/div/div/div[4]/label[1]")))
        #self.keys1.click()
        #print("imam")
        print("Testing10")
        
        self.runTest9()
        
    def runTest9(self):  
        '''
        In this method we are Clicking on submit button 
        Then clicking on side Menu Control
        And Here we are getting  text size 
        And Finally We are Clicking on Logout button
        '''
        
        wait = WebDriverWait(self.driver,100)
        time.sleep(10)
        self.user = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Submit']")))
        self.user.click()  
        print("Testing11")
        self.userr = wait.until(EC.presence_of_element_located((By.XPATH, "(//label[text()='OK'])[1]")))
        self.userr.click()
        print("Testing12")
        self.userrr = wait.until(EC.presence_of_element_located((By.XPATH, " //label[@for='sideMenuControl']")))
        self.userrr.click()
        print("Testing13")
        self.useclick = wait.until(EC.presence_of_element_located((By.XPATH, " //label[@for='sideMenuControl']")))
        self.useclick.click()
        print("Testing14")
        self.useText= wait.until(EC.presence_of_element_located((By.XPATH, "    //label[@ng-click='getHistory()'] ")))
        self.Text=self.useText.text
        print(self.Text)     
        print("Testing15")
        self.useclickk = wait.until(EC.presence_of_element_located((By.XPATH, " html/body/div[1]/div/div/div[3]/div[2]/ul/li[2]/label")))
        self.useclickk.click()
        
          
         
        print("Testing16")             
    @classmethod
    def tearDown(self):
        '''
        Finally Closing The Quiting The Code
        '''
# close the browser window
        self.driver.implicitly_wait(20)
        self.driver.quit()
         
         

if __name__ == '__main__':
     unittest.main(verbosity=2)
