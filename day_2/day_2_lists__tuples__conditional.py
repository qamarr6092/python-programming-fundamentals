#Day_2
#Chapter_4_Lists:
odd_numbers= list(range(1,11,2))
print(odd_numbers)
print(max(odd_numbers))
print(min(odd_numbers))


#List Comprehension
odd_numbers = [ i for i in range (1,11,2)]    #Value will be stored in i variable
print(odd_numbers)


#Excersizes 
#Print Numbers 1to20
for i in range(1,21):
    print(i)
#Make a list from 1 to 1000 and print
x= list(range(1,1001))
print(x)
y= [ i for i in range(1,1001)] 
print(y)
print(y[2])
print(sum(y))    #max() ,sum(), min() are useful they are used to find sum , min , max values inside the lists
print(max(y))
z=min(y)
print(z)
#Odd_Numbers
z=0
odd_numbers = []
for i in range (1,21,2):
    odd_numbers.insert(z,i)
    z=z+1
    print(odd_numbers)
#Cube
cubes =[]
for cube in range (1,11):
    cubes.append(cube**3)
    print(cubes)
#List comprehension to generate cubes
cubes_1= [ value **3 for value in range(1,11)] 
#print(value) wont work
print(cubes_1)


#Slicing The List
z=cubes_1[0:2]    #Slices the loop and stores the values in 'z' but it does not cut the list , it remains its original state
print(z)
print(z[0:1])
print(cubes_1[-3:-1], cubes_1[3:6])
print(cubes_1[:3])     #first three cubes [:3] starts from the beginning
print(cubes_1[4:])    #last cubes except the first four
print(cubes_1[-2:])    #Last two cubes


#Looping through a slice
characters = ['sasuke' , 'kakashi', 'jiraiya' ,'izuna' ,'naruto' , 'shikamaru']
for character in characters[3:]:
    print(character.title())
for i in range(3,6):
    z=characters[i].title()
    print(z)
    print(characters[i].title())




#Topic_2_Tuples:
dimensions =(200,50)    #Is a tuple with indexes whose values does not chabge
print(dimensions[0])
for dimension in dimensions:
    print(dimension)
print('\nOriginal Tuple:' , dimensions)
dimensions =(1000,800)
print('\nChanged Tuple:' , dimensions)
favorite_foods= ('pizza' ,'burger', 'chips')
print(favorite_foods)




#Chapter_5_Conditional_Tests:
#Topic_1_if_else:
actors = ['shahrukh', 'Amir' ,'hrithik', 'salman', 'akshay']
print(actors[0] =='shahrukh')    #prints true
print(actors[1] =='amir')
print(actors[1].title() == 'Amir')
print(actors[1])
if actors[0].lower()  not in actors:
    print('Not found')
else:
    print('Shahrukh present')
x=2 
y=4
z=0.1
if ( x>=2 and y>=2 and z<=0.8):    #and logic gate
    print(True)
print( x>=2 or z=='qamar' or y==9)    #or logic gate
banned_user = ['joe', 'mark', 'sam']
if 'mark' in banned_user:
    print('Mark is a banned user')
if 'qamar' not in banned_user:
    print('Qamar is not banned user')


#Excerise
alien_colors= [ 'red' ,'yellow', 'green']
if 'green' in alien_colors:
    print('Player has earned the point')
if 'red' in alien_colors:
    print('You earned 10 points')
if 'yellow' in alien_colors:
    print('You earned 15 points')
if 'pink' in alien_colors:
    print('You failed!')
    
age= int(input("Enter the person's age:"))
if (age <=10):
    print('The person is a child')
elif (age > 10 and age < 20):
    print('The person is a teenager')
elif (age>= 20 and age<= 45):
    print('The person is an adult')
else :
    print('The person is the old person')
    
food_items = ['pizza' , 'cakes', 'hamburgers' ,'pasta' ]
for food_item in food_items:
    print('We have total', len(food_items), 'items')
    if ( food_item == 'cakes'):
        print('Sorry! we are out of :',food_item.title())
    else :
        print('Adding the' ,food_item,'.Please ! wait while its getting ready')


requested_orders =[]
if requested_orders:    #This results true when list has at least one element otherwise it returns false
    for requested_order in requested_orders:
        print('Making :', requested_order)
else:
    print('Please order something before sending the request')

available_food_items = ['biryani', 'pizza', 'burger', 'sandwiches', 'french fries']
ordered_food_items = ['french fries', 'pizza', 'cookies', 'sweets', 'biryani']
for ordered_food_item in ordered_food_items:
    if ordered_food_item in available_food_items:
        print('We are adding the', ordered_food_item.title())
    else:
        print('We do not have the', ordered_food_item.title())


#Excersize
users = ['mark', 'william' ,'joe' , 'admin' ,'alex']
for user in users :
    if user == 'admin':
        print('Welcome Sir', user , '.Thanks for joining us')
    else :
        print('Hello! Thanks for logging in' ,user)
    
if users:
    print('We have following users', users, 'and we want remove everyone except the admin')
    users = ['admin']
    print('Users :' , users)

current_users =[ 'abdullah' ,'ahmed' , 'ubaid' ,'hamza' ,'uzair' ]
new_users = [ 'daniyal', 'ahmed' ,'bilal' ,'arshad' ,'abdullah' ]
for new_user in new_users:
    if new_user in current_users:
        print( new_user, 'is already in use try different one' )
    else :
        print( new_user, 'can be used' )

balls = int( input('Enter the number of balls batsman has faced: ' ))
runs = int ( input( 'Enter the runs scored by batsman : '))
strike_rate = (runs * 100) / balls
print('Strike Rate:' ,strike_rate)