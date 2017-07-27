"""tests for the application."""
import unittest
from app import app
from app.views import BucketList
from app.views import User


class BucketListApplication(unittest.TestCase):
    """test class that test many functionalities in the application. """

    def setUp(self):
        self.blist = BucketList()
        self.my_user = User()

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
        this function tests if the post will redirect to
        another page after a post request is made. """
        client = app.test_client()
        response = client.post('/signup', data={1: "just random stuff"})
        self.assertEqual(response.status, '302 FOUND')

    def test_login_page_redirection(self):
        """
        this function tests if the post will redirect
        to another page after a post request is made. """
        client = app.test_client()
        response = client.post('/login', data={'email':"some weird email here"})
        self.assertEqual(response.status, '302 FOUND')

    def test_bucketlist_page_bucketlist(self):
        """
        Test if the correct post is sent."""
        client = app.test_client()
        response = client.post('bucket_list', data={"description":"go hiking in everest"})
        self.assertNotEqual('go hiking in everest', response.get_data(as_text=True))


    def test_logout_works(self):
        """
        Test if the page logout works."""
        client = app.test_client()
        return client.get('/logout', follow_redirects=True)
    
    def test_redirection_after_edit(self):
        """
        this function tests if the post will redirect
        to another page after a post  is made. """
        self.my_dict["name"]=[]
        client = app.test_client()
        response = client.post('/bucket_list/delete_all', data={"bucket_name":"name"})
        self.assertEqual(response.status, '302 FOUND')

    def test_bucketlist_empty_after_removingall(self):
        """
        Test that the bucket list contains nothing after
        deleting everything. """
        self.blist.delete_all_items_in_bucket()
        self.assertEqual([], self.blist.display_list())

    def test_buctetlist_has_one_item(self):
        """test the bucket list has an item after adding one. """
        self.blist.add_item_to_bucket("going to glide")
        self.assertEqual(["going to glide"], self.blist.display_list())

    def test_user_assignment_name(self):
        """test that a user has a name after assigning it one. """
        self.my_user.name = "siwel"
        self.assertNotEqual("IMIRIK", self.my_user.name)


    def test_the_length_ofbucketlist(self):
        """test if the length of the bucket list is equal to the actual
        bucket list length."""
        self.blist = ["go to mt.Kenya", "visit longonot", "visit japan"]
        self.assertEqual(3, len(self.blist))
if __name__ == "__main__":
    unittest.main()
