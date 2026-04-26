from atm.account import Account
from atm.menu import show_menu, handle_choice

def main():
    """
    Main execution loop of the ATM system.
    Only controls program flow as per requirements.
    """
    user_account = Account(initial_balance=0.0)

    while True:
        show_menu()
        choice = input("Please select an option (1-5): ")
        
        continue_running = handle_choice(choice, user_account)
        if not continue_running:
            break

if __name__ == "__main__":
    main()
