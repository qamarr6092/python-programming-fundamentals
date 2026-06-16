import pygal
from pygal_maps_world.i18n import COUNTRIES 
def get_country_code ( country_name ) :
    for code , name in COUNTRIES.items() :
        if name == country_name :           #data in left , looking for in right
            return code
    return None

