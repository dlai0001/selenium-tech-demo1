'''
Created on Jul 17, 2013

@author: "David Lai"
'''
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import unittest




class Test(unittest.TestCase):
    """
    The purpose of this test is to demo waiting for an ajax call to complete before verifying.
    
    In this test we want to verify the search results after the ajax call completes and updates 
    the results.  Traditionally this has been handled by inserting hard coded waits.
    """

    def setup(self):
        self.driver = webdriver.Firefox()
    
    def tearDown(self):
        #self.driver.quit()
        pass

    def test_ajax_search(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:4567/index.html#/livesearch")
        
        self.driver.find_element_by_id("searchInput").send_keys("Tom Dale")
        
        self.wait_until(lambda: self.driver.execute_script("return window._AUTOMATION_LATCH;") == True)
        
        # Then verify only tom dale is seen.
        results = self.driver.find_elements_by_tag_name("li")
        self.assertTrue( "Tom Dale" in results[0].text )
        

    def wait_until(self, condition, timeout=10, sleep=0.5, pass_exceptions=False):
        '''
        Waits until URL matches the expression.
        @param condition: Lambda expression to wait on.  Lambda expression 
        should return true when conditions is met.
        @type condition: lambda
        @param timeout: Timeout period in seconds.
        @rtype: int
        '''
        if not hasattr(condition, '__call__'):
            raise RuntimeError("Condition argument does not appear to be a callable function." + 
                               "Please check if this is a properly formatted lambda statement.", 
                               condition)
        end_time = datetime.now() + timedelta(seconds = timeout)
        while datetime.now() < end_time:
            try:
                if condition():
                    return
            except Exception as e:
                if pass_exceptions:
                    raise e
                else:
                    pass
            time.sleep(sleep)
    
        raise TimeoutException("Operation timed out.")




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

