#Day_7_OOP :
#Chapter_7_OOP:
class Car ( ) :

    def __init__ ( self , company ,model ,year ) :
        self.company = company.title().strip()
        self.model = model.title().strip()
        self.year = year
        self.oddmeter_reading = 0   #This creates the attribute and the default value of zero it does not require argument

    def get_descriptive_name ( self ) :
        long_name =  self.company +' ' + self.model + ' '+str(self.year)
        return long_name
    
    def read_oddmeter ( self ) :
        print('This car has' , self.oddmeter_reading ,'miles in it.')

    def update_oddmeter ( self , new_value ) :  #Modifying the attribute through the method
        if self.oddmeter_reading <= new_value :
            self.oddmeter_reading = new_value
        else :
            print('Enter the valid oddmeter reading ')

    def increment_oddmeter ( self , miles ) :   #Modifying the attrbute value thorugh increment using the method
        self.oddmeter_reading += miles

my_car =  Car ( 'toyota' , 'corolla' , 2026)
print(my_car.get_descriptive_name())
my_car.read_oddmeter ( )
my_car.oddmeter_reading = 30    #Directly modifiying the attribute Value
my_car.read_oddmeter ( )        #Now has thirty miles oddmeter in it
my_car.update_oddmeter ( 40 )   #Modifying through the method
my_car.read_oddmeter ( ) 
my_car.update_oddmeter ( 34 )   #Does not modify because of logic in update_oddmeter method

my_used_car = Car ('Honda' , 'civic' , 2020 )
print(my_used_car.get_descriptive_name())
my_used_car.update_oddmeter ( 4000 ) 
my_used_car.read_oddmeter ( ) 
my_used_car.increment_oddmeter ( 200 ) 
my_used_car.read_oddmeter ( )
my_used_car.increment_oddmeter ( 600 ) 
my_used_car.read_oddmeter ( )



#Excersizes
class User ( ) :

    def __init__ ( self, first_name , last_name ) :
        self.first_name = first_name.title().strip()
        self.last_name =  last_name.title( ).strip( )
        self.login_attempts = 0

    def increment_login_attempts ( self ) :
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts ( self ) :
        self.login_attempts = 0
        return self.login_attempts

    def describe_user ( self ) :
        print('User Information' )
        print('First Name :' ,self.first_name)
        print('Last Name :' , self.last_name )
        print('Login attempts =' ,self.login_attempts )

user_1 = User ('qamar' , 'jawaid' )
user_1.describe_user ( )
user_1.increment_login_attempts ( )
user_1.increment_login_attempts ( )
user_1.increment_login_attempts ( )
user_1.describe_user ( )
user_1.reset_login_attempts ( )
user_1.describe_user ( )



#Inheritance
class Car ( ) :

    def __init__ ( self , company ,model ,year ) :
        self.company = company.title().strip()
        self.model = model.title().strip()
        self.year = year
        self.oddmeter_reading = 0   

    def get_descriptive_name ( self ) :
        long_name =  self.company +' ' + self.model + ' '+str(self.year)
        return long_name
    
    def read_oddmeter ( self ) :
        print('This' ,self.company ,  'has' , self.oddmeter_reading ,'miles in it.')

    def update_oddmeter ( self , new_value ) :  
        if self.oddmeter_reading <= new_value :
            self.oddmeter_reading = new_value
        else :
            print('Enter the valid oddmeter reading ')

    def increment_oddmeter ( self , miles ) : 
        self.oddmeter_reading += miles

class Electric_Car ( Car ) :    #class Child_Class ( Parent_Class ), Child_class inherits every method and attribute from the parent class.
    def __init__ ( self , company , model , year ) :    #The child class's instance will have these attributes , This is constructor of child's class
        super( ).__init__(company, model, year )        #And these attributes are taken from the parent class, the super() method will take to the parent class attributes
        self.battery_size = 70 
    #The above super() calls the parent class constructor what ever attributes the parent constructor has will be equipped to child, can be described as : 'Car.__init__(company, model ,year )

    def describe_battery ( self ) :
        print('This car has' , self.battery_size ,'%', 'battery.') 

my_tesla = Electric_Car ( 'tesla' , 'elon musk model' , 2020 )
print(my_tesla.get_descriptive_name ( )) 
my_tesla.read_oddmeter ( )
my_tesla.describe_battery ( )


#Overriding Methods from the parent class :
class Car ( ) :
    def __init__ (self , company , model ):
        self.company = company
        self.model = model
    def fill_gas ( self ) :
        print('Car is getting fuel : ')
class Electric_Car ( Car ) :
    def __init__ ( self , company , model , battery ='50kwh' ) :
        super ( ).__init__(company , model )
        self.battery = battery 
    def fill_gas (self ) :
        print('You know electric cars does not need fuels : ')
    def get_battery ( self ) :
        print(self.battery)

my_car = Car ( 'Toyota' ,'Cororla' )
my_car.fill_gas ( )
my_tesla = Electric_Car ( 'Tesla' , 'Elon Musk Model' )
my_tesla.fill_gas ( )   #Here I am overiding the method for the child class, the python sees the child class methods first if it founds then it ignores the parent's method
my_tesla.get_battery ( )    #Similarly the get_fuel ( ) will get ignored from the parent_Class (Car)


#Instances as attributes
#We details , attributes , methods grow we create more classes.
class Car ( ) :

    def __init__ ( self , company ,model ,year ) :
        self.company = company.title().strip()
        self.model = model.title().strip()
        self.year = year
        self.oddmeter_reading = 0   

    def get_descriptive_name ( self ) :
        long_name =  self.company +' ' + self.model + ' '+str(self.year)
        return long_name
    
    def read_oddmeter ( self ) :
        print('This' ,self.company ,  'has' , self.oddmeter_reading ,'miles in it.')

    def update_oddmeter ( self , new_value ) :  
        if self.oddmeter_reading <= new_value :
            self.oddmeter_reading = new_value
        else :
            print('Enter the valid oddmeter reading ')

    def increment_oddmeter ( self , miles ) : 
        self.oddmeter_reading += miles

class Battery ( ) :
    def __init__ ( self , battery_size = 70 ) :   #The default parameters can work without the arguments , if given they change value
        self.battery_size = battery_size
    def describe_battery ( self ) :
        print('The battery has ' +  str(self.battery_size) + ' KwH battery size.')
    def get_range ( self  ) :
        if self.battery_size >= 70 :
            range_ = 240
        elif self.battery_size <= 50 :
            range_ = 200
        print('This car can go' ,range_,'miles per hour when fully charged based on' ,self.battery_size )
  
class Electric_Car ( Car ) :
    def __init__ ( self , company , model ,year ) :
        super().__init__(company , model , year )
        self.battery = Battery ( )  #This creates an instance from class Battery () and stores into the attribute self.battery it has default value of '70'
                                    #Whenever electric car instance is created the new instance of battery will also be created that will be stored in 'battery' attribute of the new instance of electric car.
    def update_battery ( self , new_battery_size ) :
        self.battery = Battery ( new_battery_size )

my_tesla = Electric_Car ( 'Tesla' , 'Model X' , 2024 ) 
print(my_tesla.get_descriptive_name ( ))
my_tesla.battery.describe_battery( )
my_tesla.battery.get_range ( )
my_tesla.battery = Battery ( 49 )
my_tesla.battery.describe_battery( )
my_tesla.battery.get_range ( )
my_tesla.update_battery ( 37 )
my_tesla.battery.describe_battery( )
my_tesla.battery.get_range ( )

#Ending today's coding at page number 177.