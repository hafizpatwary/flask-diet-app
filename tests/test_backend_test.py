import unittest

from flask import abort, url_for
from flask_testing import TestCase
import os
from application import app, db
from application.models import User, Diet


class TestBase(TestCase):

    def create_app(self):
        # pass in test configurations
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI=f"mysql+pymysql://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_IP')}/testdiet")
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        admin = User(name="admin", surname="admin", email="admin@admin.com", password="admin2016")

        # create test non-admin user
        employee = User(name="test", surname="user", email="test@user.com", password="test2016")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()


class test_diet(TestBase):
    def test_diet_model(self):
        diet = Diet(diet_name='Vegan', description='No meat, eggs or milk', userID=1)

        db.session.add(diet)
        db.session.commit()

        self.assertEqual(Diet.query.count(), 1)
        veganDiet = Diet.query.filter_by(dietID=1).first()
        self.assertEqual(veganDiet.diet_name, 'Vegan')

    def test_food_model(self):
        pass
