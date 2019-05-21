try:  
    from PIL import Image
except ImportError:  
    import Image
import pytesseract

def ocr_core(filename):  
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text

for i in range(1,30):
    if i < 10:
        print(ocr_core('mess/mess-0'+str(i)+'.jpg'))
    elif i >= 10:
        print(ocr_core('mess/mess-'+str(i)+'.jpg'))
