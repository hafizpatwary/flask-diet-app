from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, pymysql
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_IP')}/diet"
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app) #initial an instance of LoginManager
login_manager.login_view = 'login' #Sets login route, hence it should have the same name as login function
login_manager.login_message_category = 'info' #Setting a bootstrap format for the message flashed


from application import routes
