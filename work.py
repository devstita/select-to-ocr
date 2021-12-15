import pytesseract

def ocr(image): 
    return pytesseract.image_to_string(image, lang='eng+kor')[:-1]