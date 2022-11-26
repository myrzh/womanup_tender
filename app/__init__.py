from flask import Flask
from flask_login import LoginManager
app = Flask(__name__)
from app import routes
app.config['SECRET_KEY'] = 'you-will-never-guess'
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
