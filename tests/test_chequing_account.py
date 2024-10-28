import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.account = ChequingAccount(12345, 67890, 1000.00, date.today(), -100.00, 0.05)

    def test_initialization_valid(self):
        self.assertEqual(self.account.overdraft_limit, -100.00)
        self.assertEqual(self.account.overdraft_rate, 0.05)

    def test_initialization_invalid_overdraft_limit(self):
        account = ChequingAccount(12345, 67890, 1000.00, date.today(), "invalid", 0.05)
        self.assertEqual(account.overdraft_limit, -100.00)  # Default value

    def test_initialization_invalid_overdraft_rate(self):
        account = ChequingAccount(12345, 67890, 1000.00, date.today(), -100.00, "invalid")
        self.assertEqual(account.overdraft_rate, 0.05)  # Default value

    def test_get_service_charges_above_limit(self):
        self.account.update_balance(-50.00)  # Use method to update balance
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_get_service_charges_at_limit(self):
        self.account.update_balance(-100.00)  # Use method to update balance
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_get_service_charges_below_limit(self):
        self.account.update_balance(-200.00)  # Adjust balance using the method
        expected_charge = 0.50 # Correct expected charge calculation
        self.assertEqual(round(self.account.get_service_charges(), 2), round(expected_charge, 2))


    def test_str_method(self):
        expected_str = ("Account Number: 12345 Balance: $1,000.00\n"
                        "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account Type: Chequing")
        self.assertEqual(str(self.account), expected_str)

    def test_edge_case_balance_and_overdraft(self):
        self.account.update_balance(-99.99)  # Use method to update balance
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)
        self.account.update_balance(-100.01)  # Use method to update balance
        expected_charge = 0.50 + (-100 - (-100.01)) * 0.05  # Calculate expected charge
        self.assertEqual(round(self.account.get_service_charges(), 2), round(expected_charge, 2))

if __name__ == '__main__':
    unittest.main()