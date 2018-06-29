requests = []

class User:
    def __init__(self, name, email, username, password):
        # self.user_id = user_id
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    # def get_user_id(self):
    #     return self.user_id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password    


    def __repr__(self):
        pass


