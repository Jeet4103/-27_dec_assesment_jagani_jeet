import os

class Storage:
    # Defining the file names
    def __init__(self):
        self.users_file = "users.txt"
        self.product_file = "product.txt"
        self.order_file = "order.txt"
        self.setup_file()
    
    # Creating the files if they don't exist
    def setup_file(self):
        for file_name in [self.users_file, self.product_file, self.order_file]:
            if not os.path.exists(file_name):
                with open(file_name, "w") as file:
                    file.write("")

    # Reading from a file
    def read_file(self, file_name):
        with open(file_name, "r") as file:
            return [line.strip().split('|') for line in file if line.strip()]

    # Writing to a file
    def write_file(self, file_name, data):
        with open(file_name, "w") as file:
            for row in data:
                file.write('|'.join(map(str, row)) + "\n")

    # Appending data to a file
    def add_to_file(self, file_name, row):
        with open(file_name, "a") as file:
            file.write('|'.join(map(str, row)) + "\n")

    # Saving a user
    def save_user(self, user, password, role):
        data = self.read_file(self.users_file)
        user_id = len(data) + 1  # Generate new user ID
        self.add_to_file(self.users_file, [user_id, user, password, role])
        return user_id  

    # Finding a user
    def find_user(self, user, password, role):
        for row in self.read_file(self.users_file):
            if len(row) >= 4 and row[1] == user and row[2] == password and row[3] == role:
                return row[0]  
        return None  

    # Saving a product
    def save_product(self, product_name, product_price, product_quantity):
        data = self.read_file(self.product_file)
        product_id = len(data) + 1  # Generate product ID
        self.add_to_file(self.product_file, [product_id, product_name, product_price, product_quantity])
        return product_id

    # Getting all products
    def get_products(self):
        return self.read_file(self.product_file)

    # Getting a product by ID
    def get_product_by_id(self, product_id):
        for row in self.read_file(self.product_file):
            if int(row[0]) == int(product_id):
                return row
        return None

    # Deleting a product
    def delete_product(self, product_id):
        data = self.read_file(self.product_file)
        updated_data = [row for row in data if int(row[0]) != int(product_id)]
        if len(data) == len(updated_data):
            return False  # No product found to delete

        self.write_file(self.product_file, updated_data)
        return True

    # Getting all orders for a user
    def get_order(self, user_id):
        return [row for row in self.read_file(self.order_file) if int(row[1]) == int(user_id)]


storage = Storage()
