#Day_5_Functions:
#Chapter_6_Functions:
def user_greet() :  #function definiton
    print('hello world')
user_greet()

def user_greet(username) :
    print('Hello' ,username.title() ,'nice to meet you !')
user_greet('qamar')
#The variable username in the function is a parameter , the value 'qamar' inside the user_greet() is the argument.

#Positonal argument
def pet ( animal , owner ) :
    print('My favorite animal is' ,animal.title() , '.\nAnd the owner is' ,owner.title())
pet ( 'cat' , 'qamar')
pet ( 'horse' , 'hamza')

#keyword argument
pet ( owner ='harris' , animal ='bull') #order does not matter in keyword argument, it will store to its res

#Default
def pet ( owner ,  animal = 'dog'   ):  #The default values always comes at last in function defintion
    print('Animal :' ,animal.title())
    print('Owner :' ,owner.title())
pet ('harris')  #Prints default animal 'dog'.
pet ('waqas', 'cow')    #changes dog to cat
pet ('daniyal' ,animal = 'horse' )  #better way 


#Excerisez
def shirt ():
    color = input('Enter the color of  your shirt : ')
    size = input('Enter the size of your shirt : ' )
    print('Your color is : ', color.title())
    print('Your size is : ' ,size.title())
shirt ()

def shirt ( color , size = 'medium'):
    print('Your color is : ', color.title())
    print('Your size is : ' ,size.title())
color = input('Enter the color of  your shirt : ')
size = input('Enter the size of your shirt : ' )
shirt( color , size )
y = shirt ('red' ,'small')  #does not return any value.
print(y)    #prints none


#Return function
def full_name (first_name , last_name ):
    full_name = first_name + ' ' +last_name
    return full_name.title()
my_name = full_name('qamar' ,'jawaid')  #and this will return value will the help of return statement
print(my_name)  #this will print

def full_name (first_name , last_name , middle_name = '' ):
    if middle_name :    #Python interprets as true when middle_name is non empty
        full_name = first_name +' ' + middle_name  +' ' +last_name
    else :
        full_name = first_name + ' '+ last_name
    return full_name.title()
name = full_name ('Muhammad' ,'Jawaid' ,'qamar')
print(name)
name = full_name ( 'Muhammad','jawaid', middle_name ='qamar' )
print(name)

def ice_cream (flavor , toppings , size , company = ''):
    order = { 'flavor' : flavor , 'toppings' : toppings , 'size' : size }
    if company :
        order['company'] = company
    return order
flavor = input('Enter the flavor : ' )
toppings = input('Enter the toppings : ')
size = input('What size you want to eat ? : ')
company = input('What company : ')
order = ice_cream( flavor , toppings , size ,company )
for key , value in order.items() :
    print(key.title(),': ' ,value.title()) 


#Excersizes
def make_album ( artist_name , album_title) :
    album = { 'Singer' : artist_name , 'Album' : album_title }
    return album
albums = []
for i in range (3) :
    artist_name = input('Enter the name of the singer : ')
    album_title = input ('Enter the name of the album : ')
    album_0 = make_album ( artist_name , album_title)
    albums.append(album_0)
for album in albums :
    for key , value in album.items():
        print(key.title() + ' : ' +value.title())

def make_album ( artist_name , album_title) :
    album = { 'Singer' : artist_name , 'Album' : album_title }
    return album
albums =[ ]
while True :
    message = input('Enter yes to continue or no to quit : ').lower().strip()
    if message == 'no' :
        break
    elif message != 'yes' :
        continue
    singer = input('Enter the name of singer : ').title().strip()
    album = input('Enter the album name : ').title().strip()
    info = make_album( singer , album )
    albums.append(info)
    print(albums)


#Passing through a list
usernames = [ 'mark' , 'joe' , 'alex' ] #if i use username ='qamar' , it will see q as index 0 and r as index 4
'''
usernames.sort()    #Important thing i learned is .sort() method sorts the lists but it cannot store the list into that variable we can directly print it
x = sorted(usernames)   #The sorted(usernames) will sort ,the method but wont be able to print until we store it into another variable and print it.
print(usernames)    #In conclusion .sort() sorts and also returns to list but not the variable, sorted() sorts does return to the variable
print(x) '''
def greet ( names ) :
    for name in  sorted(names) :
        message = 'Hello ' + name.title()
        print(message)
greet (usernames) 

completed_projects = []
uncompleted_projects = []
while True :
    message = input('Do you have completed projects ?: ').lower().strip()
    if message == 'no' :
        break
    elif message != 'yes' :
        continue
    completed_project = input('Which project have you completed : ').title().strip()
    completed_projects.append(completed_project)
while True :
    message = input('Do you have uncompleted projects ? : ').lower().strip()
    if message == 'no' :
        break
    elif message != 'yes' :
        continue
    uncompleted_project = input('Which project is  uncompleted : ').title().strip()
    uncompleted_projects.append(uncompleted_project)
def projects (completed_projects ,uncompleted_projects) :
    print('Completed Project : ' ,completed_projects ,'right now.')
    print('Uncompleted Project : ' ,uncompleted_projects ,'right now.')
    while uncompleted_projects :
        current_project = uncompleted_projects.pop()    #Removes the last index
        print('I am currently completing :' ,current_project)
        completed_projects.append(current_project)
def printing ( completed_projects ,uncompleted_projects) :
    for completed_project in completed_projects :
        print('Completed : ' ,completed_project)
    print('Completed Project List :\n' ,completed_projects)
projects (completed_projects ,uncompleted_projects)
printing ( completed_projects ,uncompleted_projects) 


#Copying the list
completed_projects = ['signal generator', 'oscillator' ,'risc v']
z= completed_projects
completed_projects.pop()
print(z)    #As you can see the risc v is removed because , assingmet operator never make copy of list,, we need to slice method or other method
z.append('edc cep')
print(completed_projects)    #Same list not a copy
completed_projects = ['signal generator', 'oscillator' ,'risc v']
z = completed_projects [:]
completed_projects.pop()
print(z)    #Unchanged, independent lists

completed_projects = []
uncompleted_projects = []
while True :
    message = input('Do you have completed projects ?: ').lower().strip()
    if message == 'no' :
        break
    elif message != 'yes' :
        continue
    completed_project = input('Which project have you completed : ').title().strip()
    completed_projects.append(completed_project)
while True :
    message = input('Do you have uncompleted projects ? : ').lower().strip()
    if message == 'no' :
        break
    elif message != 'yes' :
        continue
    uncompleted_project = input('Which project is  uncompleted : ').title().strip()
    uncompleted_projects.append(uncompleted_project)
z= uncompleted_projects[:]
def projects (completed_projects ,uncompleted_projects) :
    print('Completed Project : ' ,completed_projects ,'right now.')
    print('Uncompleted Project : ' ,uncompleted_projects ,'right now.')
    while uncompleted_projects :
        current_project = uncompleted_projects.pop()    #Removes the last index
        print('I am currently completing :' ,current_project)
        completed_projects.append(current_project)
    print(z)    #Modifies the copied list , original remains unchanged
def printing ( completed_projects ,uncompleted_projects) :
    for completed_project in completed_projects :
        print('Completed : ' ,completed_project)
    print('Completed Project List :\n' ,completed_projects)
projects (completed_projects ,z )
printing ( completed_projects ,uncompleted_projects)
print( uncompleted_projects)    #Original list remains unchanged 
print(z)    #copy list gets changed