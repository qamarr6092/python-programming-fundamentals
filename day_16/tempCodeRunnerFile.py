
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
