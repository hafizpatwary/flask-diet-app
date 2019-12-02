from flask import render_template, redirect, url_for, flash, request
from application import app, db, bcrypt
from application.models import User, Diet, Food, diet_plan
from application.forms import DietForm, FoodForm, RegistrationForm

#-----------------------------------------Home-----------------------------------------------------------

@app.route('/')
@app.route('/home')
def home():
    diets = Diet.query.all()
    return render_template("home.html",title='Home',diets=diets)



@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        userData = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            )
        db.seesion.add(userData)
        db.seesion.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('registration.html',title='Registration', form=form)


#-----------------------------------------Create Diet----------------------------------------------------

@app.route('/creatediet', methods=['GET','POST'])
def create_diet():
    form = DietForm()
    if form.validate_on_submit():
        dietData = Diet(
            diet_name=form.diet_name.data,
            description=form.description.data,
            user=User.query.first()
            )

        db.session.add(dietData)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        print(form.errors)

    return render_template('create_diet.html',title='Create Diet', form=form)


@app.route('/diets/delete/<string:dietID>', methods=['GET','POST'])
def delete_diet(dietID):
    diet_to_delete = Diet.query.filter_by(dietID=dietID).first()
    db.session.delete(diet_to_delete)
    db.session.commit()

    return redirect(url_for('diets'))

#-------------------------------------------DietFood------------------------------------------------------

@app.route('/diets', methods=['GET','POST'])
def diets():
    diets = Diet.query.all()
    foods = Food.query.all()
    if request.method == "POST":
        adding_to_diet = Diet.query.filter_by(dietID=request.form['diet']).first()
        food_to_add = Food.query.filter_by(foodID=request.form['foods']).first()
        adding_to_diet.foods.append(food_to_add)
        db.session.commit()
        return render_template('diets.html', foods=foods,diets=diets)
    return render_template('diets.html', foods=foods, food='no food',diets=diets)

#--------------------------------------------Food--------------------------------------------------------

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

@app.route('/food/delete/<string:foodID>', methods=['GET','POST'])
def delete_food(foodID):

    food_to_delete = Food.query.filter_by(foodID=foodID).first()
    db.session.delete(food_to_delete)
    db.session.commit()

    return redirect(url_for('food'))

