from tempfile import TemporaryDirectory
import PIL.Image as Image
from time import time
from threading import Thread

import win
import utils
import work

if __name__ == '__main__':
    with TemporaryDirectory() as td:
        dest = td + f'\\capture{str(time())}.jpg'
        win.capture_with_area(dest)
        image = Image.open(dest).convert('L')
        Thread(target=lambda: image.show(), daemon=True).start()
        msg = work.ocr(image)
        utils.copy_to_clipboard(msg)
        print('Extracted: ', msg)
