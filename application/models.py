from application import db

class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    surname = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(512), nullable=False)
    #the attribute below 'diets' is linked to the Diets table. i.e if User.diets is called all the diets that user created are shown
    diets = db.relationship('Diet', backref='user') #backref is useful when

    def __repr__(self):
        return [f"UserID: {self.userID} \r\nName: {self.name} \r\nSurname:  {self.surname} \r\nemail: {self.email}"]


diet_plan = db.Table('diet_plan',
        db.Column('userID', db.Integer, db.ForeignKey('diet.dietID')),
        db.Column('foodID', db.Integer, db.ForeignKey('food.foodID'))
        )


class Diet(db.Model):
    dietID = db.Column(db.Integer, primary_key=True)
    diet_name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(512))
    userID = db.Column(db.Integer, db.ForeignKey('user.userID'))
    #foods is a way to link Diet to Food thorugh diet_plan
    foods = db.relationship('Food', secondary=diet_plan, backref=db.backref('diets'))

    def __repr__(self):
        return [f"DietID: {self.dietID} \r\nDiet: {self.diet_name} \r\nDescription: {self.description}"]


class Food(db.Model):
    foodID = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(128), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return [f"FoodID: {self.foodID} \r\nFood: {self.food_name} \r\nCalories:  {self.calories}"]

