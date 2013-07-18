'''
Created on Jul 17, 2013

@author: "David Lai"
'''
import unittest
from selenium import webdriver
import time


class Test(unittest.TestCase):
    """
    The purpose of this test is to demo elements that are hidden during animation effects.
    
    In this test we want to click on the button that does not show until the slide-out panel 
    is fully visible.  Traditionally people worked around this by adding hard coded sleeps, 
    or handled using constant polling.
    """


    def setup(self):
        self.driver = webdriver.Firefox()
    
    def tearDown(self):
        #self.driver.quit()
        pass

    def test_clicking_on_slidin(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:4567/index.html#/movebox")
        
        self.driver.find_element_by_id("buybutton").click()
        
        # Hard coded sleep
        time.sleep(10)

        
        
        self.driver.find_element_by_id("buyMe").click()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

