from flask import render_template, request, redirect, url_for, session
from myForms import SignUpForm, LoginForm

from app import app

class User(object):
    """
    Model of a user with varoius functions."""
    def __init__(self):
        """
        function to initialize the  model with values."""
        self.name = ""
        self.password = ""
        self.email = ""
        self.description = ""

class BucketList(object):
    """
    Bucket list class that models a bucket list that constains string items. """
    def __init__(self):
        self.bucket_list = []
    def add_item_to_bucket(self, item):
        """
        Method to add single item to the list ."""
        self.bucket_list.append(item)
    def delete_all_items_in_bucket(self):
        """
        method to remove all items in bucket list."""
        del self.bucket_list[:]
    def remove_item_from_bucket(self, item):
        """
        method to remove a single item in the bucket list."""
        self.bucket_list.remove(item)
    def display_list(self):
        """
        method to return the list. """
        return self.bucket_list
model_user = User()
dict_of_bucket_list = {}



@app.route('/')
def index():
    """
    Renders the home page of the webapp. """
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Renders the signup page."""
    form = SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        model_user.name = username
        model_user.email = email
        model_user.password = password
        session["username"]= model_user.name
        return redirect(url_for('bucket_list'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders the login page."""
    form = LoginForm()    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        if email == model_user.email and password == model_user.password:
            return redirect(url_for('bucket_list'))
        else:
            msg = "wrong credentials"
            return redirect(url_for('signup', data = msg))
    return render_template('login.html',form=form)

@app.route('/bucket_list', methods=['GET', 'POST'])
def bucket_list():
    """
    Renders the bucket list page of the app."""
    if request.method == 'POST' and session['username'] != None:
        description = str(request.form.get('description'))
        description.strip()
        
        model_user.description = description
        if description not in dict_of_bucket_list.keys():
            dict_of_bucket_list[description] = BucketList().display_list()
            return redirect(url_for('bucket_list'))
    username = model_user.name
    
    bucket_list_items2 = dict_of_bucket_list
    dictionary = dict_of_bucket_list
    return render_template('my_bucket.html', username=username, description=model_user.description,\
 bucket_list_items2=bucket_list_items2, things_to_do=bucket_list_items2)



@app.route('/bucket_list/add_item', methods=['GET'])
def add_bucket_list_item():
    """
    Adds item to the bucket list."""
    if request.method == 'GET':
        alist = str(request.args.get('to_do'))
        bucket_name = str(request.args.get('bookId'))
        bucket = dict_of_bucket_list[bucket_name]
        bucket.append(alist)
    return redirect(url_for('bucket_list'))

@app.route('/bucket_list/delete_all', methods=['GET', 'POST'])
def delete_whole_bucket_list():
    """
    Deleting all items in the bucket list."""
    if request.method == 'POST':
        alist = str(request.form.get('bucket_name'))
        name = alist.strip()
        del dict_of_bucket_list[name]
        return redirect(url_for('bucket_list'))

@app.route('/bucket_list/delete_item', methods=['GET', 'POST'])
def delete_item_in_bucket():
    """
    Deleting all items in the bucket list."""
    if request.method == 'POST':
        key_of_dict = str(request.form.get('dict_name'))
        an_item = str(request.form.get('item'))
        the_list = dict_of_bucket_list[key_of_dict]
        the_list.remove(an_item)
        return redirect(url_for('bucket_list'))
@app.route('/bucket_list/edit_item', methods=['GET', 'POST'])
def edit_item_in_bucket():
    """
    Deleting all items in the bucket list."""
    if request.method == 'POST':
        key_of_dict = str(request.form.get('dict_name'))
        item_to_add = str(request.form.get('item_to_add'))
        item_to_delete = str(request.form.get('item'))       
        list_to_edit = dict_of_bucket_list[key_of_dict]
        list_to_edit.remove(item_to_delete)
        list_to_edit.append(item_to_add)
        return redirect(url_for('bucket_list'))

@app.route('/bucket_list/edit_bucketlist', methods=['GET', 'POST'])
def edit_bucketlist():
    """
    Editing the bucketlist."""
    if request.method == 'POST':
        new_bucketName = request.form.get("bucket-name")
        old_bucketName = request.form.get("bucketName")
        dict_of_bucket_list[new_bucketName] = dict_of_bucket_list.pop(old_bucketName)
        return redirect(url_for('bucket_list'))

@app.route('/logout')
def log_out():
    """
    Logs out the user out of system. """
    session.pop("username",None)
    dict_of_bucket_list.clear()
    return render_template("home.html")
    
