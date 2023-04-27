import webbrowser
import os

from flask import Flask, send_file

app = Flask(__name__)


@app.route("Stable.mp4")
def index():
    video_path = "./videos/my_video.mp4"
    mimetype = "video/mp4"
    return send_file(video_path, mimetype=mimetype)


if __name__ == '__main__':
    # Open the menu file and read its contents
    app.run()
    os.remove("./videos/my_video.mp4")
    with open('menu.html', 'r') as file:
        menu_html = file.read()

    # Open the menu in the default web browser
    webbrowser.open_new_tab('menu.html')
