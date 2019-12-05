import unittest

from flask import abort, url_for
from flask_testing import TestCase
import os
from application import app, db
from application.models import User, Diet, Food


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
        admin = User(name="admin", surname="admin", email="admin@admin.com", password="admin2019")

        # create test non-admin user
        trainer = User(name="test", surname="user", email="test@user.com", password="test2019")

        # save users to database
        db.session.add(admin)
        db.session.add(trainer)

        # create test food apple
        apple = Food(food_name='Apple', calories=75)

        # create test food pasta
        pasta = Food(food_name='Pasta', calories=400)

        # save food to database
        db.session.add(apple)
        db.session.add(pasta)

        # create a diet for admin
        vegan_diet = Diet(diet_name='Vegan', description='No meat, eggs or milk', user=admin)

        # create a 2nd diet for admin
        mass_diet = Diet(diet_name='Mass gainer', description='Protein mainly', user=admin)
        
        # save diets to database
        db.session.add(vegan_diet)
        db.session.add(mass_diet)

        # commit all changes to database
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop_all()


class test_models(TestBase):
    def test_diet_model(self):
        """ Create a diet """

        # Two diets are created in setUp()
        self.assertEqual(Diet.query.count(), 2)

        # Test if the first diet is called Vegan
        vegan_diet = Diet.query.filter_by(dietID=1).first()
        self.assertEqual(vegan_diet.diet_name, 'Vegan')

        self.assertEqual(vegan_diet.user.name, 'admin')



    def test_food_model(self):
        """ Test food query works """

        # Test there is only two food in food table
        self.assertEqual(Food.query.count(), 2)

        # Test food table is read correctly
        apple = Food.query.filter_by(foodID=1).first()
        self.assertEqual(apple.food_name, 'Apple')



    def test_diet_plan(self):
        """ Create food """

































































































































