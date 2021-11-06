users = [['Hashem', '123'], ['Mammad', '456']]


def login(user, pass_):
    for i in range(len(users)):
        if user == users[i][0]:
            if pass_ == users[i][1]:
                return True
            return False
    return False
