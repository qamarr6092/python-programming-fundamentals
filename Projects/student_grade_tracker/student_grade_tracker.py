#Day_12_Student_Grade_Tracker:
#Mini_Project:

import json
file_name = 'student_grade_tracker.json'
try :
    with open ( file_name , 'r' ) as file_object :
        students = json.load( file_object )
except FileNotFoundError :
    print('No data in the existing file yet.')
    students = { }
else :
    print('Data loaded succesfully')
    print('To add more information , Choose valid options below.')

def add_student ( name , subject ,  marks ) :
    if name not in students :
        students [ name ] = { }                 #Creates the empty dictionary that holds name , student = { name : { }}
        students[name][subject] = marks         #Creates students = { name : { subject : marks } } , it will create new key value pair in a nested dict if name matches
        print('Student : ' + name + ' has been added.')
    else :
        print('Student : ' + name + ' is already present in our record. Use different name ')
    return students

def add_subject ( name , subject , marks ) :
    if name in students.keys() :
        if subject not in students[name].keys() :
            students[name][subject] =marks
            print(subject + ' has been added in your record.')
            return students
        else :
            print(subject + ' is already present in your record.')
    else :
        print('Student : ' + name + ' is not present in our record.')

def remove_student( name ) :
    if name in students.keys():
        del students[name]
        print('Student : ' +name + ' has been removed from our record.')
        return students 
    else :
        print('Student : ' + name + ' is not present in our record.')
        return None

def update_marks ( name , subject , marks ) :
    if name in students.keys() :
        if subject in students[name].keys():
            students[name][subject] = marks
            print('Marks has been updated.')
            return students
        else :
            print(subject + ' is not present in your record.')
            return None
    else :
            print('Student : ' + name + ' is not present in our record.')
            return None
            

def calculate_grade ( name ) :
    marks = 0
    if name in students.keys() :
        for mark in students[name].values():
            marks += mark
        num_of_subjects = len(students[name])
        average = marks/num_of_subjects
        return average
    else :
        print('Student : ' + name + ' is not present in our record.')
        return None

def show_students ( ) :
    average_list = [ ] 
    i= 0
    for student , info in students.items() :
        average =  calculate_grade ( student )
        average_list.append( average )

    print('Students in our record')
    y=1
    for student , info in students.items() :    
        print(str(y) + '.)    Student : ' + student )
        y+=1
        z=1
        for subject , marks in info.items() :
            print(str(z)  +  '.)   Subject : ' + subject + ' ------ ' + ' Marks : ' + str(marks) )
            z+=1

        print('Average : ' + str(average_list[i]) )
        i+=1

while True :
    print('1.) Add Student in our record.' )
    print('2.) Add Subject in your record.' )
    print('3.) Remove Student from record.')
    print('4.) Update marks for Student.')
    print('5.) Calculate grade for Student.')
    print('6.) Show all Students from record.')
    print('7.) Exit')

    try :
        choice = int(input('Enter the choice : '))
    except ValueError :
        print('Enter choice in numeric values.')
        continue
    else :
        if choice == 1 :
            name = input('Enter the name of student : ').title().strip()
            subject = input('Enter the subject name : ').title().strip()
            try :
                marks = int (input( 'Enter the marks of ' + subject +' : '))
            except ValueError :
                print('Enter marks in numeric value.')
            else :
                add_student(name, subject , marks)
        
        elif choice == 2 :
            name = input('Enter the name of student : ').title().strip()
            subject = input('Enter the subject name you want to add in your record : ').title().strip()
            try :
                marks = int (input( 'Enter the marks of ' + subject +' : '))
            except ValueError :
                print('Enter marks in numeric value.')
            else :
                add_subject(name, subject, marks )
        
        elif choice == 3 :
            name = input('Enter the name of student : ').title().strip()
            remove_student(name)
        
        elif choice == 4 :
            
            name = input('Enter the name of student : ').title().strip()
            subject = input('Enter the subject name you want to update : ').title().strip()
            try :
                marks = int (input( 'Enter the marks of ' + subject +' : '))
            except ValueError :
                print('Enter marks in numeric value.')
            else :
                update_marks( name, subject , marks )
            
        elif choice == 5 :
            name = input('Enter the name of student : ').title().strip()
            average = calculate_grade ( name )
            print('Average of ' + name + ' : ' + str(average ))
        
        elif choice == 6  :
            show_students()
        
        elif choice == 7 :
            print('Exited')
            break

        else :
            print('Invalid Choice')
            continue

show_students()

with open ( file_name , 'w' ) as file_object :
    json.dump( students , file_object )