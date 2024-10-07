import unittest
from bank_account.savings_account import SavingsAccount
from datetime import date

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        self.account = SavingsAccount(12345, 67890, 1000.00, date.today(), 50.00)

    def test_initialization_valid_minimum_balance(self):
        self.assertEqual(self.account.minimum_balance, 50.00)

    def test_initialization_invalid_minimum_balance(self):
        account = SavingsAccount(12345, 67890, 1000.00, date.today(), "invalid")
        self.assertEqual(account.minimum_balance, 50.00)

    def test_str_method(self):
        expected_str = (
            "Account Number: 12345 Balance: $1,000.00\n"
            "Minimum Balance: $50.00 Account Type: Savings"
        )
        self.assertEqual(str(self.account), expected_str)

    def test_get_service_charges_above_minimum(self):
        self.account.update_balance(100.00)  # Increase balance to test
        expected_charge = SavingsAccount.BASE_SERVICE_CHARGE
        actual_charge = self.account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_below_minimum(self):
        self.account.update_balance(-950.01)  # Reduce balance to below minimum
        expected_charge = SavingsAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM
        actual_charge = self.account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

    def test_get_service_charges_exact_minimum(self):
        self.account.update_balance(-950.00)  # Set balance to exactly minimum
        expected_charge = SavingsAccount.BASE_SERVICE_CHARGE
        actual_charge = self.account.get_service_charges()
        self.assertEqual(expected_charge, round(actual_charge, 2))

if __name__ == "__main__":
    unittest.main()
