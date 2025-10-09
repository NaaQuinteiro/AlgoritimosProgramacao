from folium import Map, Marker

m = Map(location=[-22.8777752, -47.2240132], zoom_start=14)
Marker(location=[-22.8777752, -47.2240132], 
       popup="UNASP").add_to(m)
# m.save("unasp.html")
m.show_in_browser()