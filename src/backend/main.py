
import input_reader
import text_speech
import summarizer

'''
Main function for Text_Reader. This controls the flow of the program before the frontend is built
'''

def main():

    #TODO add command line arguements

    #create reader object
    reader = input_reader.reader("/home/jacob/Projects/Text_Reader/src/test.pdf")

    text_pdf = reader.analyze()

    #convert to text and create speaker object
    speaker = text_speech.speaker(text_pdf)

    #play the output
    speaker.speak()

    #summarize the text into a condences version

    #create condencer object
    condencer = summarizer.condencer(text_pdf)

    #call to summarize the text.
    summed_text = condencer.summarize()

    
    print(summed_text)





if __name__ == '__main__':
    main()