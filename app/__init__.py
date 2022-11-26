from flask import Flask
from app import routes
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
login = LoginManager(app)
