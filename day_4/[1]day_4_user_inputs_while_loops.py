#Day_4_User_Inputs:
#Chapter_6:
message = input ('Enter something : ')
print(message)
age = (input('age : '))
age = int(age)
if age >=19:
    print(age)
#The modulus operate just gives the remainder and the remainder is always in integer value 
number_1 = float (input('Enter a number : '))
number_2 = float (input('Enter a number : '))
number = number_1 % number_2
number = float(number)
print(number)


#Excersizes 
number = int (input('Enter a number : '))
if number % 10 == 0:
    print('Number is divisible by 10')
else :
    print('Not divisible')


#Topic_2_While_Loops:
number = 1
while number <=5:
    print(number)
    number += 1

message = input("Enter 'quit' to quit the game: ")
while message != 'quit' :
    print('Keep playing')
    message = input("Enter 'quit' to quit the game: ")
print('Exited')

active = True 
while active :
    message = input ('Enter quit to to stop : ' )
    if message == 'quit':
        active = False  #Python has no scope , the variable scope only exists in oops and the functions.
print('Exited')

while True :
    number = int(input('Enter the number : '))
    if number == 10:
        break   #the break keyword compeletly exits the loop when conditon met true skipping the remaining line of codes
    else :
        print(number)
print('exited')

print('Odd numbers : ' )
count = 0
while count < 10:
    count +=1
    if count % 2 == 0:
        continue    #the continue keyword is completely different than the break keyword, when conditon met the continue sends flow at the starting of loop
    print(count)
    

#Excersizes
price = 0
while True:
    message = input('Press Q to quit the machine (or press Enter to continue): ')
    if message == 'Q':
        break
    age = int(input('Enter the age for the ticket price: '))
    if age <= 12:
        ticket = 0
        print('For children the ticket price is:', ticket, '$')
    elif age <= 19:
        ticket = 15
        print('For teenagers the ticket price is:', ticket, '$')
    else:
        ticket = 30
        print('For adults the ticket price is:', ticket, '$')
    price += ticket   # accumulate total
print('Your total bill is:', price, '$')

balance = 0
while True :
    print('Welcome to ATM :')
    message = input('To deposit press D , To quit press Q :' ).upper()
    if message == 'Q':
        break
    elif message != 'D':
        continue
    amount = float(input('Enter the amount to be deposited : '))
    if amount < 0:
        print('Enter the valid amount !')
        continue
    else :
        balance += amount
print('Your total balance : ' + str(balance) +'$')


#while loop with dictionaries and lists
#the for loop will run depending on the number of indexes present in the dictionaries and lists
#but the while loop will run till the list or dictionary is not empty
unconfirmed_users = [ 'mark' , 'alex' , 'harris' , 'joe' ]
confirmed_users = []
while unconfirmed_users :
    current_user = unconfirmed_users.pop()  #joe is first to removed and mark is last to removed
    print('Verifying the user : ' +current_user.title())
    confirmed_users.append(current_user)
for confirmed_user in sorted(confirmed_users):
    print('Verified users : ' +confirmed_user.title())  #if we didnt sort the list the first to get printed would be joe 

#To delete multiple values from the list
#using for loop
animals = ['dog' , 'bull' ,'cat' ,  'cow' , 'cat' , 'fish' ,'cat']
print(animals)
for animal  in animals :
    if animal == 'cat':
        animals.remove(animal)
print(animals)

#using while loop
animals = ['dog' , 'bull' ,'cat' ,  'cow' , 'cat' , 'fish' ,'cat']
while 'cat' in animals :    #Runs times how many cat present in animals list
        animals.remove('cat')
print(animals)

students = {}
while True :
    response = input('Do you want to register : ').lower().strip()
    if (response == 'no') :
        break
    elif ( response != 'yes') :
        continue                         
    name = input('Enter name : ')
    year = int(input('Enter year : '))                  
    students[name] = year
print('Students Registered : '+str(len(students)) )  
for name , year in students.items():
    print(name.title() +' : ' +str(year),'Year')
 
sandwich_orders = ['cheese', 'tikka', 'chicken', 'potato']
finished_orders = []
while sandwich_orders:          # loop until list is empty
    current = sandwich_orders.pop(0)   # remove first element
    print('I am making ' + current.title() + ' right now.')
    finished_orders.append(current)
print('\nFinished orders:', finished_orders)
    


