
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