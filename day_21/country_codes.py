from pygal_maps_world.i18n import COUNTRIES

def get_code ( name ) :
    for code , country  in COUNTRIES.items() :
        if country == name :
            return code
    return None

