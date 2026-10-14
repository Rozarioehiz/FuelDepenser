import unittest

from account import Account

class TestAccount(unittest.TestCase):
    def test_that_account_can_be_created(self):
        acc = Account("bob")
        self.assertEqual(acc.balance, 0)
        self.assertEqual(acc.name, "bob")

    def test_that_account_can_receive_deposit(self):
        acc = Account("Alice")
        acc.deposit(2500)
        self.assertEqual(acc.balance, 2500)

    def test_that_account_can_not_receive_negative_amount_for_deposit(self):
        acc = Account("Alice")
        self.assertRaises(ValueError, acc.deposit, -2500)

    def test_that_account_can_withdraw_from_balance(self):
        acc = Account("Alice")
        acc.deposit(2500)
        acc.withdraw(2000)
        self.assertEqual(acc.balance, 500)

    def test_that_account_can_withdraw_exact_amount_deposited_and_succeeds(self):
        acc = Account("Alice")
        acc.deposit(2500)
        acc.withdraw(2500)
        self.assertEqual(acc.balance, 0)

    def test_that_account_can_not_withdraw_negative_amount(self):
        acc = Account("Alice")
        self.assertRaises(ValueError, acc.withdraw, -500)

    def test_account_balance_can_not_be_overdrawn(self):
        acc = Account("Alice")
        acc.deposit(2500)
        self.assertRaises(ValueError, acc.withdraw, 5000)




if __name__ == '__main__':
    unittest.main()
