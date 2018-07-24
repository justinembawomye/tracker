
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


class User:
    
    def __init__(self, user_id, name, email, username, password):
        self.user_id = 0
        self.name = name
        self.email = email
        self.username = username
        self.password = password

users = []