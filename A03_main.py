"""
Description: A client program written to verify implementation 
of the Observer Pattern.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.client import Client # type: ignore


# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
client1 = Client(client_number=12345, first_name="Ashmandeep", last_name="Kaur", email_address="ashmandeepkaur@gmail.com")






# 2. Create a Client object with data of your choice.
chequing_account = ChequingAccount(account_number=12345, client_number=client1.client_number, balance=40.0, overdraft_limit=50.0)



# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.

savings_account = SavingsAccount(account_number=12345, client_number=client1.client_number, balance=300.0, minimum_balance=200.0)



# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 1) to the ChequingAccount object (created in step 2).
chequing_account.attach(client1)

# 4a.  Attach the Client object (created in step 1) to the SavingsAccount object (created in step 2).
savings_account.attach(client1)




# 5a. Create a second Client object with data of your choice.
client2 = Client(client_number=2, first_name="Bob", last_name="Smith", email_address="bob.smith@example.com")

# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
savings_account2 = SavingsAccount(account_number=12345, client_number=client2.client_number, balance=250.0, minimum_balance=150.0)
savings_account2.attach(client2)




# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
transactions = [
    (chequing_account, 'deposit', 20),    # Should not notify
    (chequing_account, 'withdraw', 100),   # Should notify
    (chequing_account, 'withdraw', 30),    # Should notify
    (savings_account, 'withdraw', 100),    # Should not notify
    (savings_account, 'withdraw', 50),     # Should notify
    (savings_account2, 'withdraw', 100),   # Should not notify
    (savings_account2, 'deposit', 20),      # Should not notify
]

for account, action, amount in transactions:
    try:
        if action == 'deposit':
            account.deposit(amount)
            print(f"Deposited ${amount:.2f} to {account.account_number}.")
        elif action == 'withdraw':
            account.withdraw(amount)
            print(f"Withdrew ${amount:.2f} from {account.account_number}.")
    except ValueError as e:
        print(f"Error: {e}")

# Additional transactions that will not notify
try:
    chequing_account.deposit(10)  # Should not notify
    savings_account.withdraw(150)  # Should not notify
except ValueError as e:
    print(f"Error: {e}")

# Final balances
print("Final Balances:")
print(chequing_account)
print(savings_account)
print(savings_account2)
