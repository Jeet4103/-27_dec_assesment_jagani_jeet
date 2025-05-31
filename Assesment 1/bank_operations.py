from file_operations import read_customers, write_customers

def create_account():
    customers = read_customers()
    name = input("Enter Customer Name: ").strip()
    acc_no = input("Enter Account Number: ").strip()
    if acc_no in customers:
        print("Account already exists!\n")
        return
    balance = float(input("Enter Initial Deposit: ").strip())
    customers[acc_no] = {"name": name, "balance": balance, "transactions": []}
    write_customers(customers)
    print(f"Account for {name} created successfully!\n")

def search_customer():
    customers = read_customers()
    acc_no = input("Enter Account Number to search: ").strip()
    if acc_no in customers:
        print(f"Account No: {acc_no}, Name: {customers[acc_no]['name']}, Balance: {customers[acc_no]['balance']}")
    else:
        print("Customer not found!\n")

def total_amount_in_bank():
    customers = read_customers()
    total_amount = sum(cust['balance'] for cust in customers.values())
    print(f"Total Amount in Bank: {total_amount}\n")

def deposit():
    customers = read_customers()
    acc_no = input("Enter your Account Number: ").strip()
    if acc_no in customers:
        deposit_amount = float(input("Enter amount to deposit: ").strip())
        customers[acc_no]['balance'] += deposit_amount
        customers[acc_no]['transactions'].append(f"Deposited {deposit_amount}")
        write_customers(customers)
        print(f"Deposited {deposit_amount} successfully. New balance: {customers[acc_no]['balance']}\n")
    else:
        print("Account not found!\n")

def withdraw():
    customers = read_customers()
    acc_no = input("Enter your Account Number: ").strip()
    if acc_no in customers:
        withdraw_amount = float(input("Enter amount to withdraw: ").strip())
        if customers[acc_no]['balance'] >= withdraw_amount:
            customers[acc_no]['balance'] -= withdraw_amount
            customers[acc_no]['transactions'].append(f"Withdrew {withdraw_amount}")
            write_customers(customers)
            print(f"Withdrew {withdraw_amount} successfully. New balance: {customers[acc_no]['balance']}\n")
        else:
            print("Insufficient funds!\n")
    else:
        print("Account not found!\n")

def check_balance():
    customers = read_customers()
    acc_no = input("Enter your Account Number: ").strip()
    if acc_no in customers:
        print(f"Your balance: {customers[acc_no]['balance']}\n")
    else:
        print("Account not found!\n")

def delete_customer():
    customers = read_customers()
    acc_no = input("Enter the account no. of customer to delete: ").strip()
    if acc_no in customers:
        del customers[acc_no]
        write_customers(customers)  # **Saving the updated dictionary**
        print("Account deleted successfully!\n")
    else:
        print("Account not found!\n")

def update_customer():
    customers = read_customers()
    acc_no = input("Enter the account no. of customer to update: ").strip()
    if acc_no in customers:
        name = input("Enter new Customer Name: ").strip()
        balance = float(input("Enter new balance: ").strip())

        # Preserve transactions instead of resetting them
        customers[acc_no]["name"] = name
        customers[acc_no]["balance"] = balance

        write_customers(customers)  # Save updated data
        print(f"Account {acc_no} updated successfully!\n")
    else:
        print("Account not found!\n")
