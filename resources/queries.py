def normalize_path_params(barcode=None, name=None,description=None, limit = 50, offset = 0, **dados):
        return {
            'barcode': barcode,
            'name': name,
            'limit': limit,
            'description': description,
            'offset': offset}

def normalize_meal_serch_params(meal_template_name=None, user_id=None,description=None, limit = 50, offset = 0, **dados):
        return {
            'meal_template_name': meal_template_name,
            'limit': limit,
            'user_id': user_id,
            'offset': offset
            }
    


search_by_name = "SELECT * FROM food \
            WHERE name like '%'||?||'%' \
            LIMIT ? OFFSET ?"
search_by_description = "SELECT * FROM food \
            WHERE description like '%'||?||'%' \
            LIMIT ? OFFSET ?"

search_meal_template_by_name = "SELECT * FROM meal_template\
                                WHERE meal_template_name like '%'||?||'%'\
                                and user_id = ?\
                                LIMIT? OFFSET ?"

def description_search_query_builder(word_list):
        print('\n',word_list,'\n')
        base_query = "SELECT * FROM food WHERE "
        for i in word_list:
            base_query = base_query + "description like "
            base_query = base_query + "'%"+i+"%' " + "AND "
        base_query = base_query[:-4]    
        return(base_query)
