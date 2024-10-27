from datetime import date

class InvestmentAccount:
    BASE_SERVICE_CHARGE = 2.55

    def __init__(self, account_number: int, client_number: int, balance: float,
                 creation_date: date, management_fee: float) -> None:
        """
        Initialize an InvestmentAccount instance.

        :args account_number: Unique identifier for the bank account.
        :args client_number: Identifier for the client.
        :args balance: Initial balance of the account.
        :args creation_date: Date the account was created.
        :args management_fee: Management fee for the account.
        """
        self._account_number = account_number
        self._client_number = client_number
        self._balance = balance
        self._creation_date = creation_date
        self.__management_fee = management_fee if isinstance(management_fee, (int, float)) else InvestmentAccount.BASE_SERVICE_CHARGE

    def get_service_charges(self) -> float:
        """
        Calculate service charges based on the age of the account.

        If the account is less than or equal to 10 years old, the management fee is included.

        :return: Total service charges for the account.
        """
        if (date.today() - self._creation_date).days <= 365 * 10:
            return InvestmentAccount.BASE_SERVICE_CHARGE + self.__management_fee
        return InvestmentAccount.BASE_SERVICE_CHARGE

    def __str__(self) -> str:
        if (date.today() - self._creation_date).days <= 365 * 10:
            return (
                f"Account Number: {self._account_number} Balance: ${self._balance:.2f}\n"
                f"Date Created: {self._creation_date} Management Fee: ${self.__management_fee:.2f} "
                "Account Type: Investment"
            )
        return (
            f"Account Number: {self._account_number} Balance: ${self._balance:.2f}\n"
            f"Date Created: {self._creation_date} Management Fee: Waived Account Type: Investment"
        )
