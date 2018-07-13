
class Request:
<<<<<<< HEAD

    def __init__(self, client_name, email, category, request_title, description, department,  request_id):
=======
    def __init__(self, request_id, client_name, email, category, request_title, description, department, request_time):
        self.request_id = request_id
>>>>>>> 8dee14e76f26079f0caf7fa95aa54975ff30355d
        self.client_name = client_name
        self.email = email
        self.category = category
        self.request_title = request_title
        self.description = description
        self.department = department
<<<<<<< HEAD
=======

    def get_request_id(self):
        return self.request_id  

    def get_client_name(self):
        return self.client_name     
    
    def get_email(self):
        return self.email

    def get_category(self):
        return self.category

    def get_request_title(self):
        return self.request_title
    
    def get_description(self):
        return self.description

    def get_department(self):
        return self.department

 

    def update_request(self,request_id, client_name, email, category, request_title, department,  description):
        request_id = int(request_id) 
        new_request_input = {}
        if len(requests) > 0 and request_id <= len(requests):
            new_request_input = {
                'request_id':request_id,
                'clientname':self.client_name,
                'email': self.email,
                'category':self.category,
                'request_title':self.request_title,
                'department':self.department,
                'description':self.description
            }
            requests[request_id] = new_request_input
            return new_request_input
        return new_request_input  

>>>>>>> 8dee14e76f26079f0caf7fa95aa54975ff30355d

        self.request_id = request_id
        

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