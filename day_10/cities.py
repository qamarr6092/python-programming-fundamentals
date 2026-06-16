def get_location ( city , country , population ) :
    location = city + ', '  + country + ' - Population = ' + str(population)
    return location.title().strip()