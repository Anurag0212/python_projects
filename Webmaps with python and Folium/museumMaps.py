import folium,re,pandas

data = pandas.read_csv('museum_data.csv')
coordinates = data['Location 4']

lat = []
lon = []
name = list(data['LEGALNAME'])

for items in coordinates:
    if len(items.split())>1:
	lats = items.split()[1]
	lons = items.split()[2]
	lat.append(re.search(r'[-+]?\d+\.\d+',lats).group())
	lon.append(re.search(r'[-+]?\d+\.\d+',lons).group())

map = folium.Map(location=[39.9605,-75.199],titles="Mapbox Bright",zoom_start=6)

fg = featureGroup(name='Museum locations')

for lt,ln,n in zip(lat,lon,name):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(n),icon=folium.icon(color='green')))

map.add_child(fg)

map.save('Museum.html')