import re

class Client:
    """
    A class representing a client with personal and contact information.

    Attributes:
        client_number (int): The unique identifier for the client.
        first_name (str): The first name of the client.
        last_name (str): The last name of the client.
        email_address (str): The email address of the client.

    Methods:
        __str__():
            Returns a string representation of the client.
    """

    def __init__(self, client_number, first_name, last_name, email_address):
        """
        Initializes a new Client instance.

        Args:
            client_number (int): The unique identifier for the client.
            first_name (str): The first name of the client.
            last_name (str): The last name of the client.
            email_address (str): The email address of the client.

        Raises:
            ValueError: If any of the attributes are invalid.
        """
        self.client_number = client_number
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    @property
    def client_number(self):
        """
        Returns the client number.

        Returns:
            int: The client number.
        """
        return self._client_number

    @client_number.setter
    def client_number(self, value):
        """
        Sets the client number.

        Args:
            value (int): The unique identifier for the client.

        Raises:
            ValueError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise ValueError("Client number must be an integer.")
        self._client_number = value

    @property
    def first_name(self):
        """
        Returns the first name of the client.

        Returns:
            str: The first name.
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Sets the first name of the client.

        Args:
            value (str): The first name of the client.

        Raises:
            ValueError: If `value` is an empty string or None.
        """
        if not value:
            raise ValueError("First name cannot be blank.")
        self._first_name = value

    @property
    def last_name(self):
        """
        Returns the last name of the client.

        Returns:
            str: The last name.
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Sets the last name of the client.

        Args:
            value (str): The last name of the client.

        Raises:
            ValueError: If `value` is an empty string or None.
        """
        if not value:
            raise ValueError("Last name cannot be blank.")
        self._last_name = value

    @property
    def email_address(self):
        """
        Returns the email address of the client.

        Returns:
            str: The email address.
        """
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        """
        Sets the email address of the client.

        Args:
            value (str): The email address of the client.

        If `value` does not match a valid email pattern, sets it to a default invalid email address.
        """
        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, value):
            self._email_address = "invalidemail@default.com"
        else:
            self._email_address = value

    def __str__(self):
        """
        Returns a string representation of the client.

        Returns:
            str: A formatted string displaying the client's name and number.
        """
        return f"Client: {self.first_name} {self.last_name} ({self.client_number})"



