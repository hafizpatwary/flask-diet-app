from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@34.89.111.107/diet"
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
from application import routes
