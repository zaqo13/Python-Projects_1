import os
import pandas
from geopy.geocoders import Nominatim

# print(os.listdir())
df=pandas.read_json("supermarkets.json")

df["Address"]=df["Address"]+", "+ df["City"]+", "+df["Country"]

df["Coordinates"]=df["Address"].apply(Nominatim().geocode)
df["Latitude"]=df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"]=df["Coordinates"].apply(lambda x: x.longitude if x !=None else None)
print(df)

#####
## OR for above code
#####
# for i in df["Address"]:
#     nom1=Nominatim(user_agent="sags").geocode(i)
#     print(nom1.longitude)
#     df["Latitude"]=nom1.latitude
#     df["Longitude"]=nom1.longitude
# df
