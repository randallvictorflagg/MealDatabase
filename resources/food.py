from flask_restful import Resource, reqparse
from models.food import FoodModel
from flask_jwt_extended import jwt_required, get_jwt
from resources.extend_date import extend_license
from resources.queries import normalize_path_params,search_by_name,search_by_description,description_search_query_builder
import sqlite3

path_params = reqparse.RequestParser()
path_params.add_argument('barcode', type=str, location='values')
path_params.add_argument('name', type=str, location='values')
path_params.add_argument('description', type=str, location='values')
path_params.add_argument('limit', type=float, location='values')
path_params.add_argument('offset', type=float, location='values')

class Food(Resource):
    
    def get(self, food_id):
        food = FoodModel.find_food(food_id)
        if food:
            return food.json()
        return {'message': 'Food not found.'}, 404 #not found
    

        
    @jwt_required()
    def delete(self, food_id):
        jwt = get_jwt()
        if (jwt.get("user_type") != 0 and jwt.get("user_type") != 1):
            return {"message": "User type not allowed for this operation."},401
        food = FoodModel.find_food(food_id)
        if food:
            if(jwt.get("user_id") != food.user_id and jwt.get("user_type")!= 0):
                return {"message": "User type not allowed for this operation."},401
            try:
                food.delete_food()
            except:
               return {'message': 'An internal error ocurred trying to delete food.'}, 500 
            return {'message': 'Food deleted.'}
        return{'message':'Food not found.'},404   


class FoodResgister(Resource):
    @jwt_required()
    def post(self):
        jwt = get_jwt()
        if (jwt.get("user_type") != 0 and jwt.get("user_type") != 1):
            return {"message": "User type not allowed for this operation."},401
        atributes = reqparse.RequestParser()
        atributes.add_argument('user_id',type=str)
        atributes.add_argument('barcode',type=str)
        atributes.add_argument('name',type=str, required=True, help="The field 'login' cannot be null.")
        atributes.add_argument('brand',type=str)
        atributes.add_argument('description',type=str)
        atributes.add_argument('ingredients',type=str)
        atributes.add_argument('serving_unit',type=str)
        atributes.add_argument('serving_amount',type=float)
        atributes.add_argument('calories',type=int)
        atributes.add_argument('carbohydrate',type=float)
        atributes.add_argument('protein',type=float)
        atributes.add_argument('total_fat',type=float)
        atributes.add_argument('saturated_fat',type=float)
        atributes.add_argument('polyunsaturated_fat',type=float)
        atributes.add_argument('monounsaturated_fat',type=float)
        atributes.add_argument('trans_fat',type=float)
        atributes.add_argument('cholesterol',type=float)
        atributes.add_argument('sodium',type=float)
        atributes.add_argument('fiber',type=float)
        atributes.add_argument('sugar',type=float)
        atributes.add_argument('vitamin_a',type=float)
        atributes.add_argument('vitamin_b1',type=float)
        atributes.add_argument('vitamin_b12',type=float)
        atributes.add_argument('vitamin_c',type=float)
        atributes.add_argument('vitamin_d',type=float)
        atributes.add_argument('vitamin_e',type=float)
        atributes.add_argument('vitamin_k',type=float)
        atributes.add_argument('potassium',type=float)
        atributes.add_argument('zync',type=float)
        atributes.add_argument('magnesium',type=float)
        atributes.add_argument('iron',type=float)
        atributes.add_argument('chromium',type=float)
        dados = atributes.parse_args()
        dados['user_id'] = jwt.get("user_id")
                #verficar se barcode já existe
        food = FoodModel(**dados)
        food.save_food()
        return {'message':'Food created successfully.'}, 201

class FoodSearch(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('instance/banco.db')
        cursor = connection.cursor()
        dados = path_params.parse_args()
        
        dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        parametros = normalize_path_params(**dados_validos)
        print ('\n',parametros)
        if parametros.get('barcode') is not None:
            food = FoodModel.find_by_barcode(parametros.get('barcode'))
            if food:
                return food.json()
            else:
                return{'message': 'Barcode not found.'},404
        elif parametros.get('name') is not None:
            tupla = (parametros.get('name'),parametros.get('limit'),parametros.get('offset'))
            resultado = cursor.execute(search_by_name, tupla)
            foodlist = []
            for linha in resultado:
                foodlist.append({
                    'food_id': linha[0],
                    'user_id': linha[1],
                    'barcode': linha[2],
                    'name': linha[3],
                    'brand': linha[4],
                    'description': linha[7]
                })
            connection.close()
            if len(foodlist)!=0:
                return {'food': foodlist}
            else:
                return{'message': 'Name not found.'},404
        elif parametros.get('description') is not None:
            tupla = (parametros.get('description'),parametros.get('limit'),parametros.get('offset'))
            resultado = cursor.execute(search_by_description, tupla)
            foodlist = []
            for linha in resultado:
                foodlist.append({
                    'food_id': linha[0],
                    'user_id': linha[1],
                    'barcode': linha[2],
                    'name': linha[3],
                    'brand': linha[4],
                    'description': linha[7]
                })
            if len(foodlist)!=0:
                return {'food': foodlist}
            else:
                word_list = parametros.get('description').split()
                if len(word_list) == 1:
                    return{'message': 'Name not found.'},404
                else:
                    query = description_search_query_builder(word_list)
                    resultado = cursor.execute(query)
                    foodlist = []
                    for linha in resultado:
                        foodlist.append({
                            'food_id': linha[0],
                            'user_id': linha[1],
                            'barcode': linha[2],
                            'name': linha[3],
                            'brand': linha[4],
                            'description': linha[7]
                        })
                    connection.close()
                    if len(foodlist)!=0:
                        return {'food': foodlist}
                    return{'message': 'No item found with this description.'},404
        connection.close()        
        return{'message': 'No item found.'},404
        