from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo_model
class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def save(cls,data):
        query = 'insert into ninjas(dojo_id, first_name, last_name, age) values (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);'
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = 'delete from ninjas where id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def edit(cls,data):
        print('C')
        print(data)
        query = 'update ninjas set dojo_id = %(dojo_id)s, first_name = %(first_name)s, last_name =  %(last_name)s, age = %(age)s where id = %(id)s;'
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = '''
                select * from ninjas left join dojos
                on ninjas.dojo_id = dojos.id
                where ninjas.id = %(id)s;
                '''
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        this_ninja = cls(results[0])
        for key in results[0].keys():
            print(key)
        print('B')
        print('results =',results)
        print('results [0] =',results[0])
        
        dojo_data = {
            "id": results[0]["dojos.id"],
            "name": results[0]["name"],
            "created_at": results[0]["dojos.created_at"],
            "updated_at": results[0]["dojos.updated_at"],
        }
        this_ninja.dojo = dojo_model.Dojo(dojo_data)
        return this_ninja
    # @classmethod
    # def get_one_with_dojoes()