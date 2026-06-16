#Day_15
#Matplotlib

import matplotlib.pyplot as plt
''' matplotlib is the package or library , inside it there is pyplot module that holds the functions
such as plot () show () '''
squares = [ 1 , 4, 9 , 16, 25 ]
input_numbers = [ 1 , 2 ,3 ,4 ,5 ]
#plt.plot ( squares , linewidth = 2)         #sets the width of a line in the chart when plot ( ) is called

''' the plot ( ) function assumes that the first value correspondes to the 0 on x axis , which means square of 0 is 1 this is the default
behaviour when input is not given inside the plot ( ) function as argument.'''

plt.plot ( input_numbers , squares , linewidth = 3 )

plt.title ( 'Sqaure Numbers' , fontsize = 14 )          #Sets the string on the top of chart , with the fontsize = 14  

plt.xlabel ( ' Numbers ' , fontsize = 10 )      #sets the string on x axis , with the second keyword argument as fontsize

plt.ylabel (' Sqaure '  , fontsize = 10 )
plt.tick_params ( axis = 'both' , labelsize  = 14 )     
''' 
the tick_params is the function inside matlplotlib.pyplot , here it has two keyword argument  axis = both 
means apply in both axises , labelsize is the numbers appearing on axis, now it is set to 14 size'''
plt.show ( )


#The scatter () method :
import matplotlib.pyplot as plt 
plt.scatter ( 2 , 4 , s = 50)       #Points the single point on graph , the scatter ( ) method takes two arguments , scatter ( x, y ) , the s  argument tells the size of dot
plt.xlabel ( 'Numbers' , fontsize = 10  )
plt.ylabel ( 'Sqaure' , fontsize = 10 )
plt.title ( 'Sqaure Number',  fontsize = 14 )
plt.tick_params ( axis = 'both' , which = 'major' ,  labelsize = 14 )
''' the tick_params method () defines the tick, in the axis there are big (major) and small ( minor ) lines in the axis , to set we can choose ( which = 'major' etc )
and the labelsize will only to the major or minor lines or both lines present on axis of grraph'''
x_values = [  1 , 2 , 3 , 4 ,5 ,6 ]
y_values =  [ 1 , 4 , 9 , 16 , 25 ,36 ]
plt.scatter ( x_values  , y_values  ,  s = 40 )
'''
    the plt.scatter ( ) function will see list  of x values accordingly to y values list number , x_values[0]  to y_values [ 0 ] '''

plt.show ( )


#Creating Data Manually
import matplotlib.pyplot as plt

x_values = list( range  ( 1 , 101 ))        #this first creates the sequence of numbers by range ( 1, 101 ) and stores in list by list method that takes one argument and store it in a variable
y_values  = [ x**2 for x in x_values  ]     #this line of code , first runs the for loop , so whatever value in x_values iteration it stored in x variable , the x variable is squared 
                                            #and the results is stored inside a list one by one and then whole list is assigened to variable.
'''
y_values = [ x**2 for x in  x_values ]
is equivalent to :
for x in x_values :
    y_values.append ( x**2 )'''

plt.scatter ( x_values , y_values , s = 20 , c = "#ff0000" , edgecolor = 'none' )
plt.axis ( [ 0 ,10 ,  0 ,  100 ] )      #The plt.axis method controls how much axis do you want in the graph plt.axis([xmin, xmax, ymin, ymax])
'''
.) xmin starting number on x - axis .) xmax :  ending number on x axis '''
plt.show()



#ColorMap :
#Darkens color for higher value , lower for lower values
import matplotlib.pyplot as plt
x_values = list( range  ( 1 , 101))        
y_values  = [ x**2 for x in x_values  ]     
plt.scatter ( x_values , y_values , s = 20 , c = y_values ,  edgecolor = 'none' , cmap =  'Reds' )     #We store y_values in color, and cmap is set to reds
plt.axis ( [ 0 ,100  ,  0 ,  10000 ] )      
plt.savefig('squares_plot.png', bbox_inches='tight')        #Saves the file in the same directory , the second argument removes extra spaces from the grpah
'''We can pass more arguments depending on our need.'''



#Excersizes
import matplotlib.pyplot as plt
plt.xlabel ( 'Numbers' , fontsize = 13 )
plt.ylabel ( 'Cubes' , fontsize = 13 )
plt.title ( 'Cubes Number', fontsize = 16 )
plt.tick_params ( axis = 'both' , which = 'major' , labelsize  = 12 )
x = list ( range (  1 , 1001 ))
y = [ x**3 for x in x ]
plt.scatter ( x , y  , s = 30 , c = 'blue' )
plt.axis ( [ 0 , 1000 , 0 , 100000] )
plt.show( )



#Random Walk 
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
    random_walk = RandomWalk ( 10 )
    random_walk.fill_walk()
    plt.title ('Random Walk' , fontsize  = 17 )
    plt.scatter ( random_walk.x , random_walk.y , s = 10 , c = 'red' )
    plt.plot( random_walk.x , random_walk.y , linewidth = 2 , c = 'black' )
    plt.show()

    prompt = input('Press Q for exit : ').title().strip()
    if prompt == 'Q' :
        break
    else :
        continue


#Ending todays coding at PAGE NUMBER : 335