from flask import render_template, redirect, url_for, flash, request
from application import app, db, bcrypt, login_manager
from application.models import User, Diet, Food, diet_plan
from application.forms import DietForm, FoodForm, RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

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
        db.session.add(userData)
        db.session.commit()
        flash("Account created successfully", 'success')
        return redirect(url_for('login'))
    else:
        print(form.errors)

    return render_template('registration.html',title='Registration', form=form)



@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

        flash("Login unsuccessfull. Please check email and password", 'danger')

    return render_template('login.html',title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out!", 'success')
    return redirect(url_for('home'))
#-----------------------------------------Create Diet----------------------------------------------------

@app.route('/creatediet', methods=['GET','POST'])
@login_required
def create_diet():
    form = DietForm()
    if form.validate_on_submit():
        dietData = Diet(
            diet_name=form.diet_name.data,
            description=form.description.data,
            user=current_user
            )

        db.session.add(dietData)
        db.session.commit()
        flash(f"Diet {form.diet_name.data} created successfully", 'success')

        return redirect(url_for('diets'))
    else:
        print(form.errors)

    return render_template('create_diet.html',title='Create Diet', form=form)


@app.route('/diets/delete/<string:dietID>', methods=['GET','POST'])
@login_required
def delete_diet(dietID):
    diet_to_delete = Diet.query.filter_by(dietID=dietID).first()
    db.session.delete(diet_to_delete)
    db.session.commit()

    return redirect(url_for('diets'))

#------------------------------------------MyDiet---------------------------------------------------------

@app.route('/diets', methods=['GET','POST'])
@login_required
def diets():
    diets = Diet.query.filter_by(user=current_user).all()
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

