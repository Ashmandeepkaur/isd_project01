import re
from datetime import datetime
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email

class Client(Observer):
    """
    A class representing a client with personal and contact information, and 
    implements the Observer pattern to receive notifications.

    Attributes:
        client_number (int): The unique identifier for the client.
        first_name (str): The first name of the client.
        last_name (str): The last name of the client.
        email_address (str): The email address of the client.

    Methods:
        __str__():
            Returns a string representation of the client.
        update(message):
            Sends a notification email to the client.
    """

    def __init__(self, client_number, first_name, last_name, email_address="invalidemail@default.com"):
        """
        Initializes a new Client instance.

        Args:
            client_number (int): The unique identifier for the client.
            first_name (str): The first name of the client.
            last_name (str): The last name of the client.
            email_address (str): The email address of the client (optional).

        Raises:
            ValueError: If any of the attributes are invalid.
        """
        self.client_number = client_number
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address  # Validated in the setter

    @property
    def client_number(self):
        """Returns the client number."""
        return self._client_number

    @client_number.setter
    def client_number(self, value):
        """Sets the client number."""
        if not isinstance(value, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = value

    @property
    def first_name(self):
        """Returns the first name of the client."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Sets the first name of the client."""
        if not value:
            raise ValueError("First name cannot be blank.")
        self._first_name = value

    @property
    def last_name(self):
        """Returns the last name of the client."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Sets the last name of the client."""
        if not value:
            raise ValueError("Last name cannot be blank.")
        self._last_name = value

    @property
    def email_address(self):
        """Returns the email address of the client."""
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        """Sets the email address of the client."""
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, value):
            self._email_address = "invalidemail@default.com"
        else:
            self._email_address = value

    def update(self, message):
        """
        Sends a notification email to the client when updates occur.

        Args:
            message (str): The notification message to send.
        """
        subject = f"ALERT: Unusual Activity: {datetime.now()}"
        full_message = f"Notification for {self.client_number}: {self.first_name} {self.last_name}: {message}"
        simulate_send_email(subject, full_message)

    def __str__(self):
        """Returns a string representation of the client."""
        return f"Client: {self.first_name} {self.last_name} ({self.client_number})"
