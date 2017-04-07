from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
# config
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database
db = SQLAlchemy(app)
# login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views