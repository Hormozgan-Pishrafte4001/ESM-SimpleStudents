


class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password


class Core:
    def __init__(self) -> None:
         
        self.users={}

    def login(self, username, password):
        if username in self.users:
             if password == self.users[username].password:
                   return True 
        return False

    def add_user(self, username, password):
        new_ = User(username, password)
        self.users[username] = new_



