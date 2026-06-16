import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_name = 'world_gdp.csv'
with open ( file_name  , 'r' , encoding='utf-8-sig') as file_object :       #encoding removes ï»¿ utf that is sometimes hidden in files
    data = csv.reader( file_object)
    years = next(data)
    years = years[4:-1  ]
    pakistan = [ ]
    for row in data : 
        if row [0] == 'Pakistan' :
            pakistan.extend((row[4:-1]))        #when i did slicing the list , it creates another list of those items so when i append that to pakistan list, it will be two lists one list inside another
                                                #extend can fix that too or pakistan = row(4:)
for index , gdp in enumerate(pakistan ) :
    try :
        gdp  = int (float( gdp))
    except ValueError :
        pass
    else :
        pakistan[index] = gdp
print( pakistan)
print(years)
for index ,year in enumerate(years) :
    year = datetime.strptime(year , '%Y')
    years[index] = year
print(years)
for index, gdp in enumerate(pakistan):
    try:
        # Convert to float, then divide by 1 Billion
        # This turns 371,570,000,121 into 371.57
        pakistan[index] = float(gdp) / 1000000000
    except ValueError:
        pakistan[index] = 0

figure = plt.figure ( dpi = 100 , figsize = ( 12 , 8))
plt.plot( years ,  pakistan , linewidth = 1  , c ='red')
# plt.scatter ( years , pakistan , s = 10 , c= 'black' ,  edgecolor = 'none' )
plt.title ( 'Pakistan GDP' , fontsize = 16 )
plt.xlabel ('' , fontsize = 12 )
plt.ylabel ( 'Dollars (Billion)' ,fontsize = 12 )
# plt.axis( [  datetime.strptime('1960' ,'%Y') ,datetime.strptime('2030', '%Y') ,0 ,400 ])
plt.tick_params ( axis = 'both' , which = 'major' , labelsize = 12 )
figure.autofmt_xdate()
plt.savefig ( 'pakistan_gdp.png' , dpi = 460 ) 
plt.show()


#pakistan vs india vs usa vs china
import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_name = 'world_gdp.csv'
with open ( file_name  , 'r' , encoding='utf-8-sig') as file_object :       #encoding removes ï»¿ utf that is sometimes hidden in files
    data = csv.reader( file_object)
    years = next(data)
    years = years[4:-1]
    pakistan = [ ]
    for row in data : 
        if row [0] == 'Pakistan' :
            pakistan.extend((row[4:-1]))        #when i did slicing the list , it creates another list of those items so when i append that to pakistan list, it will be two lists one list inside another
                                                #extend can fix that too or pakistan = row(4:)
        if row [0] == 'India' :
            india = row[4:-1]
        
        if  row [0] == 'United States' :
            us = row [4:-1]
        if row [0] == 'China' :
            china = row [4:-1]

for index , gdp in enumerate(pakistan ) :
    try :
        gdp  = int (float( gdp))
    except ValueError :
        pass
    else :
        pakistan[index] = gdp
for index , gdp in enumerate(china) :
    try :
        gdp  = int (float( gdp))
    except ValueError :
        pass
    else :
        china[index] = gdp

for index , gdp in enumerate(us ) :
    try :
        gdp  = int (float( gdp))
    except ValueError :
        pass
    else :
        us[index] = gdp
for index , gdp in enumerate(india ) :
    try :
        gdp  = int (float( gdp))
    except ValueError :
        pass
    else :
        india[index] = gdp
for index ,year in enumerate(years) :
    year = datetime.strptime(year , '%Y')
    years[index] = year
for index, gdp in enumerate(pakistan):
    try:
        # Convert to float, then divide by 1 Billion
        # This turns 371,570,000,121 into 371.57
        pakistan[index] = float(gdp) / 1000000000
    except ValueError:
        pakistan[index] = 0
for index, gdp in enumerate(india):
    try:
        # Convert to float, then divide by 1 Billion
        # This turns 371,570,000,121 into 371.57
        india[index] = float(gdp) / 1000000000
    except ValueError:
        india[index] = 0
for index, gdp in enumerate(us):
    try:
        # Convert to float, then divide by 1 Billion
        # This turns 371,570,000,121 into 371.57
        us[index] = float(gdp) / 1000000000
    except ValueError:
        us[index] = 0

for index, gdp in enumerate(china):
    try:
        # Convert to float, then divide by 1 Billion
        # This turns 371,570,000,121 into 371.57
        china[index] = float(gdp) / 1000000000
    except ValueError:
        china[index] = 0

figure = plt.figure ( dpi = 100 , figsize = ( 12 , 8))
plt.plot( years ,  pakistan , linewidth = 1  , c ='green' , label= 'Pakistan')
plt.plot( years ,  china, linewidth = 1  , c ='orange' , label= 'China')
plt.plot( years ,  india , linewidth = 1  , c ='blue', label = 'India')
plt.plot( years ,  us , linewidth = 1  , c ='red', label = 'United States')
# plt.scatter ( years , pakistan , s = 10 , c= 'black' ,  edgecolor = 'none' )
plt.title ( 'Pakistan vs India vs US vs China GDP' , fontsize = 16 )
plt.xlabel ('' , fontsize = 14 )
plt.ylabel ( 'Dollars (Billion)' ,fontsize = 14 )
# plt.axis( [  datetime.strptime('1960' ,'%Y') ,datetime.strptime('2030', '%Y') ,0 ,400 ])
plt.tick_params ( axis = 'both' , which = 'major' , labelsize = 14 )
figure.autofmt_xdate()
plt.legend( loc = 'best' , fontsize = 15 )
plt.savefig ( 'pakistan_india_us_china_gdp.png' , dpi = 250,  bbox_inches = 'tight') 
plt.savefig ( 'pakistan_india_us_china_gdp.svg' , dpi = 250,  bbox_inches = 'tight') 
plt.show()




