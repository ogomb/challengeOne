from flask import render_template, request, redirect, url_for

from app import app

users = set()
users_bucketlist = []

@app.route('/')
def index():
    return render_template('home.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = str(request.form.get('inputName'))
        email = str(request.form.get('inputEmail'))
        password = str(request.form.get('inputPassword'))

        if username:
            users.add(username)
            users.add(email)
            users.add(password)
            print users
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = str(request.form.get('inputEmail'))
        password = str(request.form.get('inputPassword'))
        if email in users and password in users:
            return redirect(url_for('bucket_list'))
        else:
            return redirect(url_for('signup'))
    return render_template('login.html')

@app.route('/bucket_list', methods=['GET', 'POST'])
def bucket_list():
    if request.method == 'POST':
        description = str(request.form.get('description'))
        if description:
            users_bucketlist.append(description)
    return render_template('my_bucket.html', users_bucketlist=users_bucketlist)

@app.route('/bucket_list/<id>/delete', methods=['POST'])
def delete_bucket_list_item(id):
    id_to_delete = int(id) -1 
    print id_to_delete
    del users_bucketlist[id_to_delete]
    return redirect(url_for('bucket_list'))

