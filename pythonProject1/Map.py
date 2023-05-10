import os

import folium
from folium import IFrame
from folium import plugins
from folium.plugins import Draw
from flask import render_template
#
class Map:

    m = folium.Map(location=[51.760687810375956, 19.458312506837643], zoom_start=16)


    fg_restaurants = folium.FeatureGroup(name='Restaurants')
    fg_monuments = folium.FeatureGroup(name='Monuments')

    js_function = """
        function toggleTheme() {
            var body = document.getElementsByTagName('body')[0];
            var mapDiv = document.getElementsByClassName('folium-map')[0];
            if (body.classList.contains('dark-theme')) {
                body.classList.remove('dark-theme');
                mapDiv.style.filter = 'none';
            } else {
                body.classList.add('dark-theme');
                mapDiv.style.filter = 'invert(100%) hue-rotate(180deg)';
            }
        }
    """
    top_bar_html = """
        <div class="top-bar">
            <div class="toggle-theme-button" onclick="toggleTheme()"><i class="fas fa-adjust"></i></div>
            <div class="title">Explore Lodz</div>
        </div>
    <style>
    .title{
        font-size:3.5rem;
        font-weight:bold;
        text-align: center;
        position: top;
        flex-grow: 1;
        color: white;
    }
    .top-bar{
        display: flex;
        align-items: center;
        background-color: #333;
    }
    .toggle-theme-button{
        color: white;
        margin-left: 10px;
    }
    </style>
    """

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
                            popup='<h1>Poznanski Palace</h1>'
                                  '<a style="font-size:20px;" href="famousPlaces.html#PoznanskiPalace" onclick="highlightVideoContainer(\'famousPlaces.html\', \'PoznanskiPalace\')">video</a>',
                            tooltip="Poznanski Palace",
                            icon=folium.Icon(icon="heart", icon_color="pink")
                            )

    marker6 = folium.Marker([51.77933314100332, 19.444952116435194],
                            popup="<h1>Manufacture</h1>"
                                 "<img src='photos/manufaktura.jpg' width = 400px/>"
                                  '<a style="font-size:20px;" href="famousPlaces.html#PoznanskiFactory" '
                                  'onclick="highlightVideoContainer()">video</a>',

                            tooltip="Manufacture",
                            icon=folium.Icon(icon="heart", icon_color="pink")
                            )

    marker7 = folium.Marker([51.75942655450387, 19.457584362659563],
                            popup="<h1>Unicorn Stable</h1>"
                                 "<img src='photos/UnicornStable.jpg' width = 400px/>"
                                  '<a style="font-size:20px;" href="famousPlaces.html#PoznanskiFactory" ',

                            tooltip="Unicorn Stable",
                            icon=folium.Icon(icon="heart", icon_color="pink")
                            )

    marker.add_to(fg_monuments)
    marker1.add_to(fg_monuments)
    marker2.add_to(fg_monuments)
    marker3.add_to(fg_monuments)
    marker4.add_to(fg_monuments)
    marker5.add_to(fg_monuments)
    marker6.add_to(fg_monuments)
    marker7.add_to(fg_monuments)



    #Restaurants
    rest_rating = 4.6
    rating_icon = 'fa-star'
    popup_html = f'<h4>Otwarte drzwi</h4><p>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    marker = folium.Marker([51.76301779499515, 19.458066994697752], popup=popup_html, icon = folium.Icon(color='green'))
    marker.add_to(fg_restaurants)

    rest_rating = 3.8
    popup_html = f'<h4>Chlopska Izba</h4><p>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    marker2 = folium.Marker(location=[51.76876938105906, 19.456353925382906], popup=popup_html, icon = folium.Icon(color='green'))
    marker2.add_to(fg_restaurants)

    rest_rating = 4.5
    popup_html = f'<h4>Galicja</h4><p>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    marker3 = folium.Marker(location=[51.77928756113294, 19.449665533826533], popup=popup_html, icon = folium.Icon(color='green'))
    marker3.add_to(fg_restaurants)






    fg_restaurants.add_to(m)
    fg_monuments.add_to(m)
    folium.LayerControl().add_to(m)

    # Add the top bar to the map
    m.get_root().html.add_child(folium.Element(top_bar_html))

    # Add the JavaScript function to the HTML
    m.get_root().script.add_child(folium.Element(js_function))

    m.save('map.html')





