from splinter import Browser

import pytest


@pytest.yield_fixture(scope='session')
def browser():
    b = Browser()
    yield b
    b.quit()


BASE_URL = 'http://localhost:5000'

def url(route):
    return '{}/{}'.format(BASE_URL, route)

def test_can_perform_activities(browser):
    """
    A test method to test functionalities from user perspective."""
    # You have heard about a cool new online bucketlist app. you go
    # to check out its homepage
    browser.visit(url('/'))
    # you notice the page title and header mention bucketlist
    assert 'BucketList' in browser.title
    
    # YOu are invited to sign up straight away
    # you types details into the form

    browser.visit(url('signup'))
    inputbox = browser.find_by_id('inputName').first
    assert inputbox['placeholder'] == 'Name'

    # When you hits enter, the page redirects, and now the page tells you to login
    # There is still a form inviting you to login

    browser.visit(url('login'))
    inputbox = browser.find_by_id('inputEmail').first
    assert inputbox['placeholder'] == 'Email Address'


    browser.visit(url('bucket_list'))
    textwritten = browser.find_by_id('modal_open').first
    