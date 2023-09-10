from flask_restful import Resource, reqparse
from models.meal_template import MealTemplateModel
from flask_jwt_extended import jwt_required, get_jwt
from resources.extend_date import extend_license
from resources.meal_calculator import meal_calculator
from resources.queries import normalize_path_params,search_by_name,search_by_description,description_search_query_builder
import sqlite3


class MealTemplate(Resource):
    
    def get(self, meal_template_id):
        meal_template = MealTemplateModel.find_meal_template(meal_template_id)
        if meal_template:
            return meal_template.json()
        return {'message': 'Meal template not found.'}, 404 #not found
    

        
    @jwt_required()
    def delete(self, meal_template_id):
        jwt = get_jwt()
        if (jwt.get("user_type") != 0 and jwt.get("user_type") != 1):
            return {"message": "User type not allowed for this operation."},401
        meal_template = MealTemplateModel.find_meal_template(meal_template_id)
        if meal_template:
            if(jwt.get("user_id") != meal_template.user_id and jwt.get("user_type")!= 0):
                return {"message": "User not allowed for this operation."},401
            try:
                meal_template.delete_meal_template()
            except:
               return {'message': 'An internal error ocurred trying to delete meal template.'}, 500 
            return {'message': 'Meal template deleted.'}
        return{'message':'Meal template not found.'},404   


class MealTemplateRegister(Resource):
    @jwt_required()
    def post(self):
        jwt = get_jwt()
        if (jwt.get("user_type") != 0 and jwt.get("user_type") != 1):
            return {"message": "User type not allowed for this operation."},401
        atributes = reqparse.RequestParser()
        atributes.add_argument('meal_template_name',type=str, required=True, help="The field 'meal_template_name' cannot be null.")
        atributes.add_argument('store_name',type=str)
        atributes.add_argument('composition',type=list, location='json', required=True, help="The field 'composition' cannot be null.")
        atributes.add_argument('description',type=str)
        dados = atributes.parse_args()
        
        meal_template = MealTemplateModel(jwt.get("user_id"),**dados)
        meal_template = meal_calculator(meal_template)
        if isinstance(meal_template,MealTemplateModel):
            #print(meal_template.json())
            meal_template.composition = str(meal_template.composition)
            meal_template.save_meal_template()
        else:
            print(meal_template)
            return{'message': meal_template},400
        return{'message': 'Success.'},200

        

class MealTemplateSearch(Resource):
    @jwt_required()
    def get(self):
        pass