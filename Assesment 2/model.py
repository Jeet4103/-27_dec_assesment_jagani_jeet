from File_handling import storage

class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.id = None

    def register(self, role):
        self.id = storage.save_user(self.user, self.password, role)
        return bool(self.id)

    def login(self, role):
        self.id = storage.find_user(self.user, self.password, role)
        return bool(self.id)

class Manager(User):
    def __init__(self, user, password):
        super().__init__(user, password)

class Customer(User):
    def __init__(self, user, password):
        super().__init__(user, password)
        self.balance = 0  

    def add_balance(self, amount):
        self.balance += amount
        return self.balance
