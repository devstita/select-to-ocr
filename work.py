import pytesseract
from tempfile import TemporaryDirectory
import PIL.Image as Image
from time import time

import win
import utils

def do(): 
    with TemporaryDirectory() as td:
        dest = td + f'\\capture{str(time())}.jpg'
        win.capture_with_area(dest)
        image = Image.open(dest).convert('L')
        msg = ocr(image)
        utils.copy_to_clipboard(msg)
    return msg

def ocr(image): 
    return pytesseract.image_to_string(image, lang='eng+kor')[:-1]