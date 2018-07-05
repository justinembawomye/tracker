
class Request:
    users = []
    def __init__(self, request_id, client_name, email, category, request_title, description, department, request_time):
        self.request_id = request_id
        self.client_name = client_name
        self.email = email
        self.category = category
        self.request_title = request_title
        self.description = description
        self.department = department
        # self.request_time = datetime.datetime.now()

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

    # def get_request_time(self):
    #     return self.request_time 

    # def add_request(self,request_id, )

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


    def get_user_id(self):
        return self.user_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password  

    def add_user(self):
        users = []
        """Register new_user"""
        #user_id = len(users)
        self.user_id += 1

        new_user = {
            'user_id':self.user_id,
            'name':self.name,
            'email':self.email,
            'username':self.username,
            'password':self.password
        }

        users.append(new_user)
        return new_user 


    def update_user(self,user_id):
        user_id = int(user_id) 
        new_user_input = {}
        if len(users) > 0 and user_id <= len(users):
            new_user_input = {
                'user_id':user_id,
                'name':self.name,
                'email': self.email,
                'username':self.username,
                'password':self.password
            }
            users[user_id] = new_user_input
            return new_user_input
        return new_user_input  

users = []