#Day_6_OOP:
#Chapter_7_OOP:
class Dog  ( ) :
    def __init__  (self , name ,age ) : #Whenever we create an instance , this init method will work
        self.name = name    #This becomes the attribute of an instance , an  attribute is the variable of an object
        self.age = age
    def sit ( self ) :
        print(self.name.title() + " is now sitting.")
    def roll (self) :
        print(self.name.title () + ' is now rolling.')
my_dog = Dog('Willie' , 8)
print('My dog name is :' , my_dog.name.title()) #object_name.attribute to acceess 
print('My dog age :' ,my_dog.age)   #Attribute is the variables of the instance, and the values stored in it i printed
my_dog.sit()
my_dog.roll ( )
my_dog_1 = Dog ('nancy' , 4 )
print('My second dog name is  :' , my_dog_1.name.title())
print('My second dog age is :' ,my_dog_1.age)
'''my_dog_1.name = 'Laurie'
print(my_dog_1.name) '''    #We can modify the attribute of instance as well, instance_name.attribute
my_dog_1.sit ( )
my_dog_1. roll ( )


#Excersizes
class Restaurant ( ) :
    def __init__ ( self ,restaurant_name , cuisine_type ) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def  describe_restaurant (self ) :
        print('Restaurant Name :' ,self.restaurant_name.title() ,'\n' + 'Cuisine Type:' , self.cuisine_type.title())
    def open_restaurant (self) :
        print(self.restaurant_name.title() +': is now open')
my_restaurant_1 = Restaurant ( 'kfc' , 'burger' )
my_restaurant_2 = Restaurant ('dominos' ,'pizza')
my_restaurant_1.describe_restaurant () 
my_restaurant_1.open_restaurant ()
my_restaurant_2.describe_restaurant ()
my_restaurant_2.open_restaurant ()

class User ( ) :
    def __init__ ( self , first_name , last_name , year , university ) :
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.year = year
        self.full_name = first_name.title() +' '+ last_name.title()
    def greet_user ( self ) :
        print('Hello !' ,self.full_name)
    def describe_user ( self ) :
        print('Your details are : ')
        print('First Name :' ,self.first_name.title())
        print('Last Name :' ,self.last_name.title())
        print('Year :' ,self.year.title())
        print('University :' ,self.university.title())
while True :
    prompt = input('Do you wish to continue : ').lower().strip()
    if prompt == 'no' :
        break
    elif prompt != 'yes' :
        continue 
    first_name = input('Enter the First Name : ').title().strip()
    last_name = input('Enter the Last Name : ').title().strip()
    university = input ('Enter the University Name : ').title().strip()
    year = input('Enter the Year you study : ').title().strip()
    user_1 = User( first_name , last_name , year , university )
    user_1.greet_user ( )
    user_1.describe_user ( )