from atm import Atm


atm = Atm ( 10000 , 200 )

while True :

    print('1.) Create an account.')
    print('2.) Deposit amount to your account. ')
    print('3.) Withdraw from your account. ')
    print('4.) Check ATM limit. ')
    print('5.) Change your account pin.')
    print('6.) Show your account transaction detail.')
    print('7.) Show balance.')
    print('8.) Exit.')
    try :
        choice = int ( input( 'Enter the choice : '))   
    except ValueError :
        print('Enter in numeric values : ')
        continue
    else :
        if choice == 1 :
            try :
                name  = input('Enter the account name : ')
                account_number = int ( input ('Enter the account number : '))
                pin = int( input('Enter the account pin : '))
                amount = int(input('Enter the amount to start your account : '))

            except ValueError :
                print('Enter information in correct format.')
                continue
            
            else :
                atm.add_account( name , account_number , pin , amount )
            
        elif choice == 2 :
            try :
                account_number = int ( input ('Enter the account number : '))
                pin = int( input('Enter the account pin : '))
                amount = int(input('Enter the amount to deposit in your account : '))

            except ValueError :
                print('Enter information in correct format.')
                continue

            else :
                atm.deposit_from_atm ( account_number , pin , amount ) 

        elif choice == 3 :
            try :
                account_number = int ( input ('Enter the account number : '))
                pin = int( input('Enter the account pin : '))
                amount = int(input('Enter the amount to withdraw from your account : '))

            except ValueError :
                print('Enter information in correct format.')
                continue
            else :
                atm.withdraw_from_atm( account_number , pin , amount )

        elif choice == 4 :
            atm.check_atm_limit()

        elif choice ==5  :
            try :
                account_number = int ( input ('Enter the account number : '))
                old_pin = int( input('Enter the account pin : '))
                new_pin = int(input('Enter the new account pin : '))
            except ValueError :
                print('Enter information in correct format.')
                continue
            else :
                atm.change_pin ( account_number , old_pin , new_pin )
        
        elif choice == 6 :
            try :
                account_number = int ( input ('Enter the account number : '))
                pin = int( input('Enter the account pin : '))

            except ValueError :
                print('Enter information in correct format.')
            
            else :
                atm.show_transaction ( account_number , pin )

        elif choice == 7 :
            try :
                account_number = int ( input ('Enter the account number : '))
                pin = int( input('Enter the account pin : '))

            except ValueError :
                print('Enter information in correct format.')
            else :
                atm.show_balance ( account_number , pin )

        elif choice == 8 :
            print('Exited.')
            break

        else :
            print('Invalid Choice.')
            continue



