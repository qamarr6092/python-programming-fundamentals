'''unittest test the code when we give set of input and test what should be given as output as what we give it to be,
the file_name , method_name must start with 'test' in order them to run automatically ' but it is good to start ClassName
with test as well.'''


import unittest 
from name import get_formatted_name 

class TestName ( unittest.TestCase ) :  #The 'unittest' is module and that module holds the class 'TestCase' which is inherited from 'TestName'

    def test_first_name_last_name ( self ) :    #any method starting from 'test_' will always run , so need to call

        formatted_name = get_formatted_name ( 'qamar' , 'jawaid')
        self.assertEqual ( formatted_name , 'Qamar Jawaid')      #The assertEqual method compares two arguments
    
    def test_first_name_middle_name_last_name ( self ) :
        formatted_name = get_formatted_name ( 'muhammad' , 'jawaid' , 'qamar' )
        self.assertEqual ( formatted_name , 'Muhammad Qamar Jawaid')

unittest.main() 
'''unittest.main () method finds all classes that inherits from unittest.TestCase and runs each method starting from test_.'''
'''when explicity called unittest.main() we can run without the start of 'test' in the file name start'''
''' The '.'  in output terminal represent the number of method has run successful , number of 'F' defines the failure of number of methods and also we can
see in the terminal which method failed'''
''' The methods inside the Class that inherits from unittest.TestCase does not need any parameter except self, unittest.main () automatically calls 
those methods starting_from 'test' by creating an instance on its own automatically that calls those methods, so no parameter and information of input needed, 
the information is giviven inside the method definition'''



import unittest
from cities import get_location as location
class TestLocation ( unittest.TestCase ) :
    def test_location ( self ) :
        get_location  = location ( 'paris' , 'france' , 3000000 )
        self.assertEqual ( get_location , 'Paris, France - Population = 3000000')
#any code wont exrcute after the following lines in assertEqual if assert fails:
        
unittest.main()
'''
Method Use
assertEqual(a, b) Verify that a == b
assertNotEqual(a, b) Verify that a != b
assertTrue(x) Verify that x is True
assertFalse(x) Verify that x is False
assertIn(item, list) Verify that item is in list
assertNotIn(item, list) Verify that item is not in list
'''

from survey import AnonymousSurvey 
import unittest

class TestSurvey ( unittest.TestCase ) :

    def test_single_response ( self ) :
        question = ('What is your first programming language? ')
        my_survey = AnonymousSurvey ( question )
        my_survey.store_response('C')
        self.assertIn ( 'C' , my_survey.responses)
    def test_multiple_response ( self ) :
        question = ('What is your first programming language? ')
        my_survey = AnonymousSurvey ( question )
        responses = [ 'Java' , 'Python' , 'C' ]
        for response in responses :
            my_survey.store_response(response)
            self.assertIn ( response, my_survey.responses )
unittest.main()


'''The unittest.TestCase Class has setUp() method that allows you to create objects of your own class once and you can use them 
in methods of unittest class'''
'''Python runs setUp() method first then other test methods'''

from survey import AnonymousSurvey 
import unittest

class TestSurvey ( unittest.TestCase ) :
    def setUp ( self ) :
        question = 'What is the best programming language ? '
        self.my_survey = AnonymousSurvey (question)
        self.responses = [ 'C' , 'Python' , 'Java' ]
        for response in self.responses :
            self.my_survey.store_response(response)
            
    def test_single_response ( self ) :
        self.assertIn ( 'C' , self.my_survey.responses)

    def test_multiple_response ( self ) :
        i = 0
        for response in self.my_survey.responses :
            self.assertIn( self.responses[i] , self.my_survey.responses[i] )
            i+=1
unittest.main()


#Excersizes :
import unittest
class Employee () :
    def __init__ ( self , first_name , last_name , annual_salary ) :
        self.first_name = first_name.title().strip()
        self.last_name = last_name.title().strip()
        self.annual_salary = annual_salary

    def give_raise ( self , raise_amount= 500) :
        self.annual_salary += raise_amount
        return self.annual_salary

class TestEmployee ( unittest.TestCase ) :
    
    def setUp ( self ) :
        self.employee = Employee ('qamar' , 'jawaid' , 5000 )
    
    def test_default_raise ( self ) :
        annual_salary = self.employee.give_raise()
        self.assertEqual ( annual_salary , self.employee.annual_salary )
    
    def test_custom_raise ( self ) :
        annual_salary = self.employee.give_raise ( 700 )
        self.assertEqual  ( annual_salary , self.employee.annual_salary )

unittest.main()