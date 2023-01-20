from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = 'select * from dojos;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        print(results)
        dojos_list = []
        for dojo in results:
            dojos_list.append(cls(dojo))
        return dojos_list
    
    @classmethod
    def get_one(cls,data):
        query = 'select * from dojos where id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return cls(results[0])

    @classmethod
    def save(cls,data):
        query = "insert into dojos (name) values ( %(name)s);"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def get_ninjas_in_dojos(cls,data):
        query = 'select * from dojos left join ninjas on dojos.id = ninjas.dojo_id where dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        print(results)
        d = cls(results[0])
        for i in results:
            n = {
                "id": i['ninjas.id'],
                'dojo_id': i['dojo_id'],
                "first_name": i['first_name'],
                'last_name': i['last_name'],
                'age': i['age'],
                'created_at': i['ninjas.created_at'],
                'updated_at': i['ninjas.updated_at']
            }
            d.ninjas.append(Ninja(n))
        return d

