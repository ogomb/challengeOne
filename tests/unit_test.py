from app import app
import unittest


class BucketListApplication(unittest.TestCase):
       
    def test_root_url_has_correct_html(self):
        """
        this function test if the homepage has the required element values in the title. """
        client = app.test_client()
        response = client.get('/')
        assert response.status == '200 OK'
        html = response.get_data(as_text=True)
        self.assertIn('<title>BucketList</title>', html)

    def test_signup_page_redirection(self):
        """
        this function tests if the post will redirect to another page after a post request is made. """
        client = app.test_client()
        response = client.post('/signup', data={1: "just random stuff"})
        assert response.status == '302 FOUND'

    def test_login_page_redirection(self):
        """
        this function tests if the post will redirect to another page after a post request is made. """
        client = app.test_client()
        response = client.post('/login', data={'email':"some weird email here"})
        assert response.status == '302 FOUND'


    def test_bucket_list_page_for_bucket_list(self):
        """
        Test if the correct post is sent."""
        client = app.test_client()
        response = client.post('bucket_list', data={"description":["go hiking in everest"]})
        self.assertNotEqual('go hiking in everest', response.get_data(as_text=True))


    def test_logout_works(self):
        """
        Test if the page logout works."""
        client = app.test_client()
        return client.get('/logout', follow_redirects=True)    
if __name__== "__main__":
    unittest.main()




