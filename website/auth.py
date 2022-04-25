from flask import Blueprint, render_template, request


auth = Blueprint('auth', __name__)

#Post = when we change some data in database
#Get = when we want to relode a webbrowser or redirect

@auth.route('/login', methods=['GET', 'POST']) #Adding an array of request this url can handle 
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout(): 
    return "<p>Logout here</p>"

@auth.route('/signup', methods=['GET', 'POST']) #Adding an array of request this url can handle 
def sign_up():
    
    return render_template("sign_up.html")