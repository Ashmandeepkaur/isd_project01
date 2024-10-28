from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer class defines the interface for concrete observers 
    that receive notifications from a subject.

    Methods
    update(message: str):
        Called to notify the observer of changes in the subject.
    """
    
    @abstractmethod
    def update(self, message: str):
        """
        Notifies the observer with a message about a state change.

        Args
        message : str
            Information about the change.
        
        Returns: Implemented in sub class.
        """
        pass
