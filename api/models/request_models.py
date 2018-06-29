class Request:
    def __init__(self, request_id, client_name, email, category, request_title, description, department, request_time):
        self.request_id = request_id
        self.client_name = client_name
        self.email = email
        self.category = category
        self.request_title = request_time
        self.description = description
        self.department = department
        self.request_time = request_time

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

    def get_request_time(self):
        return self.request_time 



    def __repr__(self):
        pass    
requests = []