import json
file_name = 'population_data.json'
with open ( file_name , 'r' ) as file_object :
    data = json.load ( file_object)

for country in data :
    # Put the "Looking For" variable on the right, and the "Data" variable on the left.
    if country['Year'] == '2010' :
        country_name= country['Country Name' ] 
        population = int(float((country['Value'])))
        #In the data file ,  population are in string such '33113.323' we cannot directly convert this to integer, so we
        # convert the string to float first , then that float to integer after that the numbers after decimals gets removed
        print(country_name , (population))