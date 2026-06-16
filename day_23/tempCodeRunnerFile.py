import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS , LightenStyle as LS  , DarkenStyle as DS
languages = [ 'java' , 'python' , 'c' , 'cpp' #for c++
             , 'javascript' ]
repo_dicts =  [ ]
for language in languages :
    url = 'https://api.github.com/search/repositories?q=language:'+str(language)
    response = requests.get(url)
    print(response.status_code )
    response_dict = response.json( )
    repo_num = int(response_dict.get('total_count' , None))
    if language == 'cpp' :
        repo_dict = {
            'language' : 'c++' , 'num_of_repos' : repo_num
         }
    else :
        repo_dict = { 
            'language' : language , 'num_of_repos' : repo_num
        }
    repo_dicts.append( repo_dict )

repo_dicts =  sorted ( repo_dicts , key = itemgetter ('num_of_repos') , reverse = True) 
plot_dicts = [ ]
for repos in repo_dicts :
    plot_dict = { 'value' : repos['num_of_repos'] , 
                 'label' : 'Number of repostories : '+ repos['language'].title()}
    plot_dicts.append( plot_dict)


my_style = DS ( "#24A0B6" , base_style = LCS )
my_style.title_font_size = 24
my_style.label_font_size = 16
my_style.major_label_font_size = 18
my_config = pygal.Config ( )
my_config.show_y_guides =False
my_config.show_legend = False
# my_config.x_label_rotation = 45
my_config.width = 1000
my_config.height = 600
my_style.tooltip_font_size = 14
chart =pygal.Bar ( my_config , style = my_style )
# chart.y_labels = 'Number of repostories' 
chart.title = 'Most repostories in github'
chart.x_labels  = [ (d['language']).title() for d in repo_dicts ]
chart.add ( '' , plot_dicts )
chart.render_to_file ( 'github_repos.svg')

