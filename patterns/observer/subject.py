class Subject:
    """
    The Subject class maintains a list of observers and notifies them of changes.

    Attributes
    _observers : list
        A list of attached observers.

    Methods
    attach(observer):
        Adds an observer to the list.

    detach(observer):
        Removes an observer from the list.

    notify(message: str):
        Notifies all attached observers with the given message.
    """

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        Adds an observer to the observer list.

        Args
        observer : Observer
            The observer to be added.
        
        Returns
        Implemented in sub class.
        """
        self._observers.append(observer)

    def detach(self, observer):
        """
        Removes an observer from the observer list.

        Args
        observer : Observer
            The observer to be removed.
        
        Returns
        Implemented in sub class.
        """
        self._observers.remove(observer)

    def notify(self, message):
        """
        Notifies all attached observers with a message.

        Args
        message : str
            The message to send to observers.
        
        Returns
        Implemented in sub class.
        """
        for observer in self._observers:
            observer.update(message)
