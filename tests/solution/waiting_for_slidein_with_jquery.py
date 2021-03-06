'''
Created on Jul 17, 2013

@author: "David Lai"
'''
import unittest
from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.common.exceptions import TimeoutException



class Test(unittest.TestCase):
    """
    The purpose of this test is to demo elements that are hidden during animation effects.
    
    In this test we want to click on the button that does not show until the slide-out panel 
    is fully visible.  Traditionally people worked around this by adding hard coded sleeps.
    
    In this solution, we can poll on the jQuery's 'fx' queue to see how many animation 
    transistions are left before calling our action.
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
        
        
        # Using Jquery queue to examine queue length.
        animationQueueIs = """
        return $.queue( $("#ccSlideOut")[0], "fx").length;
        """
        self.wait_until(lambda: self.driver.execute_script(animationQueueIs)==0)


        self.driver.find_element_by_id("buyMe").click()



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

