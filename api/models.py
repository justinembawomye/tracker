
class Request:
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


    def __repr__(self):
        return repr(self.__dict__) 

requests = []        


class User:
    def __init__(self, user_id, name, email, username, password):
        self.user_id = user_id
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

    def new_user(self):
        """Register new_user"""

        new_user = {
            'user_id':self.user_id,
            'name':self.name,
            'email':self.email,
            'username':self.username,
            'password':self.password
        }

        users.append(new_user)
        return new_user   

users = []