class Account():

    def __init__(self, name, account_number, pin, balance):

        self.deposit_info = []
        self.withdraw_info = []
        self.name = str(name.title().strip())
        self.account_number = int(account_number)
        self.pin = int(pin)
        self.balance = float(balance)

    def deposit_amount(self, account_number, pin, amount):

        if account_number == self.account_number and pin == self.pin:
            if amount > 0:
                self.balance += float(amount)
                self.deposit_info.append(amount)
                return (self.balance, self.deposit_info)
            else:
                print('Cannot deposit, enter correct amount.')
        else:
            print('Invalid information.')

    def withdraw_amount(self, account_number, pin, amount):

        if account_number == self.account_number and pin == self.pin:
            if amount > 0 and amount <= self.balance:
                self.balance = self.balance - float(amount)
                self.withdraw_info.append(amount)
                return (self.balance, self.withdraw_info)
            else:
                print('Cannot withdraw! Insufficient funds or invalid amount.')
        else:
            print('Invalid information.')

    def check_balance(self, account_number, pin):

        if account_number == self.account_number and pin == self.pin:
            print('Account Name : ' + self.name)
            print('Account Number : ' + str(self.account_number))
            print('Account Balance : ' + str(self.balance))
        else:
            print('Invalid information provided.')
        return None

    def change_pin(self, account_number, old_pin, new_pin):

        if account_number == self.account_number:
            if old_pin == self.pin:
                self.pin = int(new_pin)
                return self.pin
            else:
                print('Invalid pin.')
        else:
            print('Invalid account number.')

    def show_transaction(self, account_number, pin):

        if account_number == self.account_number and pin == self.pin:
            i = 1
            print('Transaction History.')

            for deposit in self.deposit_info:
                print(str(i) + '.) Deposited by ' + self.name + ' : ' + str(deposit))
                i += 1

            for withdraw in self.withdraw_info:
                print(str(i) + '.) Withdrew by ' + self.name + ' : ' + str(withdraw))
                i += 1
        else:
            print('Invalid information.')