from sql_alchemy import banco
from datetime import datetime
from models.meal_template import MealTemplateModel

class SingleMealModel(banco.Model):
    __tablename__ = 'single_meal'
    single_meal_id = banco.Column(banco.Integer, primary_key = True)
    meal_template_id = banco.Column(banco.Integer, banco.ForeignKey('meal_template.meal_template_id')) #adicionar Relacionamento na tabela Meal_Template
    user_id = banco.Column(banco.Integer)
    expiration_date = banco.Column(banco.String(30))
    production_date = banco.Column(banco.String(30))
    expiration_date = banco.Column(banco.String(30))
    has_been_used = banco.Column(banco.Integer)
    

    def __init__(self, user_id, meal_template_id, expiration_date):
        self.meal_template_id = meal_template_id
        self.user_id  = user_id 
        self.production_date =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.expiration_date = expiration_date
        self.has_been_used = 0

      
    def json(self):
        return {
            'single_meal_id': self.single_meal_id,
            'meal_template_id': self.meal_template_id,
            'user_id': self.user_id,
            'production_date': self.production_date,
            'expiration_date': self.expiration_date,
            'has_been_used': self.has_been_used,
            'nutritional_value': MealTemplateModel.find_meal_template(self.meal_template_id).json()
        }
    
    @classmethod
    def find_single_meal(cls, single_meal_id):
        single_meal = cls.query.filter_by(single_meal_id = single_meal_id).first()
        if single_meal:
            return single_meal
        return None
      
    def update_single_meal(self,single_meal):
        #self.name = single_meal.name
        pass

    def  save_single_meal(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_single_meal(self):
        banco.session.delete(self)
        banco.session.commit()
    
    