import folium

map = folium.Map(location=[-36.967355, 174.918153], tiles="OpenStreetMap", zoom_start=16)

fg = folium.FeatureGroup(name="BCP_map")

fg.add_child(folium.Marker(location=[-36.967355, 174.918153], popup="Ormiston Senior College", icon=folium.Icon(color='red')))

photo_locations = [[-36.964575, 174.908148],[-36.965038, 174.908091],[-36.965219, 174.907938],[-36.966422, 174.911517],[-36.966144, 174.908414],[]]

descriptions = ['Bacteria', 'Bacteria', 'Trolley', 'General litter','Masks']

for i, j in zip(photo_locations, descriptions):
    fg.add_child(folium.CircleMarker(radius=10, opacity=0.7, location= i, popup= j, color='red', fill_color='red'))


map.add_child(fg)
map.save('Barry Curtis Park Litter.html')