'''
Created on Jul 17, 2013

@author: "David Lai"
'''
import unittest
from selenium import webdriver
import time



class TestStaleElement(unittest.TestCase):
    """
    The purpose of this test is to demo elements going stale because of rapid build/tear down cycles.
    
    In this test, we attempt to click on the element 50 times on a mock live update fund raiser 
    ranking board.  It's very likely that in this test we click on an element that is just about to 
    be reordered, causing a stale element exception.
    
    In this solution, we move the find operation and click() call into the JavaScript.  This will 
    guarantee that they both execute in the same run cycle.
    """

    def setup(self):
        self.driver = webdriver.Firefox()
    
    def tearDown(self):
        #self.driver.quit()
        pass

    def test_element_becoming_stale(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:4567/index.html#/")
        
        for _ in range(1,50):
            time.sleep(.5)
            self.driver.execute_script("$(\"li:contains('Einstein')\").click()")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()