'''
Created on 11-Sep-2017

@author: sharibimam
'''
import unittest
from com import HTMLTestRunner

from com.first import TestCase

from com.second import TestCase1

#from com import LoginClass1
#from com.LoginClass1 import LoginClass1


# get all tests from SearchProductTest and HomePageTest class
case1 = unittest.TestLoader().loadTestsFromTestCase(TestCase)
case2 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
#case3 = unittest.TestLoader().loadTestsFromTestCase(LoginClass1)

# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([case1,case2])

# open the report file
report= open("/scratch/neonworkSpace/mEngage/com/SmokeTestResult/SmokeTestResult.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
                 stream=report,
                 title='Test Report for Test Automation client',
                 description='Smoke Tests'
                 )

# run the suite using HTMLTestRunner
runner.run(smoke_tests)