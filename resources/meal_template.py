from flask_restful import Resource, reqparse
from models.meal_template import MealTemplateModel
from flask_jwt_extended import jwt_required, get_jwt
from resources.extend_date import extend_license
from resources.meal_calculator import meal_calculator
from resources.queries import search_meal_template_by_name,normalize_meal_serch_params

import sqlite3

path_params = reqparse.RequestParser()
path_params.add_argument('meal_template_name', type=str, location='values')
path_params.add_argument('user_id', type=int, location='values')
path_params.add_argument('limit', type=float, location='values')
path_params.add_argument('offset', type=float, location='values')



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



    @jwt_required()
    def patch(self):
        jwt = get_jwt()
        if (jwt.get("user_type") != 0 and jwt.get("user_type") != 1) and jwt.get("user_type" != 2):
            return {"message": "User type not allowed for this operation."},401
        atributes = reqparse.RequestParser()
        atributes.add_argument('meal_template_id',type=str, required=True, help="The field 'meal_template_id' cannot be null.")
        atributes.add_argument('meal_template_name',type=str, required=True, help="The field 'meal_template_name' cannot be null.")
        atributes.add_argument('store_name',type=str)
        atributes.add_argument('composition',type=list, location='json', required=True, help="The field 'composition' cannot be null.")
        atributes.add_argument('description',type=str)
        dados = atributes.parse_args()
        meal_template = MealTemplateModel.find_meal_template(dados['meal_template_id'])
        if meal_template:    
            if(meal_template.user_id != jwt.get("user_id") and jwt.get("user_type") != 0):
                return {"message": "User not allowed for this operation."},401
            else:
                for dado in dados:
                    if(dados[dado] is not None):
                        setattr(meal_template,str(dado),dados[dado])
                meal_template = meal_calculator(meal_template)
                
                if isinstance(meal_template,MealTemplateModel):
                    meal_template.composition = str(meal_template.composition)
                    meal_template.save_meal_template()
                    return{'message': 'Success.'},200
                else:
                    print(meal_template)
                    return{'message': meal_template},400
        else:
            return{'message': 'Meal template not found.'}
      
class MealTemplateSearch(Resource):
    @jwt_required()
    def get(self):
        jwt = get_jwt()
        connection = sqlite3.connect('instance/banco.db')
        cursor = connection.cursor()
        dados = path_params.parse_args()
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros=normalize_meal_serch_params(**dados_validos)
        if parametros.get('user_id') is not None and jwt.get('user_type') == 0:
            user_id = parametros.get('user_id')
        else:
            user_id = jwt.get('user_id') 
        if(parametros.get('meal_template_name')) is not None:
            tupla = (parametros.get('meal_template_name'),user_id,parametros.get('limit'),parametros.get('offset'))
            print(tupla)
            resultado = cursor.execute(search_meal_template_by_name,tupla)
            meal_template_list = []
            for linha in resultado:
                print("oi")
                meal_template_list.append({
                    'meal_template_id': linha[0],
                    'user_id':linha[1],
                    'meal_template_name':linha[2],
                    'description':linha[6]

                })
            connection.close()
            if(len(meal_template_list))!=0:
                return{'search_result': meal_template_list}
            else:
                return{'message': 'No item found.'},404
        return{'message': 'Please insert a template name as a parameter.'},400

