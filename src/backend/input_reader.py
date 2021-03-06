from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import sys
import os

"""
This file will contain the class reader. This takes a filename as input and converts the .pdf to text.
"""


class reader():

    #constructor
    def __init__(self, filename):
        
        #input file
        self.input_file = filename
   

    def analyze(self):
        #return text of the pdf

        #convert pdf into image for each page
        pgs = convert_from_path(self.input_file, 500)

        result_text = ""

        #for all pages
        for x in pgs:

            #append proccessed text to final text 
            result_text += pytesseract.image_to_string(x)

        return result_text