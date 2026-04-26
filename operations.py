from .account import Account

def display_balance(account: Account):
    """
    Displays the current balance of the account.
    """
    print(f"\n--- Current Balance ---")
    print(f"Balance: ${account.balance:.2f}")
    print("-----------------------\n")

def deposit(account: Account, amount: float):
    """
    Deposits the specified amount into the account.
    """
    if amount <= 0:
        print("Invalid amount. Deposit must be greater than 0.")
        return False
    
    account.balance += amount
    account.add_transaction("Deposit", amount)
    print(f"Successfully deposited ${amount:.2f}")
    return True

def withdraw(account: Account, amount: float):
    """
    Withdraws the specified amount from the account, checking for sufficient funds.
    """
    if amount <= 0:
        print("Invalid amount. Withdrawal must be greater than 0.")
        return False
    if amount > account.balance:
        print("Insufficient balance for this transaction.")
        return False
    
    account.balance -= amount
    account.add_transaction("Withdrawal", amount)
    print(f"Successfully withdrew ${amount:.2f}")
    return True
