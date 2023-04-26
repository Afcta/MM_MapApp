import folium
from folium import IFrame
from folium.plugins import Draw


class Map:
    def __init__(self):
        self.m = folium.Map(location=[51.760687810375956, 19.458312506837643], zoom_start=12)

    def add_markers(self):
        self.m = folium.Map(location=[51.760687810375956, 19.458312506837643], zoom_start=12)

        marker = folium.Marker(
            [51.76469177181548, 19.45746972538261],
            popup="<h1>Laweczka Tuwima</h1><p></p>",
            tooltip="Laweczka Tuwima",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )

        video_url = "https://www.youtube.com/embed/6JBl2Qbe2Zw"
        video_html = f'<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        video_iframe = IFrame(video_html, width=560, height=315)
        popup = folium.Popup(video_iframe, max_width=650)

        marker1 = folium.Marker(
            [51.766564986894885, 19.456798138876003],
            popup=popup,
            tooltip="Mis Uszatek",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )

        marker2 = folium.Marker(
            [51.77721719686519, 19.45463642538355],
            popup="<h1>Freedom Square</h1>",
            tooltip="Laweczka Tuwima",
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
            popup="<h1>Three manufactures</h1><img src='photos/manufactures.jpg' width = 400px/>",
            tooltip="Three manufactures",
            icon=folium.Icon(icon="heart", icon_color="pink")
        )

        marker.add_to(self.m)
        marker1.add_to(self.m)
        marker2.add_to(self.m)
        marker3.add_to(self.m)
        marker4.add_to(self.m)

    def save(self, location):
        self.m.save(location)

    # draw = Draw(export=True)
    # draw.add_to(m)
