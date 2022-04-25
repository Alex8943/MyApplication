from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from sqlalchemy import true
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

#Post = when we change some data in database
#Get = when we want to relode a webbrowser or redirect

@auth.route('/login', methods=['GET', 'POST']) #Adding an array of request this url can handle 
def login():
    if request.method == 'POST': 
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email= email).first() #db kolone navn = objekt navn
        if user: 
            if check_password_hash(user.password, password): #Checking if the users password is stored in the database
                flash('Logged in successfuly', category='success')
            else: 
                flash('Incorrect password ', category='error')
        else: 
            flash('Hey! No user with this email! ', category='error')


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

        user = User.query.filter_by(email = email).first() #db kolone navn = objekt navn
        if user: 
            flash('This mail already exist!', category='error')

        elif len(email) == 0 & len(first_name) == 0 & len(password1) == 0 & len(password2) == 0: 
            flash('You have to give out your infomation! ', category='error')
            
        elif len(email) < 8: 
                flash('Your email have to be 9 or more characters', category='error')
        elif len(first_name) < 1: 
                flash('Your name is not long enough, 1 or more is required! ', category='error')
        elif len(password1) < 5: 
            flash('Your password must be grater than 5 charecters', category='error')

        else: 
            new_user = User(email=email, firstname=first_name, password=generate_password_hash( #database kolone = objekt navn 
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created! ', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")