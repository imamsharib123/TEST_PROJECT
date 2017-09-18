'''
Created on 14-Sep-2017

@author: sharibimam
'''

class LoginClass1():
    def __init__(self, driver):
        self.driver=driver
        
    def loginClassName(self,username,Password):
        self.search_UserName = self.driver.find_element_by_name("userName")
        self.search_UserName.clear()    
        self.search_UserName.send_keys("username")
        self.search_Password =self.driver.find_element_by_name("password")
        self.search_Password.clear()
        self.search_Password.send_keys("Password")
        print("Testing1")
        self.click_Remember_me=self.driver.find_element_by_xpath("//label[@class='checkboxLabel']").click()
        self.click_Login_Button=self.driver.find_element_by_xpath("//input[@type='button']")
        self.click_Login_Button.click()    
        
        
   