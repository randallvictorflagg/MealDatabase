from datetime import datetime
import sqlite3

def inactivate_expired_users():
    connection = sqlite3.connect('instance/banco.db')
    cursor = connection.cursor()
    search = "select * from users where validUntil < date('now') and status = 1"
    update = "update users set status = 0 where validUntil < date('now') and status = 1"
    result = cursor.execute(search)
    expired_users_list = []
    for linha in result:
        expired_users_list.append({
            'user_id':linha[0]
        })
    if len(expired_users_list) != 0:
        print("Inactivating expired users: ",expired_users_list)
    cursor.execute(update)
    connection.commit()
    connection.close()   

def delete_expired_meals():
    connection = sqlite3.connect('instance/banco.db')
    cursor = connection.cursor()
    delete = "DELETE FROM single_meal WHERE date(expiration_date,'+5 days') < date('now')"
    cursor.execute(delete)
    connection.commit()
    connection.close()   
   
def job():
    print("I'm working -->",datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
