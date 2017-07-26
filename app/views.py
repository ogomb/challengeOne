
from flask import render_template, request, redirect, url_for


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
    if request.method == 'POST':
        username = str(request.form.get('inputName'))
        email = str(request.form.get('inputEmail'))
        password = str(request.form.get('inputPassword'))
                
        if username:
            model_user.name = username
            model_user.email = email
            model_user.password = password
            #print model_user.name + "============"
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
        description.strip()
        #print description
        model_user.description = description
        
        if description not in dict_of_bucket_list.keys():
            dict_of_bucket_list[description] = BucketList().display_list()
            buckets = dict_of_bucket_list.keys()
            #print buckets
            return redirect(url_for('bucket_list'))
     
    username = model_user.name
    #print "---------"
    bucket_list_items= dict_of_bucket_list.keys()
    bucket_list_items2 = dict_of_bucket_list
    dictionary=dict_of_bucket_list
    #print bucket_list_items2
    #print model_user.description
    #print dictionary
    return render_template('my_bucket.html', username=username, description=model_user.description, bucket_list_items2=bucket_list_items2, things_to_do=bucket_list_items2)



@app.route('/bucket_list/add_item', methods=['GET'])
def add_bucket_list_item():
    """
    Adds item to the bucket list."""
    if request.method == 'GET':
        
        alist = str(request.args.get('to_do'))
        bucket_name = str(request.args.get('bookId'))
        #print bucket_name
        bucket = dict_of_bucket_list[bucket_name]
        bucket.append(alist)
        
        
    return redirect(url_for('bucket_list'))

@app.route('/bucket_list/delete_all', methods=['GET','POST'])
def delete_whole_bucket_list():
    """
    Deleting all items in the bucket list."""
    if request.method == 'POST':
        alist = str(request.form.get('bucket_name'))
        #print alist + "*********************"
        name =alist.strip()
        #print name
        #print model_user.dictionary_of_lists[alist]
        del dict_of_bucket_list[name]
        return redirect(url_for('bucket_list'))

@app.route('/bucket_list/delete_item', methods=['GET','POST'])
def delete_item_in_bucket():
    """
    Deleting all items in the bucket list."""
    if request.method == 'POST':
        key_of_dict = str(request.form.get('dict_name'))
        an_item = str(request.form.get('item'))
        dict_of_bucket_list

        the_list=dict_of_bucket_list[key_of_dict]
        the_list.remove(an_item)
       
        return redirect(url_for('bucket_list'))
        

@app.route('/bucket_list/edit_item', methods=['GET','POST'])
def edit_item_in_bucket():
    """
    Deleting all items in the bucket list."""
    if request.method == 'POST':
        key_of_dict = str(request.form.get('dict_name'))
        item_to_add= str(request.form.get('item_to_add'))
        item_to_delete= str(request.form.get('item'))
        
        list_to_edit = dict_of_bucket_list[key_of_dict]
        list_to_edit.remove(item_to_delete)
        list_to_edit.append(item_to_add)
        #print item_to_add
        #print item_to_delete
        #print "_______________"
       
        return redirect(url_for('bucket_list'))
    
