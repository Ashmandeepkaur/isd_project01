from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Calculates service charges based on overdraft conditions.

    Attributes
    __overdraft_limit : float
        Maximum allowed overdraft amount.
    __overdraft_rate : float
        Rate for calculating charges on overdrafts.

    Methods
    calculate_service_charges(account):
        Computes charges if the account is overdrawn.
    """
    
    def __init__(self, overdraft_limit, overdraft_rate):
        """
        Initializes the strategy with an overdraft limit and rate.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        
    def calculate_service_charges(self, account):
        """
        Returns charges based on account's overdraft status.
        """
        if account.balance >= self.__overdraft_limit:
            return 0  # No service charge if balance is above or equal to overdraft limit
        
        # Calculate the service charge if the account is overdrawn
        charge = (self.__overdraft_limit - account.balance) * self.__overdraft_rate
        return charge
