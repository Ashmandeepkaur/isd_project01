from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract base class for defining service charge calculation strategies.

    Methods
    calculate_service_charges(account):
        Calculates service charges for a given bank account.
        
    This method must be implemented by subclasses.
    """
    
    @abstractmethod
    def calculate_service_charges(self, account):
        """
        Calculates service charges based on the specific strategy.

        Args
        account : BankAccount
            The bank account for which to calculate service charges.

        Returns
        float
            The calculated service charges.
        """
        pass
