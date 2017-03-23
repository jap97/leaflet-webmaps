import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt" )


map = folium.Map(location = [45.372, -121.00] , zoom_start = 6 , tiles ='Mapbox Bright')

def color(elev):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - min(df['ELEV'])/3))
    if elev in range(minimum,minimum+step):
        color = 'green'
    elif elev in range(minimum+step , minimum+step*2):
        color = 'orange'
    else:
        color = 'red'
    return color
fg = folium.FeatureGroup(name = 'volcanoes location')
for lat,lon,n,elev in zip(df['LAT'] , df['LON'] , df['NAME'] , df['ELEV']):
    fg.add_child(folium.Marker(location = [lat, lon],popup = n, icon = folium.Icon(color = color(elev))))
map.add_child(fg)

map.add_child(folium.GeoJson(data = open('World_population.json') , name= 'World Population ', style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005']<= 10000000 else 'orange' if 10000000 < x['properties']['POP2005']< 20000000 else 'red'}))
map.add_child(folium.LayerControl())
map.save(outfile = "test2.html")
