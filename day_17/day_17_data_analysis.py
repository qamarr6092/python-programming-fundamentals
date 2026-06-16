#Day_17_Data_Analysis :

#CSV :
'''Series of values , seperated by commas , (CsV , Comma seperated values ), the csv has values seperated by commas in plain text.'''
#Python csv module parses the csv
import csv
import matplotlib.pyplot as plt
from datetime import datetime           #Converts datetime string into Date objects

file_name = 'sitka_weather_07-2014.csv'
with open ( file_name , 'r' ) as file_obj :

    reader = csv.reader(file_obj)
    # The csv is the module and reader is the method that has taken file_instance as an argument, it returns not the value but the  instance of csv file
    #the reader 'variable' holds that instances , an instance has pointers , location etc..
    #file_obj holds the properties of csv file, and reader holds the properties of information inside it. 
    #In Python, an iterator is an object that acts like a "one-way conveyor belt." It allows you to process a large collection of data one item at a time without loading the entire thing into your computer's memory.
    # Think of it like a bookmark:
    # It doesn't contain the whole story in its memory.
    # It just knows exactly where you are and how to get to the next page.
    #How the reader acts as an Iterator
    #When you create reader = csv.reader(f), Python creates that "conveyor belt."
    #Memory Efficient: If your weather file had 10 million rows, a standard list would crash your computer. An iterator (the reader) only holds one row in memory at any given second.
    #The next() Trigger: Every time you call next(reader), the conveyor belt moves forward by one. It "consumes" that row and hands it to you as a list.
    #One-Way Trip: Once the iterator moves past a row, you can't go backward. To see the first row again, you’d have to "reset" by opening the file again.

    header = next(reader) 
    #The next () is a global method so it does not need the '.' , just like len () does not need the dot
    #the next() methdod takes an iterator and reads the next line,
    #After the next () method is called, now the instance is pointing to the next line , it updated the postion , reader is the instance + iterator
    #in text_files, file_obj.readlines() returns list, json.load() returns whatever stored in the file_obj either dict or lsit
    #but with the  csv file it is different
    print(header)

    for index , column in enumerate ( header [ : 5 ] ) :        
        #The enumerate will work on lists and also stores the indexes which starts from zero, to print first five we use slice method [ : 5 ]
        #Syntax : list[ start : stop : step ] , default values list [ 0 : end : 1 ]
        print(str(index)  +' .) ' + column)

    '''next_line = next(reader)
    print(next_line)
    #'From this we can say that in every row second column is the max_temperature'
'''
    high_temp = [ ] 
    for row in reader :
        #The instance holds the attributes and also the iterator protocol / rule book, so we can iterate over the reader instance 
        # File Instance: Iterates line by line (strings).
        # CSV Reader Instance: Iterates line by line (parsed lists).
    
        high_temp.append(int(row[1]))      #python returns whole line as string so  65 is actually '65' , so we will convert it to the integer

print(high_temp)

#Plotting the temperature data without the dates known yet.

plt.title('Temperature' , fontsize = 15 )
plt.xlabel(' ' , fontsize =12 )
plt.ylabel('Fahrenheit' , fontsize = 12 )
plt.plot( high_temp , linewidth = 2 , c= 'red' )
plt.tick_params ( axis = 'both' , which = 'major' , labelsize = 12 )
fig = plt.figure ( dpi = 150 ,  figsize = ( 12 , 6 ) )
print(type(fig))    #Not all instances are iterator
plt.show()



import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_name = 'sitka_weather_2014.csv'
with open ( file_name , 'r' ) as file_obj :
    reader = csv.reader( file_obj )
    first_line = next(reader)

    high_temp , dates = [] , [] 
    for row  in reader :
        try :
            temp = int(row[1])

        except ValueError :
            pass

        else :
            high_temp.append(temp)
            date = datetime.strptime( row[0] , '%Y-%m-%d')
            dates.append(date)

fig = plt.figure ( dpi = 128 ,  figsize = ( 10 , 6 ) )
plt.title('Temperature of  2014 ' , fontsize = 15 )
plt.xlabel('Date ' , fontsize =12 )
plt.ylabel('Fahrenheit' , fontsize = 12 )
plt.plot( dates , high_temp , linewidth = 0.5 , c= 'red' )
plt.tick_params ( axis = 'both' , which = 'major' , labelsize = 12 )
print(type(fig))    #Not all instances are iterator
fig.autofmt_xdate()         #Prevents the date from overlapping

plt.show()
