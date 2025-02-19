from menus import banker_menu, customer_menu

def main():
    while True:
        print("\nWelcome to the Bank!")
        print("1. Banker Menu")
        print("2. Customer Menu")
        print("3. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            banker_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

main()
