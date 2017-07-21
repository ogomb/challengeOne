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
        self.description = ""
        self.dictionary_of_lists = {}
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
    def add_bucket_list_to_collection(self, describe, mylist):
        """
        adds a bucket list to a collection of buckets. """
        self.dictionary_of_lists[describe] = mylist

    def remove_a_bucketlist_from_mydict(self, describe):
        """
        removes entire bucketlist from collection. """
        del self.dictionary_of_lists[describe]
       
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
        print description
        print model_user.description
        
        if description != model_user.description and model_user.bucket_list == []:
            model_user.add_bucket_list_to_collection(description, model_user.bucket_list)
            buckets = model_user.dictionary_of_lists.keys()
            print buckets
            return redirect(url_for('bucket_list'))
     
    username = model_user.name
    print "---------"
    bucket_list_items= model_user.dictionary_of_lists.keys()
    bucket_list_items2 = model_user.dictionary_of_lists.values()
    print bucket_list_items2
    return render_template('my_bucket.html', username=username, description=model_user.description, bucket_list_items=bucket_list_items, things_to_do=model_user.bucket_list)



@app.route('/bucket_list/add_item', methods=['GET','POST'])
def add_bucket_list_item():
    """
    Adds item to the bucket list."""
    if request.method == 'GET':
        
        alist = str(request.args.get('to_do'))
        print model_user.bucket_list
        print alist
        model_user.add_item_to_bucket(alist)
        print "^^^^^^^^^^^^^^^^^^"
        
        return redirect(url_for('bucket_list'))

@app.route('/bucket_list/delete_all', methods=['POST'])
def delete_whole_bucket_list():
    """
    Deleting all items in the bucket list."""
    model_user.remove_a_bucketlist_from_mydict(model_user.description)
    return redirect(url_for('bucket_list'))


        


    

