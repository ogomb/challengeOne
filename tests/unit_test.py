from app import app

    
def test_root_url_has_correct_html():
    client = app.test_client()
    rsp = client.get('/')
    assert rsp.status == '200 OK'
    html = rsp.get_data(as_text=True)
    assert'<title>BucketList</title>', html

def test_sign_up_page_accepts_post_request():
    client = app.test_client()
    rsp = client.post('/signup', data={1: "just random stuff"})
    assert rsp.status == '200 OK'
    assert 'just random stuff' in rsp.get_data(1)



