#Day_10_Files_And_Exceptions :
#Chapter_8 :
#Refactoring 
import json
def get_stored_name () :
    file_name = 'pak.json'
    try :
        with open ( file_name , 'r' ) as file :
            name = json.load(file)
    except FileNotFoundError :
        return None
    else :
        return name 

def get_new_name () :
    name = input('What is your name ' )
    file_name = 'pak.json'
    with open ( file_name , 'w' ) as file :
        json.dump ( name , file ) 
    return name


def greet_user () :
    name = get_stored_name ( )
    if name :
        print('Welcome Back' , name.title())
    else :
        name = get_new_name ()
        print('We will remember you ' , name.title ())

greet_user()
#get_new_name ()
greet_user()


#Excersiez :
import json

def store_favorite_number():
    file_name = 'favorite_number.json'
    number = input("What is your favorite number? ")
    with open(file_name, 'w') as file:
        json.dump(number, file)
        print("I'll remember that!")
def show_favorite_number():
    file_name = 'favorite_number.json'
    try:
        with open(file_name) as file:
            number = json.load(file)
    except FileNotFoundError:
        store_favorite_number()
    else :
        print(f"I know your favorite number! It’s {number}.")

show_favorite_number()

import json
def store_name():
    file_name = 'tst.json'
    name = input('Enter your name: ')
    with open(file_name, 'w') as file:
        json.dump(name, file)
    return name
def get_name():
    file_name = 'tst.json'
    try:
        with open(file_name) as file:
            name = json.load(file)
    except (FileNotFoundError) :
        name = store_name()
    else :
        message = input('If you are trying to log in ? Enter your correct name : ').lower().strip()
        if message == name :
            print('Granted Access : ')
            print('Your Name:', name.title())
        else :
            print('You are trying to steal user info ')
            print('You can make your account : ')
            message_1 = input('Do you want to continue : ').lower().strip()
            if message_1 ==  'yes' :
                name = store_name ()
                print( 'Account Created :')
            elif message_1  == 'no' or message_1 != 'yes' :
                pass
get_name()
