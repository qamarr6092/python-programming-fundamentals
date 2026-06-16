import pygal

#Creating an instance from the World() class, it has optional arguments
wm = pygal.maps.world.World()

#calling methods from those instance created from World() class.
wm.title = 'North, Central, and South America'
wm.add('North America' , [ 'ca' ,'mx' ,'us' ])
#the add method takes a label can be any string, and a list of country codes to work on those labels.
#each add method adds the new color and  and label on the left side of graph with that color
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file ('americas.svg')


#population of north america
import pygal
wm = pygal.maps.world.World()
#to set the values in the map the add() method  usees the dict instead of list, and python automatically shades the countries based on least values
wm.add  ( 'North America' , { 'ca' : 1400000 , 'us' : 340000000 })
wm.render_to_file ( 'america_population.svg')