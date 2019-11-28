from flask import render_template
from application import app


diets = (('1','Descritpion 1'),('2','Descritpion 2'),('3','Descritpion 3'),('4','Descritpion 4'),('5','Descritpion 5'),('6','Descritpion 6'),('7','Descritpion 7'),('8','Descritpion 8'),('9','Descritpion 9'),('10','Descritpion 10'),('11','Descritpion 11'),('12','Descritpion 12'),('13','Descritpion 13'),('14','Descritpion 14'))

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",diets=diets,len=len(diets))

@app.route('/creatediet')
def create_diet():
    return "Work in progress"

@app.route('/food')
def food():
    return "Work in progress"
