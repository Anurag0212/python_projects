import folium
#Creating a map object with location information and tiles type as mapbox
map = folium.Map(location = [40.00, -100.06],zoom_start=6, tiles="mapbox bright")

#adding a child to current map object with Marker with the popup on webmap
map.add_child(folium.Marker(location = [40.00, -100.06], popup = "I am the One", icon=folium.Icon(color='red')))
<<<<<<< HEAD
map.add_child(folium.Marker(location = [40.1, -101.0], popup = "I am number 2", fill_color='green',color="green"))
=======

#adding another child with circle marker and popup
map.add_child(folium.CircleMarker(location = [40.1, -101.0], popup = "I am number 2", fill_color='green',color="green"))

#saving the map in html format so that, it can be accessed using web browser
>>>>>>> 608631418954d782ff8f29495690b20b5803f6e6
map.save("webmap.html")
