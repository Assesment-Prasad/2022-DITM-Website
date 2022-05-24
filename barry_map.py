import folium


map = folium.Map(location=[-36.967355, 174.918153], tiles="CartoDB Positron", zoom_start=20)

fg = folium.FeatureGroup(name="BCP_map")
fg.add_child(folium.Marker(location=[-36.967355, 174.918153], popup="Ormiston Senior College", icon=folium.Icon(color='red')))


map.add_child(fg)
map.save('test_map.html')