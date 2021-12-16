import pystray
from pystray import MenuItem, Menu
from PIL import Image

from work import do

def stop_tray(): 
    icon.stop()

def run(): 
    do()

if __name__ == '__main__': 
    do()
    # image = Image.open('icon.png')
    # icon = pystray.Icon('Select To OCR', image, 'STO', Menu(
    #     MenuItem('Run', run), 
    #     MenuItem('Exit', stop_tray), 
    # ))
    # icon.run()
