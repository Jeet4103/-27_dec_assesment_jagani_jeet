from bank_operations import *

def banker_menu():
    while True:
        print("\nBanker Menu:")
        print("1. Create Customer Account")
        print("2. Delete Customer")
        print("3. View Customer")
        print("4. Update customer")
        print("5. Total Amount in Bank")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            create_account()
        elif choice == '2':
            delete_customer()
        elif choice == '3':
            search_customer()  # For simplicity, using the same function for viewing a customer
        elif choice == '4':
            update_customer()
        elif choice == '5':
            total_amount_in_bank()
        elif choice == '6':
            break
        else:
            print("Invalid choice!\n")

def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            break
        else:
            print("Invalid choice!\n")
