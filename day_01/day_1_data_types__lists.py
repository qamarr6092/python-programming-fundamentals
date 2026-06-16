#Day 1  [ Chapter_1 : Variables ]
# Topic_1: Data_Types_String
name = 'Muhammad qAmaR '
print(name)
print(name.title()) # The 'title' method does not take any argument it has default 1 argument , Given as str.title()
print(name.upper())
print(name.lower()) 


#Combining Strings
first_name = 'Qamar' 
second_name ='Jawaid'
full_name = first_name +' ' + second_name
print(full_name)
print(first_name + ' ' + second_name)
print(full_name.title())
print(full_name.upper())
print('Hello my full name is ' + full_name.upper() + '!')


#whitespaces
#\n used for a newline
#\t used for tab and extra spaces
print('First Name : \t' +first_name)
print('\nSecond Name: \t' +second_name.upper())
#The strip() method, 1. rstrip() remove extra whitespace from string  2. lstrip() removes from left side 3. strip() removes  from both ends, strip() method can hold the argument unlike title() method,  Can be a useful function
# String can be terminated by only like quotes


#Excersizes
print( "Albert Einstein Said :" ' "A person who never made mistakes never tried anything new " ')
#" ' can cause problems , Choose accordingly
name_1 =' Ammar '
print(name_1.rstrip())
print(name_1.lstrip())
print(name_1.strip())




#Topic_2 : Numbers
#The str() method can make any data_type into string
age = 19 #Integer value
print('My age is ' + str(age))
print(1/2) #prints a float value
import this #This prints the Python Idea for its creation





#Chapter 3 : [Lists]
#Topic_1: (Lists)
characters = [ 'Sasuke', 'Naruto' , 'Light']
print(characters)     #prints with the square brackets
print(characters[0])
print(characters[2])
print((characters[1] + characters[2]).upper()) #Upper case + combining strings 
print(characters[-1]) #'-1' index indicates the last element of a list, '-2' is thr second last element of list


#Excersize 
favorite_cars = ['Toyota' , 'Civic', 'Honda']
print('My two favorite cars are :\t' +favorite_cars[0].lower() +' and ' +favorite_cars[-2].lower())


#Modifying The Lists
test_list = ['Daniyal', 'Abdullah' , 'Ahmed', 'Umar' , 'Mujtuba']
print(test_list)
test_list[-2] ='Waqas' #Modifying The List
print(test_list)


#Adding The Element In The List
#We use the .append () It will always add the new element at the end of the list
test_list.append('Hadi')
print(test_list)


#Building List Dynamacilly by adding
favorite_singers =[ ]
favorite_singers.append('Udit Narayan  ')
favorite_singers.append('Alka')
favorite_singers.append('Kumar')
favorite_singers[0]=favorite_singers[0].rstrip()
print(favorite_singers)


#Insertint Element 
#It uses the insert() method the next elements of a list shift by one
favorite_singers.insert(2,'Sonu Nigam')
print(favorite_singers)


#Deleting an element
#It uses del method
del favorite_singers[2]
print(favorite_singers)
x=favorite_singers.pop()   # Removes the last element but stores the value back to x unlike del emthod who does not remember the removed value
print(favorite_singers)
print(x)


#We Can pop at any index
print('My favorite singer is' + favorite_singers.pop(0))

print(favorite_singers)


#Removing When index in unknown
#lets first add a element
favorite_singers.insert(0,'Udit Narayan')
favorite_singers.append('Kumar')
print(favorite_singers)
y=favorite_singers.remove('Alka')
print(favorite_singers )
print(y)  #So only pop() stores the vakye not remove () method

