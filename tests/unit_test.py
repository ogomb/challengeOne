from app import app

    
def test_root_url_has_correct_html():
    """
    this function test if the homepage has the required element values in the title. """
    client = app.test_client()
    response = client.get('/')
    assert response.status == '200 OK'
    html = response.get_data(as_text=True)
    assert'<title>BucketList</title>', html

def test_signup_page_redirection():
    """
    this function tests if the post will redirect to another page after a post request is made. """
    client = app.test_client()
    response = client.post('/signup', data={1: "just random stuff"})
    assert response.status == '302 FOUND'

def test_login_page_redirection():
    """
    this function tests if the post will redirect to another page after a post request is made. """
    client = app.test_client()
    response = client.post('/login', data={'email':"some weird email here"})
    assert response.status == '302 FOUND'


def test_bucket_list_page_for_bucket_list():
    """
    Test if the correct post is sent."""
    client = app.test_client()
    response = client.post('bucket_list', data={"description":"go hiking in everest"})
    assert 'go hiking in everest' in response.get_data(as_text=True)
    





