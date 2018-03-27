import folium
map = folium.Map(location = [40.00, -100.06],zoom_start=6, tiles="mapbox bright")
map.add_child(folium.Marker(location = [40.00, -100.06], popup = "I am the One", icon=folium.Icon(color='red')))
map.add_child(folium.CircleMarker(location = [40.1, -101.0], popup = "I am number 2", fill_color='green',color="green"))
map.save("webmap.html")
