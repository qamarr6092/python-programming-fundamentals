#Day_8_OOP :
#Chapter_7_OOP:
#Excersize
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant Name:", self.restaurant_name.title())
        print("Cuisine Type:", self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title(), "is now open")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavor):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [flavor]

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print("-", flavor)

icecream = IceCreamStand("Omore", "Cornetto", "Vanilla")
icecream.add_flavor("Chocolate")
icecream.display_flavors()


class User ( ) :

    def __init__ ( self, first_name , last_name ) :
        self.first_name = first_name.title().strip()
        self.last_name =  last_name.title( ).strip( )
        self.login_attempts = 0

    def increment_login_attempts ( self ) :
        self.login_attempts += 1
    
    def reset_login_attempts ( self ) :
        self.login_attempts = 0

    def describe_user ( self ) :
        print('User Information' )
        print('First Name :' ,self.first_name)
        print('Last Name :' , self.last_name )
        print('Login attempts =' ,self.login_attempts )

class Privileges ( ) :

    def __init__ ( self ,privileges='can add user'):
        self.privileges = [ ]
        self.privileges.append ( privileges )

    def show_privilege ( self ) :
        print('User Admin has following privileges:')
        for privilege in self.privileges :
            print('-' ,privilege.title())


class Admin ( User ) :

    def __init__ ( self , first_name , last_name  ) :
        super().__init__ ( first_name , last_name )
        self.privileges = Privileges ( )

    def store_privilege ( self , privilege) :
        self.privileges.privileges.append(privilege)

admin = Admin ( 'qamar' , 'jawaid' )
admin.describe_user ( )
admin.store_privilege('can delete posts')
admin.store_privilege ('can join the community')
admin.privileges.show_privilege()



#Importing Class :
from car import Car, Electric_Car , Battery
my_car = Car('hondA' ,'civic', year =2022)
print(my_car.get_descriptive_name( ))
my_tesla = Electric_Car ('tesla' ,'model xyz' ,year =2022)
print(my_tesla.get_descriptive_name())
my_tesla.update_battery( 47 )
my_tesla.battery.describe_battery()

#Importing module into module
from electric_car1 import Electric_Car
from car1 import Car
my_tesla = Electric_Car ('Tesla' , 'Automatic' , 2025)
print(my_tesla.get_descriptive_name())
my_new_car = Car ('honda' ,'brv' ,2014)
print(my_new_car.get_descriptive_name()) 



#Excersize
from admin import Admin , User
admin = Admin ('qamar' , 'jawaid' )
admin.privileges.show_privilege()
user = User ('qamar' , 'jawaid')
user.describe_user()


from collections import OrderedDict as Od #The OrderDict () is a class from collection that keeps order of dict
students = Od()
students['first name'] = 'qamar'
students['last name' ] = 'jawaid'
students['city'] = 'karachi'
student_2 = [ ]
student_2.append('huzaifa')
student_2.append('becon house')
students['student 2'] = student_2
for key , value in students.items ()  :
    if key != 'student 2' :
        print(key.title() ,':' ,value.title())  
    elif key == 'student 2':
        print(key)
        for info in student_2 :
            print(info)
print(students)


from random import randint as r 
class Dice  ( ) :
    def __init__ ( self , sides = 6 ) :
        self.sides = sides
    def roll_dice ( self ) :
        print(self.sides, 'sides Dice :')
        for  i in range(self.sides) :
            print('This dice has now :' , r(1, self.sides))

six_dice =  Dice ( 6 )
six_dice.roll_dice ( )
ten_dice = Dice ( 10 )
ten_dice.roll_dice ( )

import random
tries= 0
guess_number = random.randint(1,100)
while True :
    number = int(input('Enter the number to guess my number : '))
    if number == guess_number :
        print('You guessed my number' ,guess_number, 'in' ,tries , 'attempts')
        break
    elif guess_number > number :
        print('My guess number is higher')
    else :
        print('My guess number is lower')
    tries += 1