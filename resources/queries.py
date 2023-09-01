def normalize_path_params(barcode=None, name=None,description=None, limit = 50, offset = 0, **dados):
        return {
            'barcode': barcode,
            'name': name,
            'limit': limit,
            'description': description,
            'offset': offset}
    


search_by_name = "SELECT * FROM food \
            WHERE name like '%'||?||'%' \
            LIMIT ? OFFSET ?"
search_by_description = "SELECT * FROM food \
            WHERE description like '%'||?||'%' \
            LIMIT ? OFFSET ?"

def search_split_description(search):
        teste = search.split()
        print('\n',teste,'\n')