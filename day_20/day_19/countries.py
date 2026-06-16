#The pygal is the library
#the pygal_mapps is the seperate library to make it faster but pygal holds the tools while pygal_maps hold the data
#the i18n module has dicitionary inside, that has two letter country_code inside it as COUNTRIES which as dictionary
#The capitalized are known as constants in pyton

import pygal
from pygal_maps_world.i18n import  COUNTRIES 

for code, country in sorted(COUNTRIES.items() ) :
    print(code ,country)

print(COUNTRIES)