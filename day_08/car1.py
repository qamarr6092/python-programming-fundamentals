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
