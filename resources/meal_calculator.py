from models.food import FoodModel

def meal_calculator(meal_template):
    for index in meal_template.composition:
        food = FoodModel.find_food(index['food_id'])
        if food:
            try:
                nutrient_attributes = [ "calories", "carbohydrate", "protein", "total_fat", "saturated_fat", "polyunsaturated_fat", "monounsaturated_fat", "trans_fat",\
                                       "cholesterol", "sodium", "fiber", "sugar", "vitamin_a", "vitamin_b1", "vitamin_b12", "vitamin_c", "vitamin_d", "vitamin_e", "vitamin_k", "potassium", "zync", "magnesium", "iron", "chromium"]
                for attribute in nutrient_attributes:
                    meal_template_value = getattr(meal_template, attribute, 0)
                    if meal_template_value is None:
                        meal_template_value = 0
                    food_value = getattr(food, attribute, 0.0)
                    food_amount = float(index["food_amount"])
                    serving_amount = float(food.serving_amount)
                    setattr(meal_template, attribute, (meal_template_value + (food_value * food_amount) / serving_amount))
            except Exception as e:
                print(e)
                return "Error calculating meal nutritional value."
        else:
            return "Food not found."
    return meal_template

   