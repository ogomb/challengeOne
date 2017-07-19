from selenium import webdriver
import unittest


class VisitingUser(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait

    def tearDown(self):
        self.browser.quit()

    def test_can_signup_to_the_site(self):

        # You have heard about a cool new online bucketlist app. you go
        # to check out its homepage
        self.browser.get('http://localhost:5000')
        # you notice the page title and header mention bucketlist
        self.assertIn('BucketList', self.browser.title)
        self.fail('Finish the test!')
        # YOu are invited to sign up straight away
        # you types details into the form
        # When you hits enter, the page redirects, and now the page tells you to login
        # There is still a form inviting you to login
        # you enter the details
        # The page updates again, and now shows option to add items to bucket list
        # you type the list. Then she sees it updating on the page


if __name__ == "__main__":
    unittest.main(warnings='ignore')

