from random import choice 
class RandomWalk ( ) :

    def __init__ ( self , num_points = 5000) :
        self.num_points = int(num_points)       #num_points = how many points the walk will have in total , the number of movement in a single decision before changing the direction
        self.x = [ 0 ]      #This is initial coordinates of (x,y) as ( 0, 0 )
        self.y = [ 0 ]

    def fill_walk ( self ) :

        while len(self.x) < self.num_points  :
            x_direction =  choice ( [ 1 , -1 ] )        #Chooses in 1 or -1 , 1 defines the right side and -1 decides the left side 
            x_distance = choice ( [ 0 , 1, 2 , 3, 4 ])          #chooses in list of 0 to 4 it is distance covered horizontally
            x_step = x_direction * x_distance           #this is the step, it is the product of distance and direction , also known as displacement

            y_direction = choice ( [ 1 , -1  ])         #Same concept for y axis, when y distance is 0 walk happens on x axis, and the displacemet on y would be 0.
            y_distance =  choice ([ 0 , 1, 2 , 3, 4 ])          #the direction are the decision for the random walk, we can  say
            y_step  = y_direction * y_distance

            if x_step == 0  and y_step== 0 :    #We stay in our positon when we choose not cover distance in any direction
                continue

            next_x = self.x[-1]  + x_step       #the preivous distance covered + new distance covered is the our cuurent  point we are in on (x,y) plane
            next_y =  self.y[-1] + y_step

            self.x.append ( next_x)
            self.y.append ( next_y)
            ''' Here the return statement is not necessary because object remember their attributes when they are modified inside the function
            but when we need a value we need to return inside the method, but here we dont need the value  the self.x list is modified and is remembered
            in the class. 
            Return when you want a value.
            Don’t return when you change the object.'''




import matplotlib.pyplot as plt 

while True :
    random_walk = RandomWalk ( 100)
    random_walk.fill_walk()
    plt.title ('Random Walk' , fontsize  = 17 )
    point_numbers = list (range ( random_walk.num_points ))         #When not defined python will assume , 0 to random_walk.num_points list , 0 to 5000
    plt.figure( dpi =200 , figsize = ( 10 , 6 ))        #dpi controls the resolution , figsize here 10 inches wide and 6 inches tall
    plt.scatter ( random_walk.x , random_walk.y , c = point_numbers ,    s = 1 , cmap = plt.cm.Blues)
    plt.scatter ( random_walk.x[0] , random_walk.y[0]  , c = 'red' , s = 25 )       #Plots the first and last position of the random walk.
    plt.scatter ( random_walk.x[-1] , random_walk.y[-1]  , c = 'black' , s = 25 )
    #Cleaning up the axes
    '''plt.axis('off')'''

    ''' Equivalent to :
        ax = plt.axes()
    x_axis = ax.get_xaxis()
    x_axis.set_visible(False)
    '''
    #plt is the module amd axes () is the function that returns Axes object, inside the Axes get_xaxis () is the method, it returns Axis object that represent
    # x axis , inside the x axis set_visible ( ) is the method ,  is called Method Chaining.
    plt.show()

    prompt = input('Press Q for exit : ').title().strip()
    if prompt == 'Q' :
        break
    else :
        continue


#Excersizes 
from random import choice as c
class RandomWalk ( ) :

    def __init__ ( self , points = 600 )  :
        self.points = points
        self.x = [ 0 ]
        self.y =  [ 0 ]

    def get_step ( self ) :
        
        direction = c([ 1, -1 ])
        distance = c(range ( 0,7 ) )
        step = direction * distance  
        return step   



    def fill_walk ( self ) :
        
        while len(self.x) < self.points :

            x_step  = self.get_step ( )
            y_step = self.get_step ( )

            if x_step == 0 and y_step == 0 :
                continue

            next_x = self.x[-1] + x_step 
            next_y = self.y[-1] + y_step

            self.x.append ( next_x )
            self.y.append ( next_y )

rw = RandomWalk ( 100 )
rw.fill_walk ( )
print(rw.x , rw.y)

import matplotlib.pyplot as plt

plt.scatter ( rw.x , rw.y , s = 3 , c ='red' )
plt.plot ( rw.x , rw.y , linewidth  = 1 )
plt.grid(True , linewidth = 3)
plt.show ()


#Pygal 
import random
import pygal
from collections import Counter
class Dice ( ) :

    def __init__ ( self , sides ) :
        self.value = 0
        self.sides = sides
    
    def roll_dice ( self ) :
        self.value = random.randint ( 1 , self.sides )

dice = Dice ( 6 )
results = [ ]
for result in range ( 1000 ) :
    dice.roll_dice()
    result = dice.value
    results.append( result )

