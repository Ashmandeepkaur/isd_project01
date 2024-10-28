"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""


from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.savings_account import SavingsAccount
from bank_account.investment_account import InvestmentAccount

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
chequing_account = ChequingAccount(account_number=12345, client_number=1, balance=30.0, overdraft_limit=50.0)


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.


# 3. Print the ChequingAccount created in step 2.
print("Chequing Account:")
print(chequing_account)

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print("Service Charges:", chequing_account.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(25.0)

# 4b. Print the ChequingAccount
print("After Deposit:")
print(chequing_account)

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print("Service Charges:", chequing_account.get_service_charges())


print("===================================================")

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(account_number=12345, client_number=2, balance=1000.0, minimum_balance=200.0)


# 6. Print the SavingsAccount created in step 5.
print("Savings Account:")
print(savings_account)

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print("Service Charges:", savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings_account.withdraw(900.0)

# 7b. Print the SavingsAccount.
print("After Withdrawal:")
print(savings_account)

# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print("Service Charges:", savings_account.get_service_charges())


print("===================================================")

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account_recent = InvestmentAccount(account_number=12345, client_number=3, balance=1500.0, creation_date=date.today(), management_fee=15.0)


# 9a. Print the InvestmentAccount created in step 8.
print("Investment Account (Recent):")
print(investment_account_recent)

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print("Service Charges:", investment_account_recent.get_service_charges())


# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account_old = InvestmentAccount(account_number=456789, client_number=4, balance=2000.0, creation_date=date(2010, 1, 1), management_fee=15.0)


# 11a. Print the InvestmentAccount created in step 10.
print("Investment Account (Old):")
print(investment_account_old)

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print("Service Charges:", investment_account_old.get_service_charges())


print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
chequing_account.withdraw(chequing_account.get_service_charges())
savings_account.withdraw(savings_account.get_service_charges())
investment_account_recent.withdraw(investment_account_recent.get_service_charges())
investment_account_old.withdraw(investment_account_old.get_service_charges())


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print("Final Accounts:")
print(chequing_account)
print(savings_account)
print(investment_account_recent)
print(investment_account_old)

