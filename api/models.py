from database import DatabaseConnection

db_connect = DatabaseConnection()
connect = db_connect.connection
cursor = db_connect.connection.cursor()
class Request:
    def __init__(self, client_name, email, category, request_title, description, department,  request_id):
        self.request_id = request_id
        self.client_name = client_name
        self.email = email
        self.category = category
        self.request_title = request_title
        self.description = description
        self.department = department
       

    def __repr__(self):
        return repr(self.__dict__) 

requests = []        


class User(DatabaseConnection):
    
    def __init__(self, name, email, username, password, is_admin=False):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def add_user(self):
        cursor.execute("INSERT INTO users VALUES('{}', '{}','{}','{}','{}')".format(self.name, self.email, self.username, self.password, self.is_admin))
        connect.commit()
        cursor.close()