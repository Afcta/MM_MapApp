import webbrowser
import os

from flask import Flask, send_file

from menu import app

app = Flask(__name__)
#
# @app.route("menu.html")
# def index():
#     return menu_html
#
# @app.route("Stable.mp4")
# def video():
#     video_path = "./videos/my_video.mp4"
#     mimetype = "video/mp4"
#     return send_file(video_path, mimetype=mimetype)

if __name__ == '__main__':
    with open('menu.html', 'r') as file:
        menu_html = file.read()

    # Open the menu in the default web browser
    webbrowser.open_new_tab('menu.html')
