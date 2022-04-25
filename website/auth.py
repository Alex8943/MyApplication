from flask import Blueprint, render_template, request, flash


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
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) == 0 & len(first_name) == 0 & len(password1) == 0 & len(password2) == 0: 
            flash('You have to give out your infomation! ', category='error')
            
        elif len(email) < 8: 
                flash('Your email have to be 9 or more characters', category='error')
        elif len(first_name) < 1: 
                flash('Your name is not long enough, 1 or more is required! ', category='error')
        elif len(password1) < 5: 
            flash('Your account must be grater than 5 charecters', category='error')
        elif password1 == password2: 
            flash('"Confirm password" field must be the same as "password" field! ')
        else: 
            flash('Account created! ', category='Success')

    return render_template("sign_up.html")