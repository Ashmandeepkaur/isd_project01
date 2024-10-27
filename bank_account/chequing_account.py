from datetime import date

class ChequingAccount:
    def __init__(self, account_number: int, client_number: int, balance: float,
                 creation_date: date, overdraft_limit: float = -100.00,
                 overdraft_rate: float = 0.05) -> None:
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance
        self._creation_date = creation_date
        self._overdraft_limit = (
            overdraft_limit if isinstance(overdraft_limit, (int, float)) else -100.00
        )
        self._overdraft_rate = (
            overdraft_rate if isinstance(overdraft_rate, (int, float)) else 0.05
        )

    @property
    def overdraft_limit(self) -> float:
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self._overdraft_limit = value

    @property
    def overdraft_rate(self) -> float:
        return self._overdraft_rate

    @overdraft_rate.setter
    def overdraft_rate(self, value: float) -> None:
        if isinstance(value, (int, float)):
            self._overdraft_rate = value

    def update_balance(self, amount: float) -> None:
        self._balance += amount

    def get_service_charges(self) -> float:
        """
        Calculate service charges based on the current balance.

        If the balance exceeds the overdraft limit, a service charge is applied.

        :return: Total service charges for the account.
        """
        excess = max(0.0, self._overdraft_limit - self._balance)
        service_charge = 0.50 + (excess * self._overdraft_rate)
        return self.BASE_SERVICE_CHARGE + (excess * self.__overdraft_rate)


    def __str__(self) -> str:
        return (
            f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}\n"
            f"Overdraft Limit: ${self._overdraft_limit:.2f} "
            f"Overdraft Rate: {self._overdraft_rate * 100:.2f}% Account Type: Chequing"
        )
