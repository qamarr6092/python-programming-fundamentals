#Day_6_Functions:
#Chapter_6_Functions:
def show_magicians ( magicians) :
    for magician in magicians :
        print(magician.title())
def make_great ( magicians ) :
    for i in range(len(magicians)) :
        magicians[i] = 'Great ' + magicians[i].title()
    print(magicians)
def make_great_copy ( magicians) :
    magicians_copy = magicians [ : ]
    return magicians_copy
magicians = [ 'charile' ,'carl' ,'michael' ,'smith' ,'mark' ]
show_magicians (magicians)
make_great ( magicians )
copy = make_great_copy ( magicians)
print(copy)


#Arbitary Argument
def make_pizza ( toppings ) :
    print(toppings.title())
make_pizza ('cheese'  ) #Cannot take more than one argument
def make_pizza (*toppings ) :   #Python stores them in a tuple, we need a for loop for .title()
    for topping in toppings :
        print(topping.title())
make_pizza ('cheese' , 'carrot' ,'chicken')
# *toppings tells python to create empty tuple called toppings and stores whatever value it recieves
#arbitary argument always at last
def make_pizza ( size , *toppings ) :
    print('Making pizza size : ' +size.title())
    for topping in toppings :
        print('-', topping.title())
make_pizza ('large' , 'cheese' ,'chicken' , 'tikka' , 'mayo')

#* creates the empty tuple and stores whatever value it recivees
#** creaetes the dictionary
def make_user_profile ( first_name , last_name , **info ) :
    user_profile = { }
    user_profile ['first_name'] = first_name.title()
    user_profile [ 'last_name' ] = last_name.title()
    for key , value in info.items () :
        user_profile [key] = value.title()
    return user_profile
my_profile = make_user_profile ('qamar' ,'jawaid' ,university = 'ned' , city = 'karachi' )
print(my_profile)


#Excerisizes
#* is the number of positional arguments
#** is the number of keyword arguments
def create_profile () :
    profile ={ }
    i = 0
    while i < 1 :
        prompt = input('Do you wish to continue : ').lower().strip()
        if prompt == 'no' :
            break
        elif prompt != 'yes' :
            continue 
        first_name = input ('Enter the first name : ').title().strip()
        profile['First Name'] = first_name
        last_name = input ('Enter the last name : ').title().strip()
        profile['Last Name'] = last_name
        i += 1
        while True :
            message = input('Do you have additional details : ').lower().strip()
            if message == 'no' :
                break
            elif message != 'yes' :
                continue 
            detail_key = input ('Enter the additonal key : ').title().strip()
            detail_value = input ('Enter the addiotnal value : ').title().strip()
            profile[detail_key] = detail_value
    return profile
my_profile = create_profile () 
for key , value in my_profile.items() :
    print(key + ' : '  + value)


#Excersizes
def sandwiches ( *items ) :
    print('Making sandwich : ')
    for item in items :
        print('-' ,item.title())
sandwiches ( 'chicken ' , 'tikka' ,'sauce' )

def make_car ( manufacturer , model_name , **info) :
    car_info = { }
    car_info ['Manufacturer'] =  manufacturer .title().strip()
    car_info ['Model Name'] = model_name.title().strip()
    for key , value in info.items () :
        car_info [ key.title().strip()] = value.title().strip()
    return car_info
car = make_car ( 'toyota' , 'mx-2220' , color = 'blue' , seats = '5 seater' )
for key, value in car .items () :
    print(key + ' : '  + value)
