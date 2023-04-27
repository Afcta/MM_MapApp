import webbrowser
import os

if __name__ == '__main__':
    # Open the menu file and read its contents
    with open('menu.html', 'r') as file:
        menu_html = file.read()

    # Open the menu in the default web browser
    webbrowser.open_new_tab('menu.html')



