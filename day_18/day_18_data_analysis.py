import csv 
import matplotlib.pyplot as plt
from datetime import datetime

file_name = 'sitka_weather_2014.csv'
with open ( file_name , 'r' ) as f :
    reader = csv.reader ( f)
    header =next ( reader )

    highs , lows , dates = [ ] , [] , [] 
    for row in reader :
        try :
            high = int(row[1])
            low = int(row[3])
            date = str( row [0] )

        except ValueError :
            pass
        else :
            highs.append(high)
            lows.append(low)
            dates.append( (datetime.strptime( date , '%Y-%m-%d' )))

figure  =  plt.figure ( dpi = 128 , figsize = ( 10 , 6 ))
plt.title ( 'Daily high temperature of 2014' , fontsize = 16 )
plt.xlabel ( 'Dates' ,fontsize = 14 )
plt.ylabel ( 'Temperature (F)' ,fontsize = 14 )
plt.tick_params ( axis  = 'both' , which = 'major' , labelsize = 13 )
plt.plot ( dates,  highs , c = 'red' , linewidth = 0.5 , alpha = 0.5)
plt.plot(dates, lows, c= 'blue' ,linewidth = 0.5  , alpha = 0.5  )
plt.fill_between( dates , highs , lows ,facecolor = 'blue' , alpha = 0.2)
#fil_between method shades the areae between two y values, aplha controls the transpency of color  , by default alpha is one completely opaque
#facecolor is used for shading  / interior areas
figure.autofmt_xdate ()
plt.show ( )


#Excersizes (Karachi Weather )
import csv 
from datetime import datetime
import matplotlib.pyplot as plt
file_name = 'karachi_weather_december-2025.csv'

with open ( file_name , 'r' ) as file_object :
    reader = csv.reader( file_object )
    header = next(reader)
    for index , heading in enumerate(header) :
        print(str(index) + ' .) ' + heading)

    lows , dates ,highs =  [] , [] , [ ] 
    for row in reader :
        #The split method takes the string and seperate whenever space is countered 
        #This happens when no argument is passed , it splits the word before tab spaces new line into list of strings
        #But when argument passed such as  ' ' , 'e'  it treates to split those characters
        date  = row[0].split()
        try :
            low = float(row[2])
            high = float(row[3])

        except ValueError :
            print(date[0], 'is missing.')
        
        else :
            lows.append(low)
            dates.append( datetime.strptime( date[0] , '%Y-%m-%d' ))
            highs.append(high)

figure  = plt.figure ( dpi = 100 ,  figsize = (12,8))
plt.xlabel( ' ' , fontsize = 12)
plt.ylabel( 'Temperature (C)',  fontsize = 12)
plt.title  ( 'Temeperature in Karachi , December 2025',  fontsize = 16)
plt.tick_params ( axis = 'both' , which = 'major' , labelsize  = 10 )
plt.plot( dates , lows ,  linewidth = 1 , c = 'blue' , label = 'Low Temperature' ,  alpha = 0.5)
plt.plot( dates , highs ,  linewidth = 1 , c = 'red'  , label = 'High Temperature' ,alpha = 0.5 )
figure.autofmt_xdate()
# plt.axis([datetime(2025,12,1), datetime(2025,12,31),15 , 18])
plt.legend(loc = 'best')            #Loc defines where to put the label
figure.set_size_inches(12, 8)
plt.fill_between( dates , highs , lows, facecolor = 'blue' , alpha = 0.1 )
plt.savefig( 'Karachi_Weather_graph.png' , dpi = 400 ,  bbox_inches = 'tight' )
plt.savefig( 'Karachi_Weather_graph.svg' ,  bbox_inches = 'tight' )
figure.set_size_inches(7,4)
plt.show()


#Excersize ( Karachi vs lahore weather )
import csv 
from datetime import datetime
import matplotlib.pyplot as plt
file_name = 'karachi_weather_december-2025.csv'
file_name_2 = 'lahore_weather_december-2025.csv'

with open ( file_name , 'r' ) as file_object :
    reader = csv.reader( file_object )
    header = next(reader)
    # for index , heading in enumerate(header) :
    #     print(str(index) + ' .) ' + heading)
    averages = [ ] 
    dates = [ ]
    for row in reader :
        date = row[0].split()
        try :
            average = float ( row[1] )
        except ValueError :
            print(date[0] , ' is not present.')
        else :
            dates.append(datetime.strptime( date[0] , '%Y-%m-%d' ))
            averages.append(average)

with open ( file_name_2 , 'r' ) as file_object :
    reader_1 = csv.reader( file_object )
    header_1 = next(reader_1)
    averages_1 = [ ] 
    dates_1= [ ]
    for row in reader_1 :
        date_1 = row[0].split()
        try :
            average_1 = float ( row[1] )
        except ValueError :
            print(date_1[0] , ' is not present.')
        else :
            dates_1.append(datetime.strptime( date_1[0] , '%Y-%m-%d' ))
            averages_1.append(average_1)

figure  = plt.figure ( dpi = 100 ,  figsize = (12,8))
plt.xlabel( ' ' , fontsize = 12)
plt.ylabel( 'Temperature (C)',  fontsize = 12)
plt.title  ( 'Temeperature in Karachi and Lahore , December 2025',  fontsize = 16)
plt.tick_params ( axis = 'both' , which = 'major' , labelsize  = 10 )
plt.plot( dates , averages , c = 'red' , linewidth = 1 , label = 'Karachi' )
plt.plot( dates_1 , averages_1 , c = 'blue' , linewidth = 1 , label = 'Lahore' )
figure.autofmt_xdate()
# plt.axis([datetime(2025,12,1), datetime(2025,12,31),15 , 18])
plt.legend(loc = 'best', fontsize=14)            #Loc defines where to put the label
figure.set_size_inches(12, 8)
plt.savefig( 'Karachi_Lahore_graph.png' , dpi = 400 ,  bbox_inches = 'tight' )
plt.savefig( 'Karachi_Lahore_Weather_graph.svg' ,  bbox_inches = 'tight' )
figure.set_size_inches(7,4)
plt.show ()



