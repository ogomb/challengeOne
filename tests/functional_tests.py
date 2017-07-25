from splinter import Browser
import unittest

class TestFunctionalPart(unittest.TestCase):

      
 
   

    def url(self,route):
        BASE_URL = 'http://0.0.0.0:5000'
        return '{}/{}'.format(BASE_URL, route)

    def test_can_perform_activities(self):
        
        b = Browser()
            
        """
        A test method to test functionalities from user perspective."""
        # You have heard about a cool new online bucketlist app. you go
        # to check out its homepage
        b.visit(self.url('/'))
        # you notice the page title and header mention bucketlist
        assert 'BucketList' in b.title
    
        # YOu are invited to sign up straight away
        # you types details into the form

        b.visit(self.url('signup'))
        inputbox = b.find_by_id('inputName').first
        assert inputbox['placeholder'] == 'Name'

        # When you hits enter, the page redirects, and now the page tells you to login
        # There is still a form inviting you to login

        b.visit(self.url('login'))
        inputbox = b.find_by_id('inputEmail').first
        assert inputbox['placeholder'] == 'Email Address'


        b.visit(self.url('bucket_list'))
        textwritten = b.find_by_id('modal_open').first


if __name__ == "__main__":
    unittest.main()
    
