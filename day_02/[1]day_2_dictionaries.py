#[1]Day_2_Dictionaries
#Chapter_5
qamar = { 'height' : 175 , 'birthplace' : 'pakistan' , 'age' : 19}   #here birthplace and height are the key the value are next to them seperated by :
print(qamar['height'] ,qamar['birthplace'])
print('My age is :' , qamar['age'])
qamar['university'] = 'ned' #adds the key and the value
print('I study in' ,qamar['university'])
print(qamar)
qamar ={}   #sets back to zero
print(qamar)
qamar ['height'] = 175
qamar ['age'] =19
qamar ['country'] = 'pakistan'
print(qamar)
qamar['country'] ='usa' #modifying the dictionary
print(qamar)
del qamar['country']    #deleting
print (qamar)
favorite_languages = { 'mark' : 'c' , 'alex' : 'php' , 'harris' : 'javascript' , 'qamar' : 'python' }
print('Mark favorite language : ' + favorite_languages['mark'].title() +'\nMy favorite language : ' + favorite_languages['qamar'].title())


#Excersizes
favorite_numbers = { 'Ammar' : 25 , 'Owais' : 33 , 'Qamar' : 26 , 'Zain' : 24} 
print('My favorite number is : ' , favorite_numbers['Qamar'])

myself = { 'first_name' : 'Qamar' , 'last_name' : 'Jawaid', 'city' : 'Karachi' , 'uni': 'Ned'}
print('First Name:' , myself['first_name'] ,'\nLast Name:',myself[ 'last_name'])
print(myself)


#Looping through the dictionary
for key , value in myself.items():  #Loop runs on how many keys are present , key variable stores the key and changes during each iteration similarly the value variable 
    print(key, value)

for information in myself.keys():   #Only stores and prints key when we do not care about the values stored inside it we used keys() method , earlier we used items() method
    print(information.title())

favorite_languages = { 'mark' :'C' , 'joseph' : 'Python' , 'joseph' : 'Java' ,'qamar' :'Python'}
friends = [ 'mark' , 'joseph']
for keys in favorite_languages.keys() :
    if keys in friends:
        print(keys+ "'s" + ' language is ' + favorite_languages [keys])
        


#Ending today's coding with page_number 105