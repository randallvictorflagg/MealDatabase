from sql_alchemy import banco
from datetime import datetime
from resources.extend_date import extend_license


class FoodModel(banco.Model):
    __tablename__ = 'food'
    food_id = banco.Column(banco.Integer, primary_key = True)
    user_id = banco.Column(banco.Integer, banco.ForeignKey('users.user_id')) #adicionar Relacionamento na tabela Users
    barcode = banco.Column(banco.String(13))
    name  = banco.Column(banco.String(80))
    brand = banco.Column(banco.String(80))
    created_in = banco.Column(banco.String(30))
    updated_in = banco.Column(banco.String(30))
    description = banco.Column(banco.String(30))
    ingredients = banco.Column(banco.String(300))
    serving_unit = banco.Column(banco.String(10))
    serving_amount = banco.Column(banco.Float(precision = 2))
    calories = banco.Column(banco.Integer)
    carbohydrate = banco.Column(banco.Float(precision = 2))
    protein = banco.Column(banco.Float(precision = 2))
    total_fat = banco.Column(banco.Float(precision = 2))
    saturated_fat = banco.Column(banco.Float(precision = 2))
    polyunsaturated_fat = banco.Column(banco.Float(precision = 2))
    monounsaturated_fat = banco.Column(banco.Float(precision = 2))
    trans_fat = banco.Column(banco.Float(precision = 2))
    cholesterol = banco.Column(banco.Float(precision = 2))
    sodium = banco.Column(banco.Float(precision = 2))
    fiber = banco.Column(banco.Float(precision = 2))
    sugar = banco.Column(banco.Float(precision = 2))
    vitamin_a = banco.Column(banco.Float(precision = 2)) 
    vitamin_b1 = banco.Column(banco.Float(precision = 2))
    vitamin_b12 = banco.Column(banco.Float(precision = 2))
    vitamin_c = banco.Column(banco.Float(precision = 2))
    vitamin_d = banco.Column(banco.Float(precision = 2))
    vitamin_e = banco.Column(banco.Float(precision = 2))
    vitamin_k = banco.Column(banco.Float(precision = 2))
    potassium = banco.Column(banco.Float(precision = 2))
    zync = banco.Column(banco.Float(precision = 2))
    magnesium = banco.Column(banco.Float(precision = 2)) 
    iron = banco.Column(banco.Float(precision = 2)) 
    chromium= banco.Column(banco.Float(precision = 2)) 

 
    def __init__(self, user_id, barcode, name, brand, description,\
                 ingredients, serving_unit, serving_amount, calories, carbohydrate, protein,\
                 total_fat, saturated_fat, polyunsaturated_fat, monounsaturated_fat, trans_fat, \
                 cholesterol, sodium, fiber, sugar, vitamin_a, vitamin_b1, vitamin_b12, vitamin_c,\
                 vitamin_d, vitamin_e, vitamin_k, potassium, zync, magnesium, iron, chromium ):
        self.user_id  = user_id 
        self.barcode =  barcode 
        self.name =   name  
        self.brand =  brand 
        self.created_in =  datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.updated_in =  None 
        self.description =  description 
        self.ingredients = ingredients
        self.serving_unit = serving_unit
        self.serving_amount =  serving_amount 
        self.calories  = calories 
        self.carbohydrate =  carbohydrate 
        self.protein =  protein 
        self.total_fat =  total_fat 
        self.saturated_fat =  saturated_fat 
        self.polyunsaturated_fat =  polyunsaturated_fat 
        self.monounsaturated_fat =  monounsaturated_fat 
        self.trans_fat = trans_fat
        self.cholesterol =  cholesterol 
        self.sodium =  sodium 
        self.fiber =  fiber 
        self.sugar =  sugar 
        self.vitamin_a =   vitamin_a  
        self.vitamin_b1 =  vitamin_b1 
        self.vitamin_b12 =  vitamin_b12 
        self.vitamin_c =  vitamin_c 
        self.vitamin_d =  vitamin_d 
        self.vitamin_e =  vitamin_e 
        self.vitamin_k =  vitamin_k 
        self.potassium =  potassium 
        self.zync =  zync 
        self.magnesium =   magnesium  
        self.iron =   iron  
        self.chromium =  chromium 

      
    def json(self):
        return {
            'food_id': self.food_id,
            'user_id': self.user_id, 
            'barcode': self.barcode, 
            'name': self.name,  
            'brand': self.brand, 
            'created_in': self.created_in, 
            'updated_in': self.updated_in, 
            'description': self.description, 
            'ingredients': self.ingredients,
            'serving_unit': self.serving_unit,
            'serving_amount': self.serving_amount, 
            'calories': self.calories, 
            'carbohydrate': self.carbohydrate, 
            'protein': self.protein, 
            'total_fat': self.total_fat, 
            'saturated_fat': self.saturated_fat, 
            'polyunsaturated_fat': self.polyunsaturated_fat, 
            'monounsaturated_fat': self.monounsaturated_fat, 
            'trans_fat': self.trans_fat,
            'cholesterol': self.cholesterol, 
            'sodium': self.sodium, 
            'fiber': self.fiber, 
            'sugar': self.sugar, 
            'vitamin_a': self.vitamin_a,
            'vitamin_b1': self.vitamin_b1, 
            'vitamin_b12': self.vitamin_b12, 
            'vitamin_c': self.vitamin_c, 
            'vitamin_d': self.vitamin_d, 
            'vitamin_e': self.vitamin_e, 
            'vitamin_k': self.vitamin_k, 
            'potassium': self.potassium, 
            'zync': self.zync, 
            'magnesium': self.magnesium,  
            'iron': self.iron,  
            'chromium': self.chromium
        }
    
    @classmethod
    def find_food(cls, food_id):
        food = cls.query.filter_by(food_id = food_id).first()
        if food:
            return food
        return None
    
    @classmethod #aqui vai acontecer busca, fazer uma busca usando o %like%, que vai retornar uma lista de IDs e descrições
    def find_by_name(cls, name):
        pass
    
    @classmethod
    def find_by_barcode(cls, barcode):
        food = cls.query.filter_by(barcode = barcode).first()
        if food:
            return food
        return None
    
    def update_food(self,food):
        self.name = food.name

    def  save_food(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_food(self):
        banco.session.delete(self)
        banco.session.commit()
    
    