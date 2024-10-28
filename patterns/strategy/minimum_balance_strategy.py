from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy to calculate service charges based on overdraft conditions.

    Attributes
    __overdraft_limit : float
        Maximum allowed overdraft amount.
    __overdraft_rate : float
        Rate for calculating charges on overdrafts.
    """

    def __init__(self, overdraft_limit, overdraft_rate):
        """
        Initializes the strategy with an overdraft limit and rate.

        Args
        overdraft_limit : float
            The limit for overdraft.
        overdraft_rate : float
            The rate for calculating charges.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account):
        """
        Computes service charges based on account's balance and overdraft conditions.

        Args
        account : BankAccount
            The account to check.
        
        Returns
        float
            The calculated service charge.
        """
        # If the balance is greater than or equal to the overdraft limit, charge is the base service charge
        if account.balance >= self.__overdraft_limit:
            return 0.50  # Base service charge

        # If the balance is less than the overdraft limit, calculate the service charge based on the formula
        service_charge = 0.50 + (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        return service_charge
