from flask import render_template, request, redirect, url_for

from app import app

class User:
    """
    Model of a user with varoius functions."""
    def __init__(self):
        """
        function to initialize the  model with values."""
        self.name = ""
        self.password = ""
        self.email = ""
        self.bucket_list = []

    def add_item_to_list(self, item):
        """
        Method to add single item to the list ."""
        self.bucket_list.append(item)
    def delete_all_items_in_list(self):
        """
        method to remove all items in bucket list."""
        del self.bucket_list[:]
    def remove_item_from_list(self, item):
        """
        method to remove a single item in the bucket list."""
        self.bucket_list.remove(item)

model_user = User()


@app.route('/')
def index():
    """
    Renders the home page of the webapp. """
    return render_template('home.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Renders the signup page."""
    if request.method == 'POST':
        username = str(request.form.get('inputName'))
        email = str(request.form.get('inputEmail'))
        password = str(request.form.get('inputPassword'))
        
        if username:
            model_user.name = username
            model_user.email = email
            model_user.password = password
            print model_user.name
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Renders the login page."""
    if request.method == 'POST':
        email = str(request.form.get('inputEmail'))
        password = str(request.form.get('inputPassword'))
        if email == model_user.email and password == model_user.password:
            return redirect(url_for('bucket_list'))
        else:
            return redirect(url_for('signup'))
    return render_template('login.html')

@app.route('/bucket_list', methods=['GET', 'POST'])
def bucket_list():
    """
    Renders the bucket list page of the app."""
    if request.method == 'POST':
        description = str(request.form.get('description'))
        if description:
            model_user.add_item_to_list(description)
    username = model_user.name
    return render_template('my_bucket.html', users_bucketlist=model_user.bucket_list, username=username)

@app.route('/bucket_list/<item>/delete', methods=['POST'])
def delete_bucket_list_item(item):
    """
    Deletes an item from the bucket list."""
    if item in model_user.bucket_list:
        model_user.remove_item_from_list(item)
    return redirect(url_for('bucket_list'))


@app.route('/bucket_list/delete_all', methods=['POST'])
def delete_whole_bucket_list():
    """
    Deleting all items in the bucket list."""
    model_user.delete_all_items_in_list()
    return redirect(url_for('bucket_list'))

