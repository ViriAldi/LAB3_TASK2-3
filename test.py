import folium
from flask import render_template




temp = render_template('choser.html')

p = folium.Popup(html=temp, parse_html=True)

a = folium.Marker(icon=folium.CustomIcon('Qww.png', ), location=[49, 24], popup=p)

m = folium.Map()

m.add_child(a)

m.save('123.html')
