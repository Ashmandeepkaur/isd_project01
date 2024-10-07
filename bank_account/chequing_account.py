from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    BASE_SERVICE_CHARGE = 0.50  # Base service charge constant

    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate):
        """
        Initialize a ChequingAccount instance.

        :param account_number: Unique identifier for the bank account.
        :param client_number: Identifier for the client.
        :param balance: Initial balance of the account.
        :param date_created: Date the account was created.
        :param overdraft_limit: Maximum amount the account can be overdrawn.
        :param overdraft_rate: Interest rate charged on the overdrawn amount.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # Validate overdraft_limit
        try:
            self.overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.overdraft_limit = -100.00  # Default overdraft limit

        # Validate overdraft_rate
        try:
            self.overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.overdraft_rate = 0.05  # Default overdraft rate

    def __str__(self):
        """
        Return a string representation of the ChequingAccount instance.

        :return: String containing account details including overdraft information.
        """
        return (f"{super().__str__()}"
                f"Overdraft Limit: ${self.overdraft_limit:,.2f} "
                f"Overdraft Rate: {self.overdraft_rate * 100:.2f}% "
                f"Account Type: Chequing")

    def get_service_charges(self):
        """Calculate service charges based on the balance."""
        if self.balance < self.overdraft_limit:
           overdrawn_amount = self.overdraft_limit - self.balance  # This will give a positive amount
           return self.BASE_SERVICE_CHARGE + (overdrawn_amount * self.overdraft_rate)  # Calculate the additional charge
        return self.BASE_SERVICE_CHARGE  # Just the base charge if within limit
