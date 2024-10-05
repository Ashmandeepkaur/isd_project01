"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Modified by: Ashmandeep Kaur
Date: 15-09-2024
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""

import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Unit tests for the BankAccount class."""

    def test_init_valid_values(self):
        """Test that a BankAccount is correctly initialized with valid values."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        self.assertEqual(bank_account.account_number, 12345)
        self.assertEqual(bank_account.client_number, 67890)
        self.assertEqual(round(bank_account.balance, 2), 1000.00)

    def test_init_invalid_balance(self):
        """Test that the balance defaults to 0.00 if an invalid balance is provided."""
        bank_account = BankAccount(12345, 67890, 'invalid_balance')
        self.assertEqual(round(bank_account.balance, 2), 0.00)

    def test_init_invalid_account_number(self):
        """Test that a ValueError is raised if the account number is not an integer."""
        with self.assertRaises(ValueError) as e:
            BankAccount('abc', 67890, 1000.00)
        self.assertEqual(str(e.exception), "Account number must be an integer.")

    def test_init_invalid_client_number(self):
        """Test that a ValueError is raised if the client number is not an integer."""
        with self.assertRaises(ValueError) as e:
            BankAccount(12345, 'xyz', 1000.00)
        self.assertEqual(str(e.exception), "Client number must be an integer.")

    def test_account_number_getter(self):
        """Test that the account number getter returns the correct value."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        self.assertEqual(bank_account.account_number, 12345)

    def test_client_number_getter(self):
        """Test that the client number getter returns the correct value."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        self.assertEqual(bank_account.client_number, 67890)

    def test_balance_getter(self):
        """Test that the balance getter returns the correct value rounded to two decimal places."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        self.assertEqual(round(bank_account.balance, 2), 1000.00)

    def test_update_balance_positive(self):
        """Test that updating the balance with a positive amount correctly updates the balance."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        bank_account.update_balance(500.00)
        self.assertEqual(round(bank_account.balance, 2), 1500.00)

    def test_update_balance_negative(self):
        """Test that updating the balance with a negative amount correctly updates the balance."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        bank_account.update_balance(-200.00)
        self.assertEqual(round(bank_account.balance, 2), 800.00)

    def test_update_balance_invalid(self):
        """Test that updating the balance with an invalid amount does not change the balance."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        bank_account.update_balance('invalid')
        self.assertEqual(round(bank_account.balance, 2), 1000.00)

    def test_deposit_valid(self):
        """Test that a valid deposit updates the balance correctly."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        bank_account.deposit(300.00)
        self.assertEqual(round(bank_account.balance, 2), 1300.00)

    def test_deposit_invalid_negative(self):
        """Test that depositing a negative amount raises a ValueError."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        with self.assertRaises(ValueError) as e:
            bank_account.deposit(-100.00)
        self.assertEqual(str(e.exception), "Deposit amount: $-100.00 must be positive.")

    def test_withdraw_valid(self):
        """Test that a valid withdrawal updates the balance correctly."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        bank_account.withdraw(200.00)
        self.assertEqual(round(bank_account.balance, 2), 800.00)

    def test_withdraw_invalid_negative(self):
        """Test that withdrawing a negative amount raises a ValueError."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        with self.assertRaises(ValueError) as e:
            bank_account.withdraw(-50.00)
        self.assertEqual(str(e.exception), "Withdrawal amount: $-50.00 must be positive.")

    def test_withdraw_exceeds_balance(self):
        """Test that withdrawing an amount that exceeds the balance raises a ValueError."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        with self.assertRaises(ValueError) as e:
            bank_account.withdraw(5000.00)
        self.assertEqual(str(e.exception), "Withdrawal amount: $5,000.00 must not exceed the account balance: $1,000.00.")

    def test_str_method(self):
        """Test that the string representation of the BankAccount is formatted correctly."""
        bank_account = BankAccount(12345, 67890, 1000.00)
        self.assertEqual(str(bank_account), "Account Number: 12345 Balance: $1,000.00\n")

if __name__ == '__main__':
    unittest.main()




