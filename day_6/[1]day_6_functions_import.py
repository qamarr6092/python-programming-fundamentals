import car 
# Each function by this method can be accessed by module_name.function_name()
my_car = car.make_car( 'toyota' ,'corolla' , year = '2022' , color = ' black' )
print(my_car)

#Importing specific functions
# from module_name import function_name ,  ..... function_name_n
from car import make_car 
his_car = make_car ( 'honda' , 'civic' , year = '2022' )    #here we didnt use the module_name.fn_name , we directly used the fn_name
print(his_car) 

#Give function as alias
#Syntax : from module_name import function_name as fn
from car import make_car as car 
my_car = car('toyota' , 'corolla' , year = '2022' )
print(my_car)

#Module as alias
#Syntax : import module_name as mn
import day_6_functions as func
my_profile = func.create_profile( )
print(my_profile)

import car as c
my_car =  c.make_car ( 'honda' , 'civic')   #so mn.function_name will be used
print(my_car)

#importing all functions in a module
#Syntax : from module_name import *
from car import *
#Because all functions are called you can use with .dot notations
my_car = make_car  ( 'honda' , 'cultus' , color = 'grey' )
print(my_car)


#Excersizes
import profile 
my_profile = profile.create_profile() 
for key , value in my_profile.items() :
    print(key + ' : '  + value)

from profile import create_profile 
my_profile = create_profile() 
for key , value in my_profile.items() :
    print(key + ' : '  + value)

from profile import create_profile as profiles
my_profile = profiles() 
for key , value in my_profile.items() :
    print(key + ' : '  + value)

import profile as p
my_profile = p.create_profile () 
for key , value in my_profile.items() :
    print(key + ' : '  + value)

from profile import *
my_profile = create_profile ( )
for key , value in my_profile.items() :
    print(key + ' : '  + value)

