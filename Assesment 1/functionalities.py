import os
class BankOperations:
    def __init__(self):
        self.file_name = "customers.txt"
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()

    def read_customers(self):
        # Reads customer data from file.
        customers = {}
        with open(self.file_name, "r") as file:
            for line in file:
                acc_no, name, balance, transactions = line.strip().split('|')
                customers[acc_no] = {"name": name, "balance": float(balance), "transactions": transactions.split(',') if transactions else []}
        return customers

    def write_customers(self, customers):
        # Writes customer data to file.
        with open(self.file_name, "w") as file:
            for acc_no, data in customers.items():
                transactions = ','.join(data['transactions'])
                file.write(f"{acc_no}|{data['name']}|{data['balance']}|{transactions}\n")

    def create_account(self):
        # Creates a new customer account.
        customers = self.read_customers()
        name = input("Enter Customer Name: ").strip()
        acc_no = input("Enter Account Number: ").strip()
        if acc_no in customers:
            print("Account already exists!\n")
            return
        balance = float(input("Enter Initial Deposit: ").strip())
        customers[acc_no] = {"name": name, "balance": balance, "transactions": []}
        self.write_customers(customers)
        print(f"Account for {name} created successfully!\n")

    def search_customer(self):
        # Search for a customer by account number.
        customers = self.read_customers()
        acc_no = input("Enter Account Number to search: ").strip()
        if acc_no in customers:
            print(f"Account No: {acc_no}, Name: {customers[acc_no]['name']}, Balance: {customers[acc_no]['balance']}")
        else:
            print("Customer not found!\n")

    def view_customer(self):
        # View details of a specific customer.
        self.search_customer()

    def total_amount_in_bank(self):
        # Calculate and display the total amount in the bank.
        customers = self.read_customers()
        total_amount = sum(cust['balance'] for cust in customers.values())
        print(f"Total Amount in Bank: {total_amount}\n")

    def view_all_customers(self):
        # Displays all customer accounts.
        customers = self.read_customers()
        if not customers:
            print("No customers found!\n")
            return
        print("\nCustomer Accounts:")
        for acc_no, details in customers.items():
            print(f"Account No: {acc_no}, Name: {details['name']}, Balance: {details['balance']}")
        print(f"Total Bank Balance: {sum(cust['balance'] for cust in customers.values())}\n")

    def deposit(self):
        # Allows a customer to deposit money into their account.
        customers = self.read_customers()
        acc_no = input("Enter your Account Number: ").strip()
        if acc_no in customers:
            deposit_amount = float(input("Enter amount to deposit: ").strip())
            customers[acc_no]['balance'] += deposit_amount
            customers[acc_no]['transactions'].append(f"Deposited {deposit_amount}")
            self.write_customers(customers)
            print(f"Deposited {deposit_amount} successfully. New balance: {customers[acc_no]['balance']}\n")
        else:
            print("Account not found!\n")

    def withdraw(self):
        # Allows a customer to withdraw money from their account.
        customers = self.read_customers()
        acc_no = input("Enter your Account Number: ").strip()
        if acc_no in customers:
            withdraw_amount = float(input("Enter amount to withdraw: ").strip())
            if customers[acc_no]['balance'] >= withdraw_amount:
                customers[acc_no]['balance'] -= withdraw_amount
                customers[acc_no]['transactions'].append(f"Withdrew {withdraw_amount}")
                self.write_customers(customers)
                print(f"Withdrew {withdraw_amount} successfully. New balance: {customers[acc_no]['balance']}\n")
            else:
                print("Insufficient funds!\n")
        else:
            print("Account not found!\n")

    def check_balance(self):
        # Allows a customer to check their balance.
        customers = self.read_customers()
        acc_no = input("Enter your Account Number: ").strip()
        if acc_no in customers:
            print(f"Your balance: {customers[acc_no]['balance']}\n")
        else:
            print("Account not found!\n")

    def banker_menu(self):
        # Menu for the banker.
        while True:
            print("\nBanker Menu:")
            print("1. Create Customer Account")
            print("2. Search Customer")
            print("3. View Customer")
            print("4. View All Customers")
            print("5. Total Amount in Bank")
            print("6. Exit")
            choice = input("Enter choice: ").strip()
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.search_customer()
            elif choice == '3':
                self.view_customer()
            elif choice == '4':
                self.view_all_customers()
            elif choice == '5':
                self.total_amount_in_bank()
            elif choice == '6':
                break
            else:
                print("Invalid choice!\n")

    def customer_menu(self):
        # Menu for the customer.
        while True:
            print("\nCustomer Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = input("Enter choice: ").strip()
            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.check_balance()
            elif choice == '4':
                break
            else:
                print("Invalid choice!\n")
