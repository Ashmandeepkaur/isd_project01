from datetime import date
from bank_account.bank_account import BankAccount

class SavingsAccount(BankAccount):
    """
    A class representing a savings account.

    Inherits from BankAccount and includes minimum balance and service charge functionality.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): Premium service charge multiplier for balances below minimum.
        BASE_SERVICE_CHARGE (float): Base service charge applied to the account.
    """
    SERVICE_CHARGE_PREMIUM = 2.00
    BASE_SERVICE_CHARGE = 0.50

    def __init__(self, account_number: int, client_number: int, balance: float,
                 opening_date: date, minimum_balance: float) -> None:
        """
        Initialize a SavingsAccount instance.

        :args account_number: Unique identifier for the bank account.
        :args client_number: Identifier for the client.
        :args balance: Initial balance of the account.
        :args opening_date: Date the account was opened.
        :args minimum_balance: Minimum balance required to avoid additional service charges.
        """
        super().__init__(account_number, client_number, balance, opening_date)
        try:
            self.minimum_balance = float(minimum_balance)
        except (ValueError, TypeError):
            self.minimum_balance = 50.00  # Default minimum balance

    def __str__(self) -> str:
        """
        Return a string representation of the SavingsAccount instance.

        This includes the account number, balance, minimum balance, and account type.

        :return: String containing account details.
        """
        return (f"Account Number: {self.account_number} Balance: ${self.balance:,.2f}\n"
                f"Minimum Balance: ${self.minimum_balance:,.2f} Account Type: Savings")

    def get_service_charges(self) -> float:
        """
        Calculate service charges based on the current balance.

        If the balance is above or equal to the minimum balance, the base service charge is applied.
        Otherwise, a premium service charge is applied.

        :return: Total service charges for the account.
        """
        if self.balance >= self.minimum_balance:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM

    def deposit(self, amount: float) -> None:
        """
        Deposit a specified amount into the savings account.

        :args amount: The amount to be deposited.
        :raises ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a specified amount from the savings account.

        :args amount: The amount to be withdrawn.
        :raises ValueError: If the withdrawal amount is not positive or if it would reduce the balance below the minimum.
        """
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount} must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise ValueError(f"Withdrawal would reduce balance below minimum: ${self.minimum_balance}.")
        super().withdraw(amount)
