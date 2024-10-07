import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        """Create an InvestmentAccount instance for testing."""
        self.account_within_10_years = InvestmentAccount(2341234, 67890, 19329.21, date(2024, 1, 1), 1.99)
        self.account_over_10_years = InvestmentAccount(9876543, 12345, 11329.65, date(2010, 1, 1), 3.00)

    def test_service_charges_within_ten_years(self):
        """Test service charges for an account created within the last 10 years."""
        expected_service_charge = InvestmentAccount.BASE_SERVICE_CHARGE + 1.99
        actual_service_charge = self.account_within_10_years.get_service_charges()
        self.assertEqual(expected_service_charge, round(actual_service_charge, 2))

    def test_service_charges_over_ten_years(self):
        """Test service charges for an account created more than 10 years ago."""
        expected_service_charge = InvestmentAccount.BASE_SERVICE_CHARGE
        actual_service_charge = self.account_over_10_years.get_service_charges()
        self.assertEqual(expected_service_charge, round(actual_service_charge, 2))

    def test_str_method_within_ten_years(self):
        """Test the string representation of the InvestmentAccount for an account within 10 years."""
        expected_str = (
            "Account Number: 2341234 Balance: $19329.21\n"
            "Date Created: 2024-01-01 Management Fee: $1.99 Account Type: Investment"
        )
        actual_str = str(self.account_within_10_years)
        self.assertEqual(expected_str, actual_str)

    def test_str_method_over_ten_years(self):
        """Test the string representation of the InvestmentAccount for an account over 10 years."""
        expected_str = (
            "Account Number: 9876543 Balance: $11329.65\n"
            "Date Created: 2010-01-01 Management Fee: Waived Account Type: Investment"
        )
        actual_str = str(self.account_over_10_years)
        self.assertEqual(expected_str, actual_str)

    def test_management_fee_default(self):
        """Test that the management fee defaults to 2.55 when invalid input is provided."""
        account = InvestmentAccount(1122334, 44556, 15000, date(2023, 1, 1), "invalid")
        expected_fee = 2.55
        actual_fee = account._InvestmentAccount__management_fee  # Accessing the private attribute
        self.assertEqual(expected_fee, actual_fee)

    def test_service_charge_with_high_management_fee(self):
        """Test service charge with a higher management fee within 10 years."""
        account = InvestmentAccount(5566778, 99887, 25000, date(2023, 1, 1), 5.00)
        expected_service_charge = InvestmentAccount.BASE_SERVICE_CHARGE + 5.00
        actual_service_charge = account.get_service_charges()
        self.assertEqual(expected_service_charge, round(actual_service_charge, 2))

    def test_service_charge_with_no_management_fee(self):
        """Test service charge when the management fee is waived."""
        account = InvestmentAccount(4455667, 33445, 5000, date(2000, 1, 1), 0)
        expected_service_charge = InvestmentAccount.BASE_SERVICE_CHARGE
        actual_service_charge = account.get_service_charges()
        self.assertEqual(expected_service_charge, round(actual_service_charge, 2))

# Execute the tests
if __name__ == "__main__":
    unittest.main()
