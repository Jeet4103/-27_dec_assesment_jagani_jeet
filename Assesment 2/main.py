from model import Manager, Customer
from File_handling import storage

class ProductManagementApp:
    def __init__(self):
        self.current_user = None

    def main_menu(self):
        while True:
            print("\nWelcome to Product Management System")
            print("1. Manager")
            print("2. Customer")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.user_menu()
            elif choice == 2:
                self.customer_menu()
            elif choice == 3:
                exit()
            else:
                print("Invalid choice")

    def user_menu(self):
        while True:
            print("\nManager's Menu")
            print("1. Register")
            print("2. Login")
            print("3. Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.register("manager")
            elif choice == 2:
                self.login("manager")
                if self.current_user:
                    self.manager_menu()
            elif choice == 3:
                break
            else:
                print("Invalid choice")

    def customer_menu(self):
        while True:
            print("\nCustomer's Menu")
            print("1. Register")
            print("2. Login")
            print("3. Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.register("customer")
            elif choice == 2:
                self.login("customer")
                if self.current_user:
                    self.customer_dashboard()
            elif choice == 3:
                break
            else:
                print("Invalid choice")

    def register(self, role):
        user = input("Enter user name: ")
        password = input("Enter password: ")
        user_obj = Manager(user, password) if role == "manager" else Customer(user, password)
        
        if user_obj.register(role):
            print(f"{role.capitalize()} registered successfully!")
        else:
            print("Registration failed!")

    def login(self, role):
        user = input("Enter user name: ")
        password = input("Enter password: ")
        user_obj = Manager(user, password) if role == "manager" else Customer(user, password)

        if user_obj.login(role):
            print(f"{role.capitalize()} logged in successfully!")
            self.current_user = user_obj
        else:
            print("Login failed!")

    def manager_menu(self):
        while True:
            print("\nManager's Menu")
            print("1. Add Product")
            print("2. View Stock")
            print("3. Remove Product")
            print("4. Logout")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_product()
            elif choice == 2:
                self.view_stock()
            elif choice == 3:
                self.remove_product()
            elif choice == 4:
                self.current_user = None
                break
            else:
                print("Invalid choice")

    def customer_dashboard(self):
        while True:
            print("\nCustomer's Menu")
            print("1. Buy Product")
            print("2. View Order")
            print("3. Add Balance")
            print("4. Logout")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.buy_product()
            elif choice == 2:
                self.view_order()
            elif choice == 3:
                amount = float(input("Enter amount: "))
                print(f"Your balance is {self.current_user.add_balance(amount)}")
            elif choice == 4:
                self.current_user = None
                break
            else:
                print("Invalid choice")

    def buy_product(self):
        """ Allows a customer to buy a product if they have enough balance """
        print("\nAvailable Products:")
        self.view_stock()

        product_id = int(input("Enter product ID to buy: "))
        quantity = int(input("Enter quantity: "))

        product = storage.get_product_by_id(product_id)
        if product:
            product_id, name, price, stock = int(product[0]), product[1], float(product[2]), int(product[3])

            total_cost = price * quantity
            if quantity > stock:
                print("Sorry, not enough stock available.")
            elif self.current_user.balance < total_cost:
                print("Insufficient balance! Please add more funds.")
            else:
                self.current_user.balance -= total_cost
                storage.delete_product(product_id)  
                storage.add_to_file("order.txt", [self.current_user.id, product_id, name, quantity, total_cost])
                print(f"Purchase successful! You bought {quantity} x {name} for {total_cost}.")
        else:
            print("Invalid product ID!")

    def add_product(self):
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))

        if storage.save_product(product_name, product_price, product_quantity):
            print("Product added successfully!")
        else:
            print("Product not added!")

    def view_stock(self):
        stocks = storage.get_products()
        if stocks:
            print("ID\tName\tPrice\tQuantity")
            for stock in stocks:
                print(f"{stock[0]}\t{stock[1]}\t{stock[2]}\t{stock[3]}")
        else:
            print("No stocks available")

    def remove_product(self):
        product_id = int(input("Enter product ID to remove: "))
        if storage.delete_product(product_id):
            print("Product removed successfully!")
        else:
            print("Product not found!")

    def view_order(self):
        orders = storage.get_order(self.current_user.id)
        if orders:
            print("Your Orders:")
            print("ID\tProduct ID\tProduct Name\tQuantity\tTotal Cost")
            for order in orders:
                print(f"{order[0]}\t{order[1]}\t{order[2]}\t{order[3]}\t{order[4]}")
        else:
            print("No orders found!")

app = ProductManagementApp()
app.main_menu()
