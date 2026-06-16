from country_codes import get_code
import pygal
from pygal.style import RotateStyle , LightColorizedStyle , LightStyle
import csv
file_name = 'world_gdp.csv'
gdp_low  , gdp_high ,  gdp_mid= { } , {} , {}
with open ( file_name ,  encoding='utf-8-sig' ) as f :
    data = csv.reader(f)
    print(next(data))
    for row in data :
        code = get_code ( row[0] )
        if row[-3] :
             val = int(float(row[-3]))
        if code and row[-3]  :
                if val <= 10000000000 :
                    gdp_low [code] = val
                elif  val <= 500000000000 :
                     gdp_mid [ code ] = val
                else :
                     gdp_high [ code ] = val
wm_style = RotateStyle ( '#36d1d6' , base_style = LightColorizedStyle )
wm =pygal.maps.world.World( style = wm_style)
wm.value_formatter = lambda x: f"${x/1_000_000_000:.1f}B"
wm.add( 'GDP <= $10B' , gdp_low )
wm.add( 'GDP <= $500B' , gdp_mid )
wm.add( 'GDP >= $500B' , gdp_high )
wm.title = 'Countries GDP in 2023'
wm.render_to_file ('world_gdp.svg' , bbox_inches = 'tight')


#Bar Chart
import pygal
import csv
from pygal.style import Style
file_name = 'world_gdp.csv'
with open ( file_name , encoding = 'utf-8-sig' ) as f :
     data = csv.reader(f)
     header = next (data)
     for row in data :
        if row [-2] :
            val = int ( float ( row [-2] ))
        if row [0] == 'India' :
            india = val
        if row [0] == 'France' :
            france = val
        if row [0] == 'United Kingdom' :
             uk = val
        if row [0] == 'Russian Federation' :
             russia = val
custom_style = Style(
    title_font_size=24,
    label_font_size=18,      # For X and Y axis labels
    major_label_font_size=20,
    legend_font_size=16
)
hist = pygal.Bar (style = custom_style) 
hist.value_formatter = lambda x: f"${x / 1_000_000_000:,.1f}B"
hist.title = 'Countries GDP in 2024'
hist.add('GDP' , [france , uk , india, russia ] )
hist.x_labels = [ 'France' , 'India' , 'UK' , 'Russia' ]
hist.render_to_file ('countries_gdp.svg')
