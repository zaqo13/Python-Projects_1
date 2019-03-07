import folium
import os
import pandas

# my_loc = folium.Map(location=[18.576798, 73.775229],width=800,height=800,zoom_start= 80, zoom_control= True)
# name=input("Enter the amee for file:- ")
# my_loc.save(name)

data=pandas.read_csv("Volcanoes_USA.csv")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elv=list(data["ELEV"])
status=list(data["STATUS"])
# print(elv)
# print(lat,lon)


# map=folium.Map(location=[30,-99.09], zoom_start=6, tiles="Mapbox Bright")     # map & map2 are differ by tiles
map2=folium.Map(location=[35.92,-115.234], zoom_start=6, tiles="Mapbox Control Room")

def color_chart(elevation):
    if elevation < 1000:
        return "green"
    elif 2000> elevation > 1000 :
        return "blue"
    else:
        return "red"

fg=folium.FeatureGroup(name="Volcano:- Marker")

fgh=folium.FeatureGroup(name="Volcano:- CircleMarker", control=True )           # overlay=False
for lt,ln,el,na,st in zip(lat,lon,elv,name,status):
    fg.add_child(folium.Marker(location=[lt,ln],popup="Elv:- %s m\nStatus:- %s" %(el,st), tooltip=" %s"%na, icon=folium.Icon(color= color_chart(el))))
    fgh.add_child(folium.CircleMarker(location=[lt,ln],popup=str(el)+"m"+", Status:- %s"%st,tooltip="%s"%na,radius=6,fill_color=color_chart(el), fill_opacity=0.6 ))


map2.add_child(fg)
map2.add_child(fgh)
map2.add_child(folium.LayerControl())
# map.add_child(fg)
# map.add_child(fgh)
# map.add_child(folium.LayerControl())

map2.save("map_S_12.html")
# map.save("map1212.html")



## map = folium.Map(location=[45.523, -122.675],tiles='Mapbox Control Room')
## name=input("Enter the name for file:- ")

## map.add_child(folium.Marker(location=[18.576493, 73.775551],popup="2nd room", icon=folium.Icon(color="red")))
## map.add_child(folium.Marker(location=[18.647573,73.762271], popup="1st room", icon=folium.Icon(color="green")))


## map.save("name of base map.html")
## print(dir(folium.Map))
