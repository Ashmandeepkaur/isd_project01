from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    SERVICE_CHARGE_PREMIUM = 2.00
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number, client_number, balance, opening_date, minimum_balance):
        super().__init__(account_number, client_number, balance, opening_date)
        try:
            self.minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.minimum_balance = 50.00

    def __str__(self):
        return (f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"
                f"Minimum Balance: ${self.minimum_balance:,.2f} Account Type: Savings")

    def get_service_charges(self):
        if self.balance >= self.minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount} must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise ValueError(f"Withdrawal would reduce balance below minimum: ${self.minimum_balance}.")
        super().withdraw(amount)
