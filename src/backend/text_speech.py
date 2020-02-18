from gtts import gTTS
import os

'''
Contains Speaker class which converts text to speach. 
'''


class speaker():

    #contructor
    def __init__(self, text):
        self.to_read = text

    def speak(self):

        #move this to command line option or gui.
        language = 'en'

        #convert text using gTTS
        voice = gTTS(text = self.to_read, lang = language, slow=False)
        
        #play the mp3

        #create the mp3 file
        voice.save("temp.mp3")

        #eventually write mp3 player so that it is built in.
        os.system("mpg321 temp.mp3")