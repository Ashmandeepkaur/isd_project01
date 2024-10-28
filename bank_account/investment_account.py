from datetime import date, timedelta
from bank_account.bank_account import BankAccount  # Adjust this if necessary

class InvestmentAccount(BankAccount):
    """
    A class representing an investment account.

    Inherits from BankAccount and adds management fee functionality.
    
    Attributes:
        TEN_YEARS_AGO (date): The date that marks ten years from today.
    """
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number, account_holder, balance, date_created, management_fee):
        """
        Initialize an InvestmentAccount instance.

        :param account_number: Unique identifier for the bank account.
        :param account_holder: Name or identifier for the account holder.
        :param balance: Initial balance of the account.
        :param date_created: Date the account was created.
        :param management_fee: Annual management fee for the account.
        """
        super().__init__(account_number, account_holder, balance, date_created)
        self.date_created = date_created  # Ensure this attribute is set

        # Validate management_fee
        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55  # Default management fee

    def get_service_charges(self):
        """
        Calculate service charges based on the age of the account.

        If the account was created over ten years ago, only the base service charge 
        is applied. Otherwise, the management fee is added to the base service charge.

        :return: Total service charges for the account.
        """
        if self.date_created < InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self):
        """
        Return a string representation of the InvestmentAccount instance.

        This includes the account number, balance, creation date, and management fee 
        status.

        :return: String containing account details including management fee information.
        """
        management_fee_str = "${:.2f}".format(self.__management_fee) if self.date_created >= InvestmentAccount.TEN_YEARS_AGO else "Waived"
        return (f"Account Number: {self.account_number} Balance: ${self.balance:.2f}\n"
                f"Date Created: {self.date_created} Management Fee: {management_fee_str} "
                f"Account Type: Investment")
