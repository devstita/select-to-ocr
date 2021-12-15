import pystray
from pystray import MenuItem, Menu
from PIL import Image

def exit_tray(): 
    icon.stop()

image = Image.open('download.jpg')
menu = (MenuItem('Exit', exit_tray), )
icon = pystray.Icon('name', image, 'title', menu)
icon.run()

print('nunu')
