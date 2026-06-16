#Day_9_Files_And_Exceptions:
#Chapter_8:

file_path = 'pi_digit_1.txt'
with open( file_path ) as file :
    lines = file.readlines()   #Stores line by line inside a list called 'lines'.
pi=''
for line  in lines :
    pi += line
birthday = input('Enter the birthday ')
if birthday in pi :
    print('It exists:')
else :
    print('does not exist')


#Excersizes:
file_path = 'text_files/learning_python.txt' 
with open( file_path ) as file_object :
    contents = file_object.read()
print( contents)

with open(file_path ) as file_object :
    lines = file_object.readlines()
print('\n')
for line in lines :
    print(line.rstrip())

with open(file_path ) as file_object :
    print('\n')
    for line in file_object :   #Here file_object is not a list , but a connection to actual file , but it is also iterator so we can iterate over to print whatever is written inside it.
        print(line.strip())

message = 'Python is better than Java'
new_message = message.replace('Python' ,'C' )
print(new_message)
new_message = message.replace('Pytho' ,'C' )
print(new_message)
print(message)

file_path  = 'text_files/learning_python.txt'
with open (file_path) as  file :
    contents = file.read()
    print(contents.replace('Python' , 'C').rstrip())

file_name = 'python.txt'                        
''' When we use 'w' write mode in a file, python creates that file on its own and we can write what we want'''
# If file EXISTS: Overwrites (deletes old content)
# If file DOESN'T exist: Creates new file
with open ( 'python.txt'  ,'w' ) as file_object :
    file_object.write('I love Python more than Java')

with open ( 'text_files/learning_python.txt' , 'w' ) as file_object:   #It removed the previous text and wrote what we write in next statement
    file_object.write('I love Python than Java\nand it is easier.')

#'a' append mode is like 'w' mode, it writes the text in the file but it does not erase the existing file, it simply writes at the end of the line
#if file does not exist it creates the new file and writes
file_name ='text_files/learning_python.txt'
with open ( file_name , 'a' ) as file_object :
    file_object.write('\nJava has verbose syntax and has limited and strict work in Pakistan')


#Excersizes 
guests = [ ]
while True :
    message = input ('Do you want to enter our party ? ').strip().lower()
    if message == 'no' :
        break
    elif message  != 'yes' :
        continue
    guest = input('Enter the guest name for atttending the party : ').title().strip()
    guests.append(guest)

file_name = 'guests.txt'
with open ( file_name , 'w' ) as file_object :
    file_object.write('Invited Guest List:\n')
    s_no = 1
    for guest in guests :
        file_object.write(str(s_no) + '.)' +guest  + '\n' )
        s_no +=1

#Programming Poll :
while True :
    message = input ('Do you want ? ').strip().lower()
    if message == 'no' :
        break
    elif message  != 'yes' :
        continue
    reason = input ('Why do you like programming : ').title().strip()
    file_name = 'programming_poll.txt'
    if reason :
        with open ( file_name , 'a' ) as file :
            file.write(reason + '\n' )


#Exception
while True :
    message = input ('Do you want to continue ? ').strip().lower()
    if message == 'no' :
        break
    elif message  != 'yes' :
        continue
    try :                                               #Only code that might cause error gets written inside the try block
        num_1 = int(input('Enter the number : '))
        num_2 = int( input('Enter the number : '))
        div = num_1 / num_2
    except ValueError :
        print('Cannot take string')
    except ZeroDivisionError :
        print('Cannot divide by 0')
    else :
        print(div)
    finally :   #This block will always run , else block only runs when no error met
        print('Program has run')

#FileNotFoundError is caused by when file does not exist , misspelled , different directory
file_name = 'text_files/learning_python.txt'
try :
    with open ( file_name , 'r' ) as file:
        contents = file.readlines ()
except FileNotFoundError :
    print('File not found')
else :
    print(contents )                #readlines () always returns list, read() and readline() returns string.
finally : 
    print('Program run successfully')

name = 'Muhammad Qamar Jawaid'
new = name.split()  #Splits each word and stores it in list as items, when countered space , it consider that as word
print(name)
print ( new)

file_path = 'python_crash_course_summary.txt'
try :
    with open ( file_path , 'r') as file_object :
        contents = file_object.read()
except FileNotFoundError :
    print('File is missing')
else :
    words = contents.split()
    print(len(words))

def count_words ( file_path ) :
    try :
        with open ( file_path , 'r' ) as file_object :
            contents  = file_object.read ( )
    except FileNotFoundError :
        '''print(file_path.title() + ' is missing')    
            we can also not print that the error has caused, the except statement handles the error and continues the program to run
            but we can display none by using 'pass' keyword.'''
        pass
    else :
        words = contents.split()
        num_of_words = len(words)
        print(file_path.title() + ' has the total ' + str(num_of_words) + ' words' )

files = ['python_crash_course_summary.txt' , 'guests.txt' , 'python.txt' ,'learning_python.txt' ]
for file in files :
    count_words ( file )

try :
    with open ('python_crash_course_summary.txt' , 'r') as file :
        contents = file.read()
except FileNotFoundError:
    print('File is missing')
else :
    count = contents.lower().count('python')
    print(count)
    count_1 = contents.title().count('Python')
    print(count_1)
print('The word' + ' Python ' + 'has appeared ' + str(count_1) + ' times.' )

import json 
numbers = [ 2,4,6,8,10 ]
file_name = 'numbers.json'
with open ( file_name , 'w' ) as f_obj :
    json.dump(numbers , f_obj ) #json.dump() takes two argument, 1.) piece of data, 2.) and a file_object it can use to store that data
with open ( file_name  , 'r') as f_obj :
    numbers_json =json.load(f_obj)
print ( numbers_json )
'''json.load() and json.dump() are the methods or functions'''
'''while the file_object.readlines() is also a method or file_object.write(' ') but it is simpler than json'''

import json
name = input('Enter the name : ').title()
print('We will remember your name' ,name )
file_name = 'name.json'
with open (file_name , 'w' ) as file_object :
    json.dump (name , file_object )
with open ( file_name , 'r' ) as file_object :
    name_from_file = json.load(file_object) 
print('I told you' ,name_from_file )

import json 
file_name = 'new.json'
try :
    ''' If the user has run the program once, it will greet , otherwise it will first take their name'''
    with open ( file_name , 'r' ) as f_obj :
        name_from_file = json.load ( f_obj )
except FileNotFoundError :
    name = input('Enter the name : ').title().strip()
    print('We will remember your name the next time.')
    with open ( file_name , 'w' ) as f_obj :
        json.dump ( name , f_obj )
else :
    print(name_from_file)

#Ending todays coding at page number 211.