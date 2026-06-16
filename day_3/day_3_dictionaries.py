#Day_3_Dictionaries:
#Chapter 5
#Continuing from page 105 
students = { 'qamar' : 26 , 'ammar' : 25 ,'owais': 33 , 'noman' : 61 , 'zyan' :28 }
#sorted_students = students.sort()  #works on lists , the sort() method works only on lists not on dictionaries
sorted_students = sorted(students.items())  #It first sorts the items of dictionaries then store it in as a list of tuple not as a dictionary
print(students)
print(sorted_students)
print(students['qamar'])
print(sorted_students[3][0])    #here in sorted_students list of tuple , the first [1] is index of list and the second [1] is the index of tuple for eg: the ('qamar',26) qamar is index [0] and 26 is index[1]
for name , roll_no in sorted_students:  #here 
    print('Name : ' +name.title() + '\nRoll no : ' + str(roll_no))
students['ahmed'] = 23
sorted_students.append(('ahmed' , 23))
sorted_students = sorted(students.items()) 
print(students)
print(sorted_students)
for roll_no in set(students.values()):  #set() ignores the repititve values
    print('Roll no ' + str(roll_no))


#Excerise
rivers = { 'nile' : 'egypt' , 'indus' : 'india' ,'chenab' : 'pakistan' }
for river , country in sorted(rivers.items()):
    print(river.title() , 'flows through from' , country.title())


#Topic_2_Nesting:
student_1 = { 'first_name' : 'qamar' , 'last_name' : 'jawaid'}
student_2 = { 'first_name' : 'ahsan' , 'last_name' : 'owais'}
student_3 = {'first_name' : 'owais' , 'last_name' : 'akbar'}
students = [ student_1 , student_2 , student_3 ]
print(students)
print( students[0]['first_name'].title() )  #0 is the index of list ,inside index 0 a dicitionary who has key 'first_name' which gets printed
print(sorted(students[2].values()))     #the students is a list containing dictionaries to sort define which index list to sort, also dictionaries does not have indexes
for student in students:    #'student' variable stores the dictionary each time loop runs so in the loop body we have key and values but not indexes so we will find student['first_name'] because each time loop runs the new dictionary is stored in the student variable.
    if student ['first_name'] == 'qamar':
        print(student['first_name'].title())
    for key , name  in student.items() :
        if name =='qamar':
            print(key.title())

aliens = []
for i in range (3):
    new_alien = { 'color' : 'red' , 'height' : 5 , 'ship' : 'ufo' }
    aliens.append(new_alien)
    print(aliens)
for alien in aliens :
    for key , values in alien.items() :
        print(key.title() , str(values).title())
print('Total aliens :' , len(aliens))
for alien in aliens [0:2]:
    if alien['color'] == 'red':
        alien['color'] ='pink'
        alien ['height'] = 10
print(aliens)

pizza = { 'crust' : 'thick' , 'toppings' : [ 'onion' , 'sauce' , 'mushrooms' ] }
print(pizza['toppings'])
print('You ordered pizza in ' +pizza['crust'] + ' crust.')
for key , value in pizza.items ():
    if key == 'toppings':
       # print('You ordered pizza with ' +value)   #wont work because the list of toppings has been stored in variable value.
       for value_1 in value:
           print(value_1)

favorite_languages = { 'qamar' : ['python' , 'java' ] , 'jack' : 'c' , 'james' : ['c++' , 'kotlin' , 'python' ]}
for person , language in favorite_languages.items() :
    print('\n' +person.title() , 'favorite languages are : ' )
    for language_1 in language:
        print(language_1.title() , end = '  '  )
    if len(language) == 1 :
        print(person , 'has one favorite language')



#Ending today's coding at 113 page.