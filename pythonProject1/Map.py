import os

import folium
from folium import IFrame
from folium.plugins import Draw
from flask import render_template
#
class Map:

    m = folium.Map(location=[51.760687810375956, 19.458312506837643], zoom_start=12)


    m = folium.Map(location=[51.760687810375956, 19.458312506837643], zoom_start=12)



    video_url = "https://www.youtube.com/embed/6JBl2Qbe2Zw"
    video_html = f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    video_iframe = IFrame(video_html, width=560, height=315)
    popup = folium.Popup(video_iframe, max_width=650)

    popup1 = folium.Popup('<a href="famousPlaces.html">Click here to view the video</a>'
                              )
    marker = folium.Marker(
            [51.76469177181548, 19.45746972538261], popup=popup1,
            tooltip="Twoja stara",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )
    marker1 = folium.Marker(
            [51.766564986894885, 19.456798138876003],
            popup=popup,
            tooltip="Mis Uszatek",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )
    marker2 = folium.Marker(
            [51.77721719686519, 19.45463642538355],
            popup="<h1>Freedom Square</h1>",
            tooltip="Freedom Square",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )

    marker3 = folium.Marker(
            [51.76792979001689, 19.456680333446094],
            popup="<h1>Rubenstein Piano</h1><img src='photos/piano.jpg' width = 400px/>",
            tooltip="Rubenstein Piano",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )

    marker4 = folium.Marker(
            [51.77287876573184, 19.455790267712022],
            popup='<h1 style="font-size:30px;">Three manufactures</h1>'
                  "<img src='photos/manufactures.jpg' width = 400px/>"
                  "<h2> Izrael Poznański</h2>"
                  '<a style="font-size:20px;" href="famousPeople.html#Izrael">video</a>'
                  '<h2 style="font-size:30px;">Karol Scheibler</h2>'
                  '<a style="font-size:20px;" href="famousPeople.html#Karol">video</a>'
                  '<h2 style="font-size:30px;">Henryk Grohman</h2>'
        ,
            tooltip="Three manufactures",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )

    marker5 = folium.Marker([51.778906051771884, 19.451293974304274],
                            popup="<h1>Poznanski Palace</h1>"
                                  '<a style="font-size:20px;" href="famousPlaces.html#PoznanskiPalace"">video</a>',
                            tooltip="Poznanski Palace",
                            icon=folium.Icon(icon="heart", icon_color="pink")
                            )

    marker.add_to(m)
    marker1.add_to(m)
    marker2.add_to(m)
    marker3.add_to(m)
    marker4.add_to(m)
    marker5.add_to(m)

    map_file = os.path.abspath('map.html')
    print(map_file)

    m.save('map.html')





