from flask import render_template, redirect, url_for
from application import app, db
from application.models import User, Diet, Food, diet_plan


#mydiets = [('1','Descritpion 1'),('2','Descritpion 2'),('3','Descritpion 3'),('4','Descritpion 4'),('5','Descritpion 5'),('6','Descritpion 6'),('7','Descritpion 7'),('8','Descritpion 8'),('9','Descritpion 9'),('10','Descritpion 10'),('11','Descritpion 11'),('12','Descritpion 12'),('13','Descritpion 13'),('14','Descritpion 14')]

#{{ url_for(create_diet) }}

@app.route('/')
@app.route('/home')
def home():
    diets = Diet.query.all()
    return render_template("home.html",diets=diets)

@app.route('/diets')
def diets():
    return "Work in progress"

@app.route('/creatediet')
def create_diet():
    return "Work in progress"

@app.route('/food')
def food():
    return "Work in progress"
