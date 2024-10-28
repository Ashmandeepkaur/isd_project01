from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from investment_account import InvestmentAccount


class ManagementFeeStrategy:
    TEN_YEARS_AGO = date.today() - timedelta(days=365 * 10)

    def __init__(self, management_fee: float, date_created):
        """
        Initializes with management fee and account creation date.
      
        Args
        management_fee : float
            Fee for management services.
        date_created : date
            Account creation date.
        """
        self.__management_fee = management_fee
        self.__date_created = date_created

    def calculate_service_charges(self, account) -> float:
        """
        Calculates management fees based on account age.
        
        Returns
        float
            Fee if the account is over ten years old; otherwise, zero.
        """
        if account._creation_date < self.TEN_YEARS_AGO:
            return self.management_fee
        else:
            return 0.0
