from sql_alchemy import banco
from datetime import datetime


class MealTemplateModel(banco.Model):
    __tablename__ = 'meal_template'
    meal_template_id = banco.Column(banco.Integer, primary_key = True)
    user_id = banco.Column(banco.Integer, banco.ForeignKey('users.user_id')) #adicionar Relacionamento na tabela Users
    meal_template_name  = banco.Column(banco.String(80))
    store_name = banco.Column(banco.String(80))
    created_in = banco.Column(banco.String(30))
    updated_in = banco.Column(banco.String(30))
    description = banco.Column(banco.String(30))
    composition = banco.Column(banco.String(300))
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

 
    def __init__(self, user_id, meal_template_name, store_name,description, composition):
        self.user_id  = user_id 
        self.meal_template_name =   meal_template_name  
        self.store_name = store_name
        self.created_in =  datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        self.updated_in =  None 
        self.description =  description 
        self.composition = composition
        self.calories  = None 
        self.carbohydrate =  None 
        self.protein =  None 
        self.total_fat =  None 
        self.saturated_fat =  None 
        self.polyunsaturated_fat =  None 
        self.monounsaturated_fat =  None 
        self.trans_fat = None
        self.cholesterol =  None 
        self.sodium =  None 
        self.fiber =  None 
        self.sugar =  None 
        self.vitamin_a =   None  
        self.vitamin_b1 =  None 
        self.vitamin_b12 =  None 
        self.vitamin_c =  None 
        self.vitamin_d =  None 
        self.vitamin_e =  None 
        self.vitamin_k =  None 
        self.potassium =  None 
        self.zync =  None 
        self.magnesium =   None  
        self.iron =   None  
        self.chromium =  None 

      
    def json(self):
        return {
            'meal_template_id': self.meal_template_id,
            'user_id': self.user_id,
            'meal_template_name': self.meal_template_name,
            'store_name': self.store_name,
            'created_in': self.created_in,
            'updated_in': self.updated_in,
            'description': self.description,
            'composition': self.composition,
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
    def find_meal_template(cls, meal_template_id):
        meal_template = cls.query.filter_by(meal_template_id = meal_template_id).first()
        if meal_template:
            return meal_template
        return None
    
    
   
    def update_meal_template(self,meal_template):
        self.name = meal_template.name

    def  save_meal_template(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_meal_template(self):
        banco.session.delete(self)
        banco.session.commit()
    
    