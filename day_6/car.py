def make_car ( manufacturer , model_name , **info) :
    car_info = { }
    car_info ['Manufacturer'] =  manufacturer .title().strip()
    car_info ['Model Name'] = model_name.title().strip()
    for key , value in info.items () :
        car_info [ key.title().strip()] = value.title().strip()
    return car_info
'''car = make_car ( 'toyota' , 'mx-2220' , color = 'blue' , seats = '5 seater' )
for key, value in car .items () :
    print(key + ' : '  + value)'''

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
