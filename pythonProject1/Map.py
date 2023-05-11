import os

import folium
from folium import IFrame
from folium import plugins
from folium.plugins import Draw
from flask import render_template


#
class Map:
    m = folium.Map(location=[51.760687810375956, 19.458312506837643], zoom_start=16)

    tile1 = folium.TileLayer('Stamen Terrain')
    tile2 = folium.TileLayer('cartodbdark_matter')

    tile1.add_to(m)
    tile2.add_to(m)

    fg_restaurants = folium.FeatureGroup(name='Restaurants')
    fg_monuments = folium.FeatureGroup(name='Monuments')

    js_function = """
        function toggleTheme() {
            var mapDiv = document.getElementsByClassName('leaflet-container')[0];
            if (mapDiv.classList.contains('dark-theme')) {
                mapDiv.classList.remove('dark-theme');
                mapDiv.style.filter = 'none';
            } else {
                mapDiv.classList.add('dark-theme');
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
        font-family: Arial;
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
    video_iframe = IFrame(video_html, width=590, height=345)
    popup = folium.Popup(video_iframe, max_width=650)

    popup1 = folium.Popup('<a href="famousPlaces.html">Click here to view the video</a>'
                          )

    marker = folium.Marker(
        [51.76469177181548, 19.45746972538261], popup=popup1,
        tooltip="Twoja stara",
        icon=folium.Icon(icon="heart", icon_color="pink")
    )
    marker.add_to(fg_monuments)

    marker1 = folium.Marker(
        [51.766564986894885, 19.456798138876003],
        popup=popup,
        tooltip="Mis Uszatek",
        icon=folium.Icon(icon="heart", icon_color="pink")
    )
    marker1.add_to(fg_monuments)

    marker2 = folium.Marker(
        [51.77721719686519, 19.45463642538355],
        popup="<h1>Freedom Square</h1>",
        tooltip="Freedom Square",
        icon=folium.Icon(icon="heart", icon_color="pink")
    )
    marker2.add_to(fg_monuments)

    marker3 = folium.Marker(
        [51.76792979001689, 19.456680333446094],
        popup="<h1>Rubenstein Piano</h1><img src='photos/piano.jpg' width = 400px/>",
        tooltip="Rubenstein Piano",
        icon=folium.Icon(icon="heart", icon_color="pink")
    )
    marker3.add_to(fg_monuments)

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
    marker4.add_to(fg_monuments)

    marker5 = folium.Marker([51.778906051771884, 19.451293974304274],
                            popup='<h1>Poznanski Palace</h1>'
                                  "<img src='photos/PoznanskiPalace.jpg' width = 400px/>"
                                  '<a style="font-size:20px;" href="famousPlaces.html#PoznanskiPalace" onclick="highlightVideoContainer(\'famousPlaces.html\', \'PoznanskiPalace\')">video</a>',
                            tooltip="Poznanski Palace",
                            icon=folium.Icon(icon="heart", icon_color="pink")
                            )
    marker5.add_to(fg_monuments)

    marker6 = folium.Marker([51.77933314100332, 19.444952116435194],
                            popup="<h1>Manufacture</h1>"
                                  "<img src='photos/manufaktura.jpg' width = 400px/>"
                                  '<a style="font-size:20px;" href="famousPlaces.html#PoznanskiFactory" '
                                  'onclick="highlightVideoContainer()">video</a>',

                            tooltip="Manufacture",
                            icon=folium.Icon(icon="heart", icon_color="pink")
                            )
    marker6.add_to(fg_monuments)

    marker7 = folium.Marker([51.75942655450387, 19.457584362659563],
                            popup="<h1>Unicorn Stable</h1>"
                                  "<img src='photos/UnicornStable.jpg' width = 400px/>",
                            tooltip="Unicorn Stable",
                            icon=folium.Icon(icon="heart", icon_color="pink")
                            )
    marker7.add_to(fg_monuments)

    videorose_url = "https://www.youtube.com/embed/LtemZkQz9gU"
    videorose_html = f'<iframe width="560" height="315" src="{videorose_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    videorose_iframe = IFrame(videorose_html, width=590, height=345)
    popuprose = folium.Popup(videorose_iframe, max_width=850)
    marker8 = folium.Marker(
        [51.775960970248164, 19.454576994698662],
        popup=popuprose,
        tooltip="Rose Passage",
        icon=folium.Icon(icon="heart", icon_color="pink")
    )
    marker8.add_to(fg_monuments)


    # Restaurants
    rest_rating = 4.6
    rating_icon = 'fa-star'
    cuisine_type = 'Italian'
    google_price_level = '$$'
    popup_html = f'<h4>Otwarte drzwi</h4><p>Type of cuisine: {cuisine_type}<br>Google price level: {google_price_level}<br>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    popup_html += f'<p><a href="https://www.instagram.com/otwartedrzwi/" target="_blank"><i class="fab fa-instagram"></i> Otwarte drzwi</a></p>'
    popup = folium.Popup(html=popup_html, max_width=500)
    marker = folium.Marker([51.76301779499515, 19.458066994697752], popup=popup,
                           icon=folium.Icon(icon="cutlery", color='green'))
    marker.add_to(fg_restaurants)

    cuisine_type = 'Polish'
    google_price_level = '$$'
    rest_rating = 3.8
    popup_html = f'<h4>Chlopska Izba</h4><p>Type of cuisine: {cuisine_type}<br>Google price level: {google_price_level}<br>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    popup_html += f'<p><a href="https://www.instagram.com/chlopska_izba/" target="_blank"><i class="fab fa-instagram"></i> Chlopska Izba</a></p>'
    popup = folium.Popup(html=popup_html, max_width=500)
    marker2 = folium.Marker(location=[51.76876938105906, 19.456353925382906], popup=popup,
                            icon=folium.Icon(icon="cutlery", color='green'))
    marker2.add_to(fg_restaurants)

    cuisine_type = 'Polish'
    google_price_level = '$$'
    rest_rating = 4.5
    popup_html = f'<h4>Galicja</h4><p>Type of cuisine: {cuisine_type}<br>Google price level: {google_price_level}<br>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    popup_html += f'<p><a href="https://www.instagram.com/galicjaldz/" target="_blank"><i class="fab fa-instagram"></i> Galicja</a></p>'
    popup = folium.Popup(html=popup_html, max_width=500)
    marker3 = folium.Marker(location=[51.77928756113294, 19.449665533826533], popup=popup,
                            icon=folium.Icon(icon="cutlery", color='green'))
    marker3.add_to(fg_restaurants)

    cuisine_type = 'Mediterranean'
    google_price_level = '$$'
    rest_rating = 4.5
    popup_html = f'<h4>DOKI</h4><p>Type of cuisine: {cuisine_type}<br>Google price level: {google_price_level}<br>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    popup_html += f'<p><a href="https://www.instagram.com/dokigastrobar/" target="_blank"><i class="fab fa-instagram"></i> DOKI</a></p>'
    popup = folium.Popup(html=popup_html, max_width=500)
    marker4 = folium.Marker(location=[51.76188505647845, 19.461487548198058], popup=popup,
                            icon=folium.Icon(icon="cutlery", color='green'))
    marker4.add_to(fg_restaurants)

    cuisine_type = 'Argentinian'
    google_price_level = '$$$'
    rest_rating = 4.8
    popup_html = f'<h4>Tango Argentino Steakhouse</h4><p>Type of cuisine: {cuisine_type}<br>Google price level: {google_price_level}<br>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    popup = folium.Popup(html=popup_html, max_width=500)
    marker4 = folium.Marker(location=[51.77028589498561, 19.460605927270585], popup=popup,
                            icon=folium.Icon(icon="cutlery", color='green'))
    marker4.add_to(fg_restaurants)

    cuisine_type = 'Chinese'
    google_price_level = '$$'
    rest_rating = 4.7
    popup_html = f'<h4>Zloty Imbir</h4><p>Type of cuisine: {cuisine_type}<br>Google price level: {google_price_level}<br>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    popup_html += f'<p><a href="https://www.instagram.com/zloty_imbir/" target="_blank"><i class="fab fa-instagram"></i> Zloty Imbir</a></p>'
    popup = folium.Popup(html=popup_html, max_width=500)
    marker5 = folium.Marker(location=[51.766699906500406, 19.46124564878098], popup=popup,
                            icon=folium.Icon(icon="cutlery", color='green'))
    marker5.add_to(fg_restaurants)

    cuisine_type = 'Creperie'
    google_price_level = '$'
    rest_rating = 4.5
    popup_html = f'<h4>Manekin</h4><p>Type of cuisine: {cuisine_type}<br>Google price level: {google_price_level}<br>Rating: '
    for i in range(5):
        if rest_rating >= i + 0.5:
            popup_html += f'<i class="fas {rating_icon}"></i>'
        else:
            popup_html += f'<i class="far {rating_icon}"></i>'
    popup_html += f' {rest_rating}</p>'
    popup_html += f'<p><a href="https://www.instagram.com/manekinlodz/" target="_blank"><i class="fab fa-instagram"></i> Manekin</a></p>'
    popup = folium.Popup(html=popup_html, max_width=500)
    marker5 = folium.Marker(location=[51.76908497809051, 19.45632981826978], popup=popup,
                            icon=folium.Icon(icon="cutlery", color='green'))
    marker5.add_to(fg_restaurants)

    fg_restaurants.add_to(m)
    fg_monuments.add_to(m)
    folium.LayerControl().add_to(m)

    # Add the top bar to the map
    m.get_root().html.add_child(folium.Element(top_bar_html))

    # Add the JavaScript function to the HTML
    m.get_root().script.add_child(folium.Element(js_function))

    m.save('map.html')
