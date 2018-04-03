import folium, pandas,re

data = pandas.read_csv('Museum_Universe.csv')
coordinates = list(data['Location 4'])
lat = []
lon = []
name_list = list(data['LEGALNAME'])
name = []
for names in name_list:
    for location in coordinates:
        if len(location.split())>1:
            lats = location.split()[1]
            lons = location.split()[2]
            lat.append(float(re.search(r'[-+]?\d+\.\d+',lats).group()))
            lon.append(float(re.search(r'[-+]?\d+\.\d+',lons).group()))
            name.append(names)


map = folium.Map(location=[29.431037, -81.580028],tiles="Mapbox Bright",zoom_start=6)

fg = folium.FeatureGroup(name="Museum Marking")
for lt,ln,n in zip(lat,lon,name):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(n),icon=folium.Icon(color='green')))

map.add_child(fg)
map.save('museum.html')
