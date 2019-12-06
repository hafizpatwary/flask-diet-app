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


class TestModels(TestBase):
    """ To test the tables created """

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
        """ Testing many to many relationship between food and diet.
        Adding Apple and Pasta to vegan diet  """
        apple = Food.query.filter_by(food_name='Apple').first()
        pasta = Food.query.filter_by(food_name='Pasta').first()

        mass_diet = Diet.query.filter_by(diet_name='Mass gainer').first()
        mass_diet.foods = [apple, pasta]

        db.session.commit()


        self.assertEqual(mass_diet.foods[1].food_name, 'Pasta')

class TestUpdateDelete(TestBase):

    def test_update_account(self):
        """ Update Account """

        # user with ID=2 curernt details:
        # name= "test", surname="user"
        trainer = User.query.filter_by(userID=2).first()

        trainer.name = "Ben"
        trainer.surname = "Crutchley"
        trainer.email = "ben@qa.com"

        db.session.commit()

        trainer = User.query.filter_by(userID=2).first()

        self.assertNotEqual(trainer.name, "test")
        self.assertNotEqual(trainer.surname, "user")
        self.assertEqual(trainer.email, "ben@qa.com")


class TestRoutes(TestBase):

    def test_home_page(self):
        """ Testing home page is responsive"""

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """ Testing login page is responsive"""

        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_food_page(self):
        """ Testing food page is responsive"""

        response = self.client.get(url_for('food'))
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        """ Testing register page is responsive"""

        response = self.client.get(url_for('food'))
        self.assertEqual(response.status_code, 200)

    def test_dietpage_without_login(self):
        """ Test diet page is not accessible without login """

        target_url = url_for('diets')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)

    def test_creatediet_without_login(self):
        """ Test login required to create diet """

        target_url = url_for('create_diet')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)

    def test_account__without_login(self):
        """ Test login required to view account """

        target_url = url_for('account')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)

class TestLoginFucntionality(TestBase):
    pass

































































































































