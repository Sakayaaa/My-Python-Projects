from account import *

try:
    title = input("Enter your title: ").lower()
    account_id = input("Enter your account id: ")
    amount = input("Enter your amount: ")

    account_1 = Account(title, account_id, amount)
    print(account_1)

except Exception as e:
    print(f"Error: {e}")