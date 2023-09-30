from flask_restful import Resource, reqparse
from models.single_meal import SingleMealModel
from models.meal_template import MealTemplateModel
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime,date


class SingleMeal(Resource):
    @jwt_required()
    def get(self, user_id,single_meal_id):
        single_meal = SingleMealModel.find_single_meal(single_meal_id)
        if single_meal:
            if(single_meal.user_id != user_id):
                return{'message': 'Incorrect user id.'}, 404
            try:
                return single_meal.json()
            finally:
                single_meal.has_been_used = 1
                print(single_meal.has_been_used)
                single_meal.save_single_meal()
        return {'message': 'Meal not found.'}, 404 #not found
     
    @jwt_required()
    def delete(self, user_id, single_meal_id):
        jwt = get_jwt()
        if (jwt.get("user_type") != 0 and jwt.get("user_type") != 1):
            return {"message": "User type not allowed for this operation."},401
        single_meal = SingleMealModel.find_single_meal(single_meal_id)
        if single_meal:
            if(jwt.get("user_id") != single_meal.user_id and jwt.get("user_type")!= 0):
                return {"message": "User not allowed for this operation."},401
            try:
                single_meal.delete_single_meal()
            except:
               return {'message': 'An internal error ocurred trying to delete meal.'}, 500 
            return {'message': 'Meal deleted.'}
        return{'message':'Meal not found.'},404   


class SingleMealRegister(Resource):
    @jwt_required()
    def post(self):
        jwt = get_jwt()
        if (jwt.get("user_type") != 0 and jwt.get("user_type") != 1 and jwt.get("user_type") != 3):
            return {"message": "User type not allowed for this operation."},401
        atributes = reqparse.RequestParser()
        atributes.add_argument('meal_template_id',type=int, required=True, help="The field 'meal_template_id' cannot be null.")
        atributes.add_argument('expiration_date',type=str, required=True, help="The field 'expiration_date' cannot be null.")
        dados = atributes.parse_args()
        MealTemplate = MealTemplateModel.find_meal_template(dados['meal_template_id'])
        if(MealTemplate is not None and MealTemplate.user_id == jwt.get("user_id")):     
            date_format = '%Y-%m-%d'
            try:
                dateObject = datetime.strptime(dados['expiration_date'], date_format)
                dateObject = date(dateObject.year,dateObject.month,dateObject.day)
            except ValueError:        
                return{'message': 'Meal creation failed. Invalid date.'},400
            if (dateObject < date.today()):
                return{'message': 'Meal creation failed. Past date.'},400
            else:
                single_meal = SingleMealModel(jwt.get("user_id"),**dados)
                single_meal.save_single_meal()
                return{'message': 'Meal created successfully.'},200
        else:
            return{'message': 'Meal template not found.'},404
        
class SingleMealSearch(Resource):
    @jwt_required()
    def get(self):
        pass