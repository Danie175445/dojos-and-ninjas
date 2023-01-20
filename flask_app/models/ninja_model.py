from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = 'insert into ninjas(dojo_id, first_name, last_name, age) values (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s);'
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)