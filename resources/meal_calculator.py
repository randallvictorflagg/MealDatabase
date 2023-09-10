from models.meal_template import MealTemplateModel
from models.food import FoodModel

def meal_calculator(meal_template):
    for index in meal_template.composition:
        food = FoodModel.find_food(index['food_id'])
        if food:
            try:
                meal_template.calories = float(0 if meal_template.calories is None else meal_template.calories) + (float(0 if food.calories is None else food.calories) * float(index["food_amount"]))/float(food.serving_amount)
                meal_template.carbohydrate =  float(0 if meal_template.carbohydrate is None else meal_template.carbohydrate) + (float(0 if food.carbohydrate is None else food.carbohydrate) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.protein =  float(0 if meal_template.protein is None else meal_template.protein) + (float(0 if food.protein is None else food.protein) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.total_fat =  float(0 if meal_template.total_fat is None else meal_template.total_fat) + (float(0 if food.total_fat is None else food.total_fat) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.saturated_fat =  float(0 if meal_template.saturated_fat is None else meal_template.saturated_fat) + (float(0 if food.saturated_fat is None else food.saturated_fat) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.polyunsaturated_fat =  float(0 if meal_template.polyunsaturated_fat is None else meal_template.polyunsaturated_fat) + (float(0 if food.polyunsaturated_fat is None else food.polyunsaturated_fat) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.monounsaturated_fat =  float(0 if meal_template.monounsaturated_fat is None else meal_template.monounsaturated_fat) + (float(0 if food.monounsaturated_fat is None else food.monounsaturated_fat) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.trans_fat = float(0 if meal_template.trans_fat is None else meal_template.trans_fat) + (float(0 if food.trans_fat is None else food.trans_fat) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.cholesterol =  float(0 if meal_template.cholesterol is None else meal_template.cholesterol) + (float(0 if food.cholesterol is None else food.cholesterol) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.sodium =  float(0 if meal_template.sodium is None else meal_template.sodium) + (float(0 if food.sodium is None else food.sodium) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.fiber =  float(0 if meal_template.fiber is None else meal_template.fiber) + (float(0 if food.fiber is None else food.fiber) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.sugar =  float(0 if meal_template.sugar is None else meal_template.sugar) + (float(0 if food.sugar is None else food.sugar) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.vitamin_a =   float(0 if meal_template.vitamin_a is None else meal_template.vitamin_a) + (float(0 if food.vitamin_a is None else food.vitamin_a) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.vitamin_b1 =  float(0 if meal_template.vitamin_b1 is None else meal_template.vitamin_b1) + (float(0 if food.vitamin_b1 is None else food.vitamin_b1) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.vitamin_b12 =  float(0 if meal_template.vitamin_b12 is None else meal_template.vitamin_b12) + (float(0 if food.vitamin_b12 is None else food.vitamin_b12) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.vitamin_c =  float(0 if meal_template.vitamin_c is None else meal_template.vitamin_c) + (float(0 if food.vitamin_c is None else food.vitamin_c) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.vitamin_d =  float(0 if meal_template.vitamin_d is None else meal_template.vitamin_d) + (float(0 if food.vitamin_d is None else food.vitamin_d) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.vitamin_e =  float(0 if meal_template.vitamin_e is None else meal_template.vitamin_e) + (float(0 if food.vitamin_e is None else food.vitamin_e) *  float(index["food_amount"]))/float(food.serving_amount) 
                meal_template.vitamin_k =  float(0 if meal_template.vitamin_k is None else meal_template.vitamin_k) + (float(0 if food.vitamin_k is None else food.vitamin_k) *  float(index["food_amount"]))/float(food.serving_amount) 
                meal_template.potassium =  float(0 if meal_template.potassium is None else meal_template.potassium) + (float(0 if food.potassium is None else food.potassium) *  float(index["food_amount"]))/float(food.serving_amount) 
                meal_template.zync =  float(0 if meal_template.zync is None else meal_template.zync) + (float(0 if food.zync is None else food.zync) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.magnesium = float(0 if meal_template.magnesium is None else meal_template.magnesium) + (float(0 if food.magnesium is None else food.magnesium) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.iron = float(0 if meal_template.iron is None else meal_template.iron) + (float(0 if food.iron is None else food.iron) *  float(index["food_amount"]))/float(food.serving_amount)
                meal_template.chromium = float(0 if meal_template.chromium is None else meal_template.chromium) + (float(0 if food.chromium is None else food.chromium) *  float(index["food_amount"]))/float(food.serving_amount)

            except:
                return "Error calculating meal nutritional value."
        else:
            return "Food not found."
    return meal_template

   