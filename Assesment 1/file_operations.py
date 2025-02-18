import os

file_name = "customers.txt"

def read_customers():
    customers = {}
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                acc_no, name, balance, transactions = line.strip().split('|')
                customers[acc_no] = {
                    "name": name,
                    "balance": float(balance),
                    "transactions": transactions.split(',') if transactions else []
                }
    return customers

def write_customers(customers):
    with open(file_name, "w") as file:
        for acc_no, data in customers.items():
            transactions = ','.join(data['transactions'])
            file.write(f"{acc_no}|{data['name']}|{data['balance']}|{transactions}\n")
