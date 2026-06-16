import requests
from operator import itemgetter
'''The item getter is a function that creates another function to work with later'''
url ='https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get ( url )
print(r.status_code)
submission_ids = r.json () 
submission_dicts = [ ]
for submission_id in submission_ids[ : 10 ]  :
    url = 'https://hacker-news.firebaseio.com/v0/item/'+str(submission_id)+'.json'
    submission_r = requests.get ( url)
    print(submission_r.status_code)
    response_dict = submission_r.json ( )
    submission_dict = { 'title' : response_dict['title'] , 
                            'link' : response_dict.get('url' ,  ' ') ,
                            'comments' : response_dict.get( 'descendants' , 0 )         #We use get method as safety when key is not present it returns whatever present in the second argument , if key is present it returns whatever value inside that particular key
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted (submission_dicts , key =  itemgetter('comments') , reverse = True )
# #This sorted method takes three arguments , the first argument is the list of dicts , and the second argument is the itemgetter which
# itself takes the argument as comments now key variable is a function 
# python iterates through that list of dict and for every dict it calls key function () and it reverse sorts the list based on the comments
for submission_dict in submission_dicts :
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'] )
    

