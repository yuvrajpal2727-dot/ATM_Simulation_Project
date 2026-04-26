from .account import Account

def print_statement(account: Account):
    """
    Prints a formatted history of all account transactions.
    """
    print("\n========= TRANSACTION STATEMENT =========")
    if not account.transactions:
        print("No transactions found.")
    else:
        print(f"{'Date & Time':<22} | {'Type':<12} | {'Amount':<10} | {'Balance':<10}")
        print("-" * 62)
        for t in account.transactions:
            print(f"{t['timestamp']:<22} | {t['type']:<12} | ${t['amount']:<9.2f} | ${t['balance_after']:<9.2f}")
    print("=========================================\n")
