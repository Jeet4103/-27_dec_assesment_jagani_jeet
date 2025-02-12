# main.py
import sys
from functionalities import *

def main_menu():
    """Main menu for selecting module."""
    bank = BankOperations()
    while True:
        print("\nBank Management System")
        print("1. Banker")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            bank.banker_menu()
        elif choice == '2':
            bank.customer_menu()
        elif choice == '3':
            print("Exiting system. Thank you!")
            sys.exit()
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main_menu()