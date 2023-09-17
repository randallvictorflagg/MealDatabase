from sql_alchemy import banco
from datetime import datetime
from resources.extend_date import extend_license


class UserModel(banco.Model):
    __tablename__ = 'users'
    user_id = banco.Column(banco.Integer, primary_key = True)
    store_name = banco.Column(banco.String(30))
    login = banco.Column (banco.String(40))
    password = banco.Column (banco.String)
    status = banco.Column (banco.Integer)
    type = banco.Column(banco.Integer)
    createdIn = banco.Column(banco.String(30))
    validUntil = banco.Column(banco.String(30))
    

    def __init__(self, login, password, status, store_name, type):
        self.login = login
        self.password = password
        self.status = status
        self.type = type
        self.store_name = store_name
        self.createdIn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.validUntil = extend_license(self.createdIn, 3)
        
    
    def json(self):
        return {
            'user_id': self.user_id,
            'login': self.login,
            'status': self.status,
            'store_name': self.store_name,
            'type': self.type,
            'createdIn': self.createdIn,
            'validUntil': self.validUntil

        }
    
    @classmethod
    def find_user(cls, user_id):
        user = cls.query.filter_by(user_id = user_id).first() #SELECT * FROM users WHERE user_id = user_id
        if user:
            return user
        return None
    
    @classmethod
    def find_by_login(cls, login):
        user = cls.query.filter_by(login = login).first()
        if user:
            return user
        return None
    
    def delete_user(self): #deletar todos os alimentos de um user
        pass

    def update_user(self,user):
        self.login = user.login
        self.password = user.password
        self.status = user.status
        self.type = user.type
        self.store_name = user.store_name
        self.validUntil = user.validUntil

    
    def  save_user(self):
        banco.session.add(self)
        banco.session.commit()
    
    def delete_user(self):
        banco.session.delete(self)
        banco.session.commit()
    
    