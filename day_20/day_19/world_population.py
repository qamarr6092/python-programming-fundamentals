# import json
# from country_codes import get_country_code
# file_name = 'population_data.json'
# with open ( file_name , 'r' ) as file_object :
#     data = json.load ( file_object)

# for country in data :
#     # Put the "Looking For" variable on the right, and the "Data" variable on the left.
#     if country['Year'] == '2010' :
#         country_name= country['Country Name' ] 
#         population = int(float((country['Value'])))
#         #In the data file ,  population are in string such '33113.323' we cannot directly convert this to integer, so we
#         # convert the string to float first , then that float to integer after that the numbers after decimals gets removed
#         # print(country_name , (population))

# for country in data :
#     if country['Year'] == '2010' :
#         country_name = country['Country Name']
#         population = int(float((country['Value'])))
#         code = get_country_code( country_name )
#         if code :

#             print (code , population)
#         else :
#             print('country code not found for population,' ,  country_name)


#plotting the data on a world map
import json
import pygal
from pygal.style import RotateStyle  , LightStyle  ,DarkStyle    #To style the worldmap the module style holds the classes , rotatestyle changes the color automatically, lightstyle chnages the background color
from country_codes import get_country_code
from pygal_maps_world.i18n import COUNTRIES 
file_name = 'population_data.json'
with open ( file_name ) as f :
    data = json.load ( f)
    data_2010 =  { }
    for country in data :
        if country['Year'] == '2010' :
            code = get_country_code( country['Country Name'] )
            if code :
                data_2010 [ code ] = int(float(country['Value']))
            else :
                pass
population_1 , population_2 , population_3 , population_4= {} , {} , {} ,{}
for code , population in data_2010.items( ) :
    if population <= 10000000 :
        population_1[code] = population 
    
    elif population > 10000000 and population <= 100000000 :
        population_2[code] = population 
    
    elif  population > 100000000 and  population <= 1000000000 :
        population_3[code] = population

    elif population > 1000000000 :
        population_4[code] = population

#setting title  attribute of world class
wm_style = RotateStyle ( "#2F5F8F" , base_style = DarkStyle)       #Passing LightStyle class as a reference not as instance, now it will hold the feature of that class
wm = pygal.maps.world.World(style =wm_style)
wm.title = 'World Population in 2010'
wm.add ( ' Less than 10M' , population_1 )
wm.add ( ' 10 - 100M' , population_2 )
wm.add ( '100M - 1B' , population_3 )
wm.add ( 'Over 1B' , population_4 )
wm.render_to_file ( 'world_population.svg')