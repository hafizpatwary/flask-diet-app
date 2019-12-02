from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, pymysql
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@34.89.111.107/diet"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from application import routes
