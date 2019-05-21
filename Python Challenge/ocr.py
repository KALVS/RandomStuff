# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
     
    return dict


def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,
#	help="path to input image to be OCR'd")
#ap.add_argument("-p", "--preprocess", type=str, default="thresh",
#	help="type of preprocessing to be done")
#args = vars(ap.parse_args())
# load the example image and convert it to grayscale
temp = ''
for i in range(1,30):
        if i < 10:
                image = cv2.imread('mess/mess-0'+ str(i) +'.jpg')
        elif i >= 10:
                image = cv2.imread('mess/mess-'+ str(i) +'.jpg')              
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
         
        # check to see if we should apply thresholding to preprocess the
        # image
#        if args["preprocess"] == "thresh":
        gray = cv2.threshold(gray, 0, 255,
        cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
         
        # make a check to see if median blurring should be done to remove
        # noise
        #if args["preprocess"] == "blur":
         #       gray = cv2.medianBlur(gray, 3)
         
        # write the grayscale image to disk as a temporary file so we can
        # apply OCR to it
        filename = "{}.png".format(os.getpid())
        cv2.imwrite(filename, gray)

        # load the image as a PIL/Pillow image, apply OCR, and then delete
        # the temporary file
        text = pytesseract.image_to_string(Image.open(filename))
        for i in range(30,len(text)):
                if text[i].isalpha():
                        temp += text[i]
        

     
print(sortFreqDict(char_frequency(temp)))

