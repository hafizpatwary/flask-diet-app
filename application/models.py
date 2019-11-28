from application import db

class Food(db.Model):
    foodID = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(128), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return ''.join(['FoodID: ', self.foodID, '\r\n', 'Food: ', self.food_name, '\r\n', 'Calories: ', self.calories])

class Diets(db.Model):
    dietID = db.Column(db.Integer, primary_key=True)
    diet_name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(512))

    def __repr__(self):
        return ''.join(['dietID: ', self.dietID, '\r\n', 'Diet: ', self.diet_name, '\r\n', 'Description: ', self.description])
