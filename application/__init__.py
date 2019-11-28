from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os, pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+os.getenv('MYSQL_USERNAME')+':'+os.getenv('MYSQL_PASSWORD')+'@34.89.111.107/diet'
db = SQLAlchemy(app)

from application import routes
