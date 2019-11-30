from flask import render_template, redirect, url_for
from application import app, db
from application.models import User, Diet, Food, diet_plan
from application.forms import DietForm, FoodForm

@app.route('/')
@app.route('/home')
def home():
    diets = Diet.query.all()
    return render_template("home.html",title='Home',diets=diets)


@app.route('/creatediet', methods=['GET','POST'])
def create_diet():
    form = DietForm()

    if form.validate_on_submit():
        dietData = Diet(
            diet_name=form.diet_name.data,
            description=form.description.data,
            user=User.query.first()
            #foods =
            )

        db.session.add(dietData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('create_diet.html',title='Create Diet', form=form)


@app.route('/diets', methods=['GET','POST'])
def diets():
    return "Work in progress"


@app.route('/food', methods=['GET','POST'])
def food():
    form = FoodForm()

    if form.validate_on_submit():
        foodData = Food(
            food_name=form.food_name.data,
            calories=form.calories.data,
            )

        db.session.add(foodData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('food.html',title='Food', form=form)
