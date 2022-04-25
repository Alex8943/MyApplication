from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app(): 
    app = Flask(__name__) #This method has only one job, its to create the secure key, witch is used to handle data for the user when login in
    app.config['SECRET_KEY'] = 'This is a test for the secure key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///[DB_NAME]' #Used to tell flash where the database is located
    db.init_app(app)
    
    from .views import views
    from .auth import auth 
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app

def create_database(app): 
    if not path.exists('website/' + DB_NAME): 
        db.create_all(app=app)
        print('Created database!')