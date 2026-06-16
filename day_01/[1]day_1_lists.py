#[1]Day_1_Lists:
#Excersize of Lists
guests = [ 'Alex', 'John', 'Mark']
print('The invited guests are :' +guests[0] , guests[1], guests[2])
print('Unfortunately! ' + guests[1] +' cannot make to the party')
guests[1] = 'Smith'
print('The new member is :', guests[1])
print(guests)
print('William, Joe and Harris are our three new guests to the party')
guests.insert(2,'William')
guests.append('Joe')
guests.append('Harris')
print(guests)
x= guests.pop(2)
print('We cannot invite '+x)
print(guests)
del guests[1] 
print('We cannot invite Smith')
print(guests)
guests.remove('Harris')
print('We cannot invite Harris')
print(guests)


#Sorting the lists
#Sorting the list is done by sort() method, it sorts the data alphabatically
test_list = ['a' ,'z' , 'x' ,'b' ,'q']
print('Original List')
print(test_list)
print(test_list.sort())     #The sort()  does not return any value 
x= test_list.sort()     #The has value of none
print(test_list)    #The sorted lists is stored in its list, so it will print the sorted list
test_list.sort(reverse=True)    #sorts reverse
print(test_list)
test_list = ['a' ,'z' , 'x' ,'b' ,'q']
print('Original List')
print(test_list)
print(sorted(test_list))    #Can print the sorted lists, but alone sorted(test_lists) will not do sortion alone, it is only done inside the print paranthesis


#Reversing the list
food = ['biryani', 'burger', 'pizza', 'coldrinks']
food.reverse()
print(food)
x=food.reverse()
print(x)    #none


#Length of a list using the len method
n=len(food)
print(n)

#Excersizes
places =[]
places.append('Paris')
places.append('Lahore')
places.append('Islamabad')
places.append('Germany')
print('The places I want to visit:')
print(places)
places.sort()
print('The sorted places list:')
print(places)
places.sort(reverse= True)
print('Reverse alphabetical order')
print(places)
x=places
print(x)
places.reverse()
print('In reverse order:')
print(places)
print(len(places))  #Len() method does return the value





#Chapter 4 (Lists with for loop)
animals =[ 'cat', 'dog' , 'cow' ,'horse']
for i in animals:
    print(i)    #len =4 -> loop runs 4 times ->  whatever the values in  0 to 4 gets stored in i variable, this only works in strifns, lists not in numbers and it is different than for i in range() 
i=1
for animal in animals:
    print(animal.title() +' My ' +str(i)+ ' favorite animal') 
    i=i+1
fruits = ['mango' , 'orange', 'apple', 'grapes']
print(fruits)
for fruit in fruits :
    print('My favorite fruit is :' , fruit)
    print('I really like :' ,fruit)
print('All fruits')


#for loop with numbers
for i in range (1,11):
    print(i)
numbers = list(range(1,11,2))    #Always use list when creating list using range() and store it in a variable
print(numbers)


#** represent exponential
square_numbers= []
for i in range(1,11):
    square_value = i**2
    square_numbers.append(square_value)
    print('Value Stored in ' + str(i) +' iteration : ' +str(square_value))
print(square_numbers)
print(min(square_numbers))
print(max(square_numbers))
print(sum(square_numbers))
#or
