import requests        
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'         
r = requests.get ( url )
print(r.status_code )
response_dict = r.json()
print(response_dict.keys())
repo_dicts = response_dict['items']
repo_dict = repo_dicts [ 0 ]
# print(repo_dict.keys())
# print ('Name : ' , repo_dict['name'] )
# print('Full Name : ' , repo_dict['full_name'] )
# print('Owner : ' , repo_dict ['owner'] )
# print('Owner : ' , repo_dict ['owner'] ['login'] )
# print('Description : ' , repo_dict ['description'] )
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at'])
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'])

for repo_dict in repo_dicts :
    print ('Name : ' , repo_dict['name'] )
    print('Full Name : ' , repo_dict['full_name'] )
    # print('Owner : ' , repo_dict ['owner'] )
    print('Owner : ' , repo_dict ['owner'] ['login'] )
    print('Description : ' , repo_dict ['description'] )
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'],'\n')


#Making chart of projects based on their stars
import pygal 
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS 
names , stars =  [] , [] 
for repo_dict in repo_dicts :
    names.append( repo_dict['name'].title())
    stars.append( int(repo_dict['stargazers_count']))
# my_style = LS ("#215C92"  , base_style =  LCS , title_font_size = 24  )
# chart = pygal.Bar ( style = my_style , x_label_rotation = 45 , show_legend =  False )
# chart.title ='Most starred python projects on Github' 
# chart.x_labels = names
# chart.add ( '' , stars )
# chart.render_to_file ( 'python_repos.svg') 

my_style = LS ( '#215c92' , base_style = LCS )
#Style class controls things like font color etc
my_style.title_font_size = 24               #sets the font size of title
my_style.label_font_size = 14               #sets the x axis labels , idk for now
my_style.major_label_font_size = 18
my_config = pygal.Config()
my_config.x_label_rotation  = 45            #rotates x labels
my_config.show_legend = False
#config class controls the grid lines things like rotation etc
# my_config.title_font_size = 1
# my_config.label_font_size = 14
# my_config.major_label_font_size = 18
my_config.truncate_label = 15           #removes extra words by ...
my_config.show_y_guides = False         #removes grid lines
my_config.width  = 1000                 #bar width
my_config.height =600
chart = pygal.Bar (my_config , style = my_style )
chart.title = 'Most starred python projects on Github'
chart.x_labels = names
chart.add ( '' , stars )
chart.render_to_file ('python_repos.svg' )


#Adjusting tootltips :
import pygal 
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS , DarkColorizedStyle as DS
my_style = LS ( "#BE0606" , base_style = DS )      #Chose a primary color  , the second argument base_style determines the background color
chart = pygal.Bar ( style = my_style , x_label_rotation = 45  , show_legend = False )
chart.title = 'Python Projects'
chart.x_labels = ['Fast API' , 'Django' , 'Models' ]
plot_dicts =  [ { 'value' : 93771 , 'label' : 'This is Fast API ' } ,               #Pygal understand the keys value and label automatically , value determines how tall the bar would be and string inside the label will display at the tooltips
                { 'value' : 86383 , 'label' : 'This is Django ' }
                ,{ 'value' : 77694 , 'label' : 'This is Models ' } ]
chart.add ( '' , plot_dicts )
chart.render_to_file ( 'bar_descrpitions.svg')



#Creating Better Chart
import pygal
import requests
from pygal.style import LightColorizedStyle as LCS , DarkColorizedStyle as DCS , LightenStyle as LS , DarkenStyle as DS ,RotateStyle as RS
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'         
r = requests.get ( url )
print( r.status_code)
repo_dicts = r.json()
repo_dict = repo_dicts['items']
names , my_dicts = [ ]  , [  ]
for repo in repo_dict :
    name = repo['name']
    names.append(name)
    my_dict = { 'value' : int(repo['stargazers_count']) ,
               'label' : repo ['description'] ,
                'xlink' : repo['html_url'] }
    my_dicts.append(my_dict)
my_style = DS ( '#A20F0F' , base_style =  LCS )
my_style.title_font_size = 24
my_style.tooltip_font_size = 14
# my_style.value_label_font_size = 1
# my_style.value_font_size = 1
my_style.label_font_size = 14
my_style.major_label_font_size = 16
my_config = pygal.Config ( )
my_config.show_legend = False
my_config.show_y_guides= False
my_config.x_label_rotation = 45
my_config.truncate_label = 15
my_config.width = 1000
my_config.height = 600
chart = pygal.Bar ( my_config ,  style = my_style )
chart.x_labels = names
chart.title = 'Most starred python projects on Github'
chart.add ( '' , my_dicts  )
chart.render_to_file ( 'python_repos[1].svg')



#Hacker News API
# https://hacker-news.firebaseio.com/v0/item/9884165.json
# This URL gives details for one story (ID 9884165), NOT a user's most popular post.
#It shows the information of that particular story id 

# https://hacker-news.firebaseio.com/v0/topstories.json
# this url gives the list of top stories posted by their id numbers , and they are sorted by their site algorithm like popularity , time
#not neceseraily to be sorted

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
    
    