counts = Counter ( results )
print( counts )
# one important thing that ''' is the string not the comment so only write explanation in ''' not any command , it will cause confusion
frequencies = [ ]
for value in range ( 1 , dice.sides + 1 ) :
    frequency = results.count(value )
    frequencies.append(frequency)
# the value stores 1 to 6 numbers, result.count(1 ) counts number of 1 in the results list and returns, the iteration  hppens from 1 to 6
print(frequencies)
#pygal for presentation , matplotlib for the analysis
#Histogram is bar chart showing how often results occur

hist  = pygal.Bar ()        #pygal library,inside it Bar is class, so the  instance is stored in variable named hist
hist.title = 'Results on rolling a six side dice'   #These following are attributes of the hist instance except for ( );
hist.x_labels = [ '1' , '2' , '3' , '4' ,'5' , '6' ]
hist.x_title = 'Results'
hist.y_title = 'Frequency of result.'
hist.add ( 'Six sided Dice' ,frequencies )          #.add is the method that adds the frequencies element to the chart and the string before that is the explalantion 
hist.render_to_file ( 'die_visual.svg')


#like two using two six sided dice and finding the probablity
import random
import pygal
from collections import Counter
class Dice ( ) :

    def __init__ ( self , sides ) :
        self.value = 0
        self.sides = sides
    
    def roll_dice ( self ) :
        self.value = random.randint ( 1 , self.sides )


dice_1 = Dice ( 6 )
dice_2 =  Dice ( 6 )
results_1 = [ ]
for result in range(1000 ) :
    dice_1.roll_dice ( )
    results_1.append( dice_1.value)

results_2 =  [ ]
for result in range ( 1000 ) :
    dice_2.roll_dice ( )
    results_2.append( dice_2.value)

results = [ ]
for i in range(0 , len(results_1)) :
    sum = results_1[i] + results_2[i]
    results.append( sum )

frequencies = [ ] 
for value in range( 2 , 13 ) :
    frequency = results.count( value )
    frequencies.append(frequency)

hist = pygal.Bar ()
hist.title = 'Playing Ludo with 2 six sided dice'
hist.add('Sum of two six sided dice roll' , frequencies )
hist.x_labels = list(range(2,13))
hist.x_title  =  'Sum'
hist.y_title = 'Frequency'
hist.render_to_file ( 'ludo _dice.svg')


#Toss
from random import choice
import pygal
class Toss ( ) :

    def __init__ ( self ) :
        self.value = ''
    
    def toss_coin ( self ) :
        self.value = choice ( [ 'heads' , 'tails' ] ).title()

toss =  Toss ( )
toss.toss_coin()
print( toss.value )
frequencies = [ ] 
results = []
for value in range ( 10000 ) :
    toss.toss_coin()
    results.append( toss.value)

frequency = results.count('heads'.title())
frequencies.append(frequency)
frequency = results.count('tails'.title())
frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar ()
hist.title = 'Toss'
hist.add('Heads and Tails' , frequencies )
hist.x_labels = ['Heads' ,'Tails']
hist.y_title = 'Frequency'
hist.render_to_file ( 'toss.svg')


#Excerisezes
import random
import matplotlib.pyplot as plt
class Dice ( ) :

    def __init__ ( self , sides = 6) :
        self.value = 0
        self.sides = sides
    
    def roll_dice ( self ) :
        self.value = random.randint ( 1 , self.sides )



dice_1 = Dice ( )
dice_2 = Dice ( )
results  = [ ]
for result in range ( 10000 ) :
    dice_1.roll_dice()
    dice_2.roll_dice()
    results.append( dice_1.value + dice_2.value)

max_value =  (2*(dice_1.sides) + 1)
frequencies = [ ]
for value in range ( 2 , max_value ) :
    frequencies.append ( results.count(value))
print(frequencies)

plt.xlabel ( 'Sum of two dice' , fontsize = 12 )
plt.ylabel ( 'Frequency of results' , fontsize = 12 )
plt.title( 'Two six sided dice' , fontsize = 15 )
plt.scatter ( list(range(2,13)), frequencies , s = 3 , c = 'black')
plt.plot ( list(range(2,13)) , frequencies ,linewidth = 1 ,  c= 'red' )
plt.show()


import matplotlib.pyplot as plt
x= list (range(-1000 , 1001) )
y= [ ]
for val in x :
    if val <= 0 : 
        y.append(-val**2)
    
    else :
        y.append(val**2)


fig, ax = plt.subplots()

ax.plot(x, y)

# Move axes to the center
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Hide the other two spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks only on bottom and left
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.show()