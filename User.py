class User:
    def __init__(self, email, password):
        self.userEmail = email
        self.userPassword = password
        self.favorites = []
        self.history = []
