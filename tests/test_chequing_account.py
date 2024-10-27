import unittest
from bank_account.chequing_account import ChequingAccount
from datetime import date

class TestChequingAccount(unittest.TestCase):

    def setUp(self) -> None:
        self.account = ChequingAccount(12345, 67890, 1000.00, date.today(), -100.00, 0.05)

    def test_initialization_valid(self) -> None:
        self.assertEqual(self.account.overdraft_limit, -100.00)
        self.assertEqual(self.account.overdraft_rate, 0.05)

    def test_initialization_invalid_overdraft_limit(self) -> None:
        account = ChequingAccount(12345, 67890, 1000.00, date.today(), "invalid", 0.05)
        self.assertEqual(account.overdraft_limit, -100.00)

    def test_initialization_invalid_overdraft_rate(self) -> None:
        account = ChequingAccount(12345, 67890, 1000.00, date.today(), -100.00, "invalid")
        self.assertEqual(account.overdraft_rate, 0.05)

    def test_get_service_charges_above_limit(self) -> None:
        self.account.update_balance(-50.00)
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_get_service_charges_at_limit(self) -> None:
        self.account.update_balance(-100.00)
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

    def test_get_service_charges_below_limit(self) -> None:
        self.account.update_balance(-200.00)
        expected_charge = 0.50 + (100.00 * self.account.overdraft_rate)
        self.assertEqual(round(self.account.get_service_charges(), 2), round(expected_charge, 2))

    def test_str_method(self) -> None:
        expected_str = (
            "Account Number: 12345 Balance: $1,000.00\n"
            "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% Account Type: Chequing"
        )
        self.assertEqual(str(self.account), expected_str)

    def test_edge_case_balance_and_overdraft(self) -> None:
        self.account.update_balance(-99.99)
        self.assertEqual(round(self.account.get_service_charges(), 2), 0.50)

        self.account.update_balance(-100.01)
        expected_charge = 0.50 + abs(-100 - (-100.01)) * self.account.overdraft_rate
        self.assertEqual(round(self.account.get_service_charges(), 2), round(expected_charge, 2))

if __name__ == '__main__':
    unittest.main()
