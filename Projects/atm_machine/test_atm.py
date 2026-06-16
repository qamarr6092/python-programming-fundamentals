import unittest 
from atm import Atm
from account import Account

class TestAtm ( unittest.TestCase ) :

    def setUp ( self ) :

        self.atm = Atm ( cash_available = 1000 , max_withdrawl = 50 ) 

    def test_add_account ( self ) :
        self.atm.add_account ( 'mark', 9999 , 111, 20.5 ) 
        acc_obj = self.atm.accounts[ 9999 ]
        self.assertIn ( 9999 , self.atm.accounts )
        self.assertEqual ( 'Mark' , self.atm.accounts[9999].name )  #Expected Value at left , actual at right


    def test_withdraw_from_atm ( self ) :
        self.atm.add_account ( 'harry' , 7777 , 777 , 100 )
        self.atm.withdraw_from_atm( 7777 , 777 , 40)
        self.assertEqual ( 60 , self.atm.accounts[7777].balance )
        self.assertEqual ( 960 , self.atm.cash_available )
    



unittest.main( )