
import input_reader
import text_speech

'''
Main function for Text_Reader. This controls the flow of the program before the frontend is built
'''

def main():

    #create reader object
    reader = input_reader.reader("/home/jacob/Projects/Text_Reader/src/test.pdf")

    #convert to text and create speaker object
    speaker = text_speech.speaker(reader.analyze())

    #play the output
    speaker.speak()





if __name__ == '__main__':
    main()