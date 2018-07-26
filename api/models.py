from database import DatabaseConnection
import uuid
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
import datetime



db_connect = DatabaseConnection()
connect = db_connect.connection
cursor = db_connect.connection.cursor()


class Request:
    def __init__(self, client_name, email, category, request_title, description, department, status='pending...'):
        self.client_name = client_name
        self.email = email
        self.category = category
        self.request_title = request_title
        self.description = description
        self.department = department
        self.status = status


    def create_request(self):
        cursor.execute("INSERT INTO requests(client_name, email, category, request_title, description, department) VALUES('{}', '{}','{}','{}','{}', '{}')".format(
    self.client_name, self.email, self.category, self.request_title, self.description, self.department))
 


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
        cursor.execute("INSERT INTO users(name, email, username, password, is_admin) VALUES('{}', '{}','{}','{}','{}')".format(
        self.name, self.email, self.username, self.password, self.is_admin))
        cursor.close()
    def user_login(self):
        cursor.execute("SELECT * FROM users WHERE username = '{}' and password = '{}'").format(self.username, self.password)    
        cursor.fetchone()

    def get_token(self):
        token = jwt.encode({'email': self.email}, 'secret', algorithm='HS256')
        return token    

    def get_all_users(self):
        self.cursor.execute("SELECT * from users")
        all_users = self.cursor.fetchall()
        return list(all_users)

    def get_user(self, id):
        self.cursor.execute("SELECT * from users where id = '{}'" .format(id))
        user = self.cursor.fetchone()
        return user

    def get_user_by_username(self, username):
        self.cursor.execute("SELECT * from users where username = '{}'" .format(username))
        user = self.cursor.fetchone()
        return user    
    