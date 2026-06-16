#Importing a module into a module to keep main file clean
from car import Car


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