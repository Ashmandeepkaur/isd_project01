from datetime import date, timedelta
from bank_account.bank_account import BankAccount  # Adjust this if necessary

class InvestmentAccount(BankAccount):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, account_number, account_holder, balance, date_created, management_fee):
        super().__init__(account_number, account_holder, balance, date_created)
        self.date_created = date_created  # Ensure this attribute is set

        try:
            self.__management_fee = float(management_fee)
        except (ValueError, TypeError):
            self.__management_fee = 2.55

    def get_service_charges(self):
        if self.date_created < InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee

    def __str__(self):
        management_fee_str = "${:.2f}".format(self.__management_fee) if self.date_created >= InvestmentAccount.TEN_YEARS_AGO else "Waived"
        return (f"Account Number: {self.account_number} Balance: ${self.balance:.2f}\n"
                f"Date Created: {self.date_created} Management Fee: {management_fee_str} Account Type: Investment")
