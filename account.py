from datetime import datetime

class Account:
    """
    Represents a user's bank account.
    Stores the balance and transaction history.
    """
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance
        self.transactions = []

    def add_transaction(self, type_, amount):
        """
        Adds a transaction to the history with a timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "timestamp": timestamp,
            "type": type_,
            "amount": amount,
            "balance_after": self.balance
        })
