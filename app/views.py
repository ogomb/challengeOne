from flask import render_template, request

from app import app

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/bucket_list', methods=['GET', 'POST'])
def bucket_list():
    if request.method == 'POST':
        
    return render_template('my_bucket.html', )

