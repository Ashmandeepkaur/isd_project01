class BankAccount:
    """
    A class representing a bank account.

    Attributes:
        account_number (int): The account number of the bank account.
        client_number (int): The client number associated with the account.
        balance (float): The current balance of the account.

    Methods:
        update_balance(amount):
            Updates the account balance by the specified amount.
        deposit(amount):
            Deposits a specified amount into the account.
        withdraw(amount):
            Withdraws a specified amount from the account.
        __str__():
            Returns a string representation of the bank account.
    """

    def __init__(self, account_number: int, client_number: int, balance: float = 0.0):
        """
        Initializes a new BankAccount instance.

        Args:
            account_number (int): The account number for the bank account.
            client_number (int): The client number for the bank account.
            balance (float, optional): The initial balance of the account. Defaults to 0.0.

        Raises:
            ValueError: If `account_number` or `client_number` is not an integer.
        """
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        self._account_number = account_number

        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = client_number

        try:
            self._balance = float(balance)
        except ValueError:
            self._balance = 0.0

    @property
    def account_number(self):
        """
        Returns the account number.

        Returns:
            int: The account number.
        """
        return self._account_number

    @property
    def client_number(self):
        """
        Returns the client number.

        Returns:
            int: The client number.
        """
        return self._client_number

    @property
    def balance(self):
        """
        Returns the current balance.

        Returns:
            float: The current balance.
        """
        return self._balance

    def update_balance(self, amount):
        """
        Updates the account balance by adding the specified amount.

        Args:
            amount (float or str): The amount to add to the balance.

        If `amount` cannot be converted to a float, the balance is not updated.
        """
        try:
            amount = float(amount)
            self._balance += amount
        except ValueError:
            pass

    def deposit(self, amount):
        """
        Deposits a specified amount into the account.

        Args:
            amount (float or str): The amount to deposit.

        Raises:
            ValueError: If `amount` is not numeric or is less than or equal to 0.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account.

        Args:
            amount (float or str): The amount to withdraw.

        Raises:
            ValueError: If `amount` is not numeric, is less than or equal to 0, or exceeds the current balance.
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        
        if amount <= 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        if amount > self._balance:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed the account balance: ${self._balance:,.2f}.")
        
        self.update_balance(-amount)

    def __str__(self):
        """
        Returns a string representation of the bank account.

        Returns:
            str: A string summarizing the account number and balance.
        """
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
