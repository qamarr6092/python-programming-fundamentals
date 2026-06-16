from account import Account 
import json


#It is not recomended to print something inside the fucntion
#but for beginers it is okay

class Atm ( ) :

    def __init__ ( self , cash_available , max_withdrawl ) :
        self.accounts = { }
        self.cash_available = float(cash_available)
        self.max_withdrawl = float(max_withdrawl)

    def add_account ( self , name , account_number , pin , balance ) :
        if account_number not in  self.accounts.keys() :
            new_account = Account ( name , account_number , pin , balance )
            self.accounts[ account_number ] = new_account
            print('Account created successfully.')
            return ( self.accounts , new_account )
        else :
            print ('Account is already present.')

    def withdraw_from_atm ( self , account_number , pin ,amount ) :
        if account_number in self.accounts.keys() :
            account = self.accounts[account_number]
            if pin == account.pin :
                if self.cash_available >= amount :
                    if self.max_withdrawl >= amount :
                        if  account.balance >= amount and amount > 0:
                            self.cash_available -= amount
                            account.balance -= amount
                            account.withdraw_info.append(amount)
                            print('Amount Withdrew : ' + str(amount))
                            return (self.cash_available , account ,self.accounts , account.withdraw_info )
                        elif account.balance < amount or amount <= 0 :
                            print('Insufficient funds.')
                            return None
                    elif self.max_withdrawl < amount :
                        print('ATM has a limit of max withdrawl : ' + str(self.max_withdrawl))
                        return None
                elif self.cash_available < amount :
                    print('ATM has cash of ' + str(self.cash_available) + ' available right now. ')
                    return None
                
            else :
                print('Invalid Pin.')
                return None
        else :
            print('Account not present.')
            return None

    def check_atm_limit ( self ) :
        print('Atm max withdrawl : ' +  str(self.max_withdrawl ))
        print ('Atm available cash : ' + str(self.cash_available ))
        return None


    def deposit_from_atm ( self  , account_number , pin , amount ) :
        if account_number in self.accounts.keys () :
            account_object = self.accounts[account_number]
            if account_object.pin == pin :
                if amount > 0 :
                    account_object.balance += float(amount)
                    account_object.deposit_info.append(amount)
                    print('Amount Deposited : ' + str(amount))

                    return (self.accounts , account_object.balance , account_object.deposit_info )
                else :
                    print('Enter sufficient amount.')
                    return None
            else :
                print('Invalid Pin.')
                return None
        else :
            print('Account not present.')
            return None

    def show_transaction(self, account_number, pin):
        if account_number in self.accounts.keys () :
            
            if pin ==  self.accounts[account_number].pin :
                print('Transaction History.')
                print('Account Name : ' + self.accounts[account_number].name )
                i = 1
                for deposit in  self.accounts[account_number].deposit_info :
                    print(str(i) + '.) Deposited  : ' + str(deposit) )
                    i += 1
                for withdraw in self.accounts[account_number].withdraw_info :
                    print(str(i) + '.) Withdrew : ' + str(withdraw))
                    i+=1
            else :
                print('Invalid Pin.')
        else :
            print('Account not present.')
        return None
    
    def change_pin ( self , account_number , old_pin , new_pin ) :
        if account_number in self.accounts.keys () :
            if old_pin ==  self.accounts[account_number].pin :
                self.accounts[account_number].pin =  int(new_pin)
                print('Account Pin changed.')
                return self.accounts[account_number].pin
            else :
                print('Invalid Pin.')
                return None
        else :
            print('Account not present.')
            return None
        
    def show_balance ( self , account_number , pin ) :
        if account_number in self.accounts.keys () :
            if pin ==  self.accounts[account_number].pin :
                print( 'Account Balance : ' + str(self.accounts[account_number].balance) )
                return None
            else :
                print('Invalid Pin.')
                return None
        else :
            print('Account not present.')
            return None
        






