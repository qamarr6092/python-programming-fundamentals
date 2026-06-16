import unittest
from account import Account

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.balance = 500
        self.my_account = Account('qamar', 1023, 7113, self.balance)

    def test_add_amount(self):
        amount = 900
        self.my_account.deposit_amount(1023, 7113, amount)

        expected_balance = self.balance + amount
        actual_balance = self.my_account.balance

        self.assertEqual(expected_balance, actual_balance)
        self.assertIn(amount , self.my_account.deposit_info)
    
    def test_change_pin ( self ) :
        old_pin = self.my_account.pin
        self.my_account.change_pin ( 1023 ,old_pin , 7114 ) 
        self.assertEqual ( 7114 , self.my_account.pin )
    
    def test_withdraw_amount ( self ) :
        amount = 200
        self.my_account.withdraw_amount ( 1023 , 7113 , amount ) 
        self.assertEqual  ( 300 , self.my_account.balance)
        self.assertIn ( amount  , self.my_account.withdraw_info)



unittest.main()
