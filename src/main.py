
import input_reader
import text_speech



def main():

    #create reader object
    reader = input_reader.reader("/home/jacob/Projects/Text_Reader/src/test.pdf")

    #convert to text and create speaker object
    speaker = text_speech.speaker(reader.analyze())

    #play the output
    speaker.speak()





if __name__ == '__main__':
    main()