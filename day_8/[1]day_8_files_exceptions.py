#Day_8_Files_And_Exception:
#Chapter_8

with open('pi_digit.txt') as file_object :  #opens the file and stores as object in file_object, the with keyword closes the file when necesary
    contents = file_object.read()           #read the entire file and stores in contents as string
    print(contents)                #print whatever stores in contents and removes whtiespaces from right side

#File Path
with open('text_files/text_file_1.txt') as file_object :    #The text file is stored in the sub-directory
    contents = file_object.read()           
    print(contents)                

#Absolute File Path :
file_path = 'C:/Users/hp/Documents/test_file.txt'   #Can accept both slashes, if '\' use two slashess to differ from escape sequence'\n'
with open(file_path) as file_object :   #file_object has now information of txtfile , where the file is  , current position but not what it is writte
    contents = file_object.read()       #this stores 'content' whatever is written    
    print(contents) 

file_path = 'pi_digit.txt'
with open (file_path) as file_object :
    for line in file_object :
        print(line.rstrip())                    #also prints the extra line , using.rstrip()

#The object returned by open ( ) is only available inside the with block:
#You can store file lines inside the list and use outside the with block
file_path = 'pi_digit.txt'
with open(file_path) as file :
    lines = file.readlines()    #This stores the line by line into a list , the variable here 'lines' holds that list
print(lines)
for line in lines :
    print(line.rstrip())

file_path = 'pi_digit.txt'
with open(file_path) as file :
    lines = file.readlines( )
pi_string = ''
for line in lines :
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

file_path ='pi_digit_1.txt'
with open (file_path) as file_object :
    lines = file_object.readlines ( )
pi_string = ''
for line in lines :
    pi_string += line.strip()
print(len(pi_string))
print(pi_string[0:10],'......')


#Ending today's coding at page number 196