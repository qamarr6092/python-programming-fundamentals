import requests         #Python Library that allows to talk to interent
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'         
#The first part, https://api.github.com/, directs the request to the part of GitHub’s website that responds to API calls. 
# The next part, search/repositories, tells the API to conduct a search through all repositories on GitHub.
# '?' represents passing arguments start
# q=language:python&sort=stars' q stands for query so here we find python projects sorted in number of stars 

r = requests.get(url)           
# 1. Sends an HTTP GET request to the specified URL.
# 2. The 'requests' library handles the connection and data retrieval.
# 3. Returns a 'Response' object (assigned to 'r') containing the server's data and metadata.
print('Status code : ' , r.status_code )        #200 indicates successful response

response_dict = r.json()        #The api returns the information in the json format , converted json format in python dictionary
print(response_dict.keys() )

# qamar = { 'qamar' : 'jawaid' , 'class' : 'second year' }
# print(qamar.keys() )        #this will print with dict_keys class with tuples of list
# print(qamar.items())        #this will print the items with tuples of lsit
# print(qamar )               #this will print as it is
# print(qamar['qamar'])       #this will print the value

print('Total Repostries : ' ,  response_dict['total_count'])        #Total repostories present on github from python language
repo_dicts = response_dict['items']         #The value assosicated with items has the list of dicts storing info of those repostries returned
print('Repositories Returned : ' , len(repo_dicts))                 #Total repostories information from the api call
repo_dict = repo_dicts[0]
print('keys : ' , len ( repo_dict ))
for key in sorted( repo_dict.keys()) :
    print( key )