from bank_account.bank_account import BankAccount

class ChequingAccount(BankAccount):
    BASE_SERVICE_CHARGE = 0.50  # Assuming there's a base service charge constant

    def __init__(self, account_number, client_number, balance, date_created, overdraft_limit, overdraft_rate):
        super().__init__(account_number, client_number, balance, date_created)

        # Validate overdraft_limit
        try:
            self.overdraft_limit = float(overdraft_limit)
        except (ValueError, TypeError):
            self.overdraft_limit = -100.00  # Default value

        # Validate overdraft_rate
        try:
            self.overdraft_rate = float(overdraft_rate)
        except (ValueError, TypeError):
            self.overdraft_rate = 0.05  # Default value

    def __str__(self):
        return (f"{super().__str__()}"
                f"Overdraft Limit: ${self.overdraft_limit:,.2f} Overdraft Rate: {self.overdraft_rate * 100:.2f}% Account Type: Chequing")
    
    
    def get_service_charges(self):
        """Calculate service charges based on the balance."""
        if self.balance < self.overdraft_limit:
            overdrawn_amount = self.balance - self.overdraft_limit  # This will be negative
            return 0.50 + (-overdrawn_amount) * self.overdraft_rate  # Use positive amount for charge
        return 0.50  # Just the base charge if within limit

