# import the library
import pandas as pd
import folium
import matplotlib.pyplot as plt

m = folium.Map([41.8781, -87.6298], zoom_start=11)
m

df = pd.read_csv("data_week64.csv")
# mark each station as a point
for index, row in df.iterrows():
    folium.CircleMarker([row['lat'], row['lon']],
                        radius=row['value'],
                        fill_color="#3db7e4", # divvy color
                       ).add_to(m)

# convert to (n, 2) nd-array format for heatmap
df1 = df[['lat', 'lon']].as_matrix()

# plot heatmap
from folium import plugins
from folium.plugins import HeatMap
m.add_child(plugins.HeatMap(df1, radius=15))
m