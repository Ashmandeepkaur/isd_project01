"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Modified by: Ashmandeep Kaur
Date: 15-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client import Client

class TestClient(unittest.TestCase):
    """
    Unit tests for the Client class.

    Methods:
        test_init_valid_values():
            Tests that a Client instance is correctly initialized with valid values.
        test_init_invalid_client_number():
            Tests that initializing a Client with a non-integer client number raises a ValueError.
        test_init_blank_first_name():
            Tests that initializing a Client with a blank first name raises a ValueError.
        test_init_blank_last_name():
            Tests that initializing a Client with a blank last name raises a ValueError.
        test_init_invalid_email_address():
            Tests that an invalid email address is replaced with a default invalid email address.
        test_client_number_getter():
            Tests that the client number getter returns the correct value.
        test_first_name_getter():
            Tests that the first name getter returns the correct value.
        test_last_name_getter():
            Tests that the last name getter returns the correct value.
        test_email_address_getter():
            Tests that the email address getter returns the correct value.
        test_str_method():
            Tests that the string representation of the Client instance is formatted correctly.
    """

    def test_init_valid_values(self):
        """
        Test that a Client instance is correctly initialized with valid values.

        Verifies that the client number, first name, last name, and email address are set correctly.
        """
        client = Client(12345, "Ashmandeep", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(client.client_number, 12345)
        self.assertEqual(client.first_name, "Ashmandeep")
        self.assertEqual(client.last_name, "Kaur")
        self.assertEqual(client.email_address, "ashmandeepkaur@gmail.com")

    def test_init_invalid_client_number(self):
        """
        Test that initializing a Client with a non-integer client number raises a ValueError.

        Verifies that a ValueError is raised when the client number is not an integer.
        """
        with self.assertRaises(ValueError) as e:
            client = Client("abc", "Ashmandeep", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(str(e.exception), "Client number must be an integer.")

    def test_init_blank_first_name(self):
        """
        Test that initializing a Client with a blank first name raises a ValueError.

        Verifies that a ValueError is raised when the first name is an empty string.
        """
        with self.assertRaises(ValueError) as e:
            client = Client(12345, "", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(str(e.exception), "First name cannot be blank.")

    def test_init_blank_last_name(self):
        """
        Test that initializing a Client with a blank last name raises a ValueError.

        Verifies that a ValueError is raised when the last name is an empty string.
        """
        with self.assertRaises(ValueError) as e:
            client = Client(12345, "Ashmandeep", "", "ashmandeepkaur@gmail.com")
        self.assertEqual(str(e.exception), "Last name cannot be blank.")

    def test_init_invalid_email_address(self):
        """
        Test that an invalid email address is replaced with a default invalid email address.

        Verifies that the email address is set to "invalidemail@default.com" if it does not match the valid email pattern.
        """
        client = Client(12345, "Ashmandeep", "Kaur", "invalidemail")
        self.assertEqual(client.email_address, "invalidemail@default.com")

    def test_client_number_getter(self):
        """
        Test that the client number getter returns the correct value.

        Verifies that the getter method for client number returns the value set during initialization.
        """
        client = Client(12345, "Ashmandeep", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(client.client_number, 12345)

    def test_first_name_getter(self):
        """
        Test that the first name getter returns the correct value.

        Verifies that the getter method for first name returns the value set during initialization.
        """
        client = Client(12345, "Ashmandeep", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(client.first_name, "Ashmandeep")

    def test_last_name_getter(self):
        """
        Test that the last name getter returns the correct value.

        Verifies that the getter method for last name returns the value set during initialization.
        """
        client = Client(12345, "Ashmandeep", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(client.last_name, "Kaur")

    def test_email_address_getter(self):
        """
        Test that the email address getter returns the correct value.

        Verifies that the getter method for email address returns the value set during initialization.
        """
        client = Client(12345, "Ashmandeep", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(client.email_address, "ashmandeepkaur@gmail.com")

    def test_str_method(self):
        """
        Test that the string representation of the Client instance is formatted correctly.

        Verifies that the `__str__` method returns a string in the format: "Client: {first_name} {last_name} ({client_number})".
        """
        client = Client(12345, "Ashmandeep", "Kaur", "ashmandeepkaur@gmail.com")
        self.assertEqual(str(client), "Client: Ashmandeep Kaur (12345)")

if __name__ == '__main__':
    unittest.main()
