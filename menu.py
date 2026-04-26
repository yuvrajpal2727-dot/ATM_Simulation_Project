from .operations import display_balance, deposit, withdraw
from .statement import print_statement
from .account import Account

def show_menu():
    """
    Displays the main ATM menu.
    """
    print("\n WELCOME TO THE ATM SYSTEM")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Statement")
    print("5. Exit")
    print("===============================")

def handle_choice(choice: str, account: Account) -> bool:
    """
    Handles the user's menu choice and delegates to respective operations.
    Returns False if the user chooses to exit, otherwise True.
    """
    if choice == '1':
        display_balance(account)
    elif choice == '2':
        try:
            amount = float(input("Enter amount to deposit: $"))
            deposit(account, amount)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")
    elif choice == '3':
        try:
            amount = float(input("Enter amount to withdraw: $"))
            withdraw(account, amount)
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")
    elif choice == '4':
        print_statement(account)
    elif choice == '5':
        print("\nThank you for using our ATM system. Have a great day!\n")
        return False
    else:
        print("Invalid choice. Please specify a number between 1 and 5.")
    
    return True
