from flask import render_template, redirect, url_for, flash, request
from application import app, db
from application.models import User, Diet, Food, diet_plan
from application.forms import DietForm, FoodForm

#-----------------------------------------Home-----------------------------------------------------------

@app.route('/')
@app.route('/home')
def home():
    diets = Diet.query.all()
    return render_template("home.html",title='Home',diets=diets)

#-----------------------------------------Create Diet----------------------------------------------------

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
        flash('Your diet has been added!', 'success') ##################
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('create_diet.html',title='Create Diet', form=form)

#-------------------------------------------DietFood------------------------------------------------------

@app.route('/diets', methods=['GET','POST'])
def diets():
    foods = Food.query.all()
    if request.method == "POST":
        food = request.form['foods']
        text = request.form['any']
        return render_template('diets.html', text = text, foods=foods, food=food)
    return render_template('diets.html', text='not changed', foods=foods, food='no food')

#---------------------------------------------------------------------------------------------------------

@app.route('/food', methods=['GET','POST'])
def food():
    foods = Food.query.all()
    form = FoodForm()

    if form.validate_on_submit():
        foodData = Food(
            food_name=form.food_name.data,
            calories=form.calories.data,
            )

        db.session.add(foodData)
        db.session.commit()
        return redirect(url_for('food'))
    else:
        print(form.errors)

    return render_template('food.html',title='Food', form=form, foods=foods)
