#Day_4_Dictionaries:
#Chapter_5 
#Continuing from page 113
students = { 'qamar' : { 'first_name' : 'qamar' , 'last_name' : 'jawaid' , 'class' : 'second year' } ,
            'owais' : { 'first_name' : 'owais' , 'last_name' : 'akbar' , 'class' : 'second year' } ,
            'hamza' : { 'first_name' : 'hamza' , 'last_name' : 'ali' , 'class' : 'fourth year' } }
for student , student_infos in students.items() :
    print('\nStudent ' + student.title() + ' info:')
    for key , student_info in student_infos.items():
        print (key.title()+ ' : ' +student_info.title())
print('Total number of students : ' +str(len(students)))


#Exercizes
cities = { 'karachi' : { 'country' : 'pakistan' , 'population' : 1200000 } , 
        'lahore' : { 'country' : 'pakistan' , 'population' : 8500000 } ,
        'paris' : { 'country' : 'france' , 'population' : 40000 } }
for city , info in cities.items() :
    print(city.title() + ' :' )
    for key , info_1 in info.items() :
        print(key.title() +' : ' + str(info_1).title())