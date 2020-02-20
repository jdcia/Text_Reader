
import input_reader
import text_speech
import summarizer
import argparse

'''
Main function for Text_Reader. This controls the flow of the program before the frontend is built
'''

def main():

    #create parser object
    parser = argparse.ArgumentParser()
    
    #parser arguments
    parser.add_argument("-p", "--play", help="This arg will play the mp3 after creation", action="store_true")
    parser.add_argument("-t", "--text", help="This arg will print the text from the pdf", action="store_true")
    parser.add_argument("-s", "--sum", help="This arg will print the summary of the pdf", action="store_true")
    
    #get arguements
    args = parser.parse_args()

    #create reader object
    reader = input_reader.reader("./test.pdf")

    #get text from the pdf
    text_pdf = reader.analyze()

    if args.text == True:
        print("Text from PDF:")
        print(text_pdf)

    #convert to text and create speaker object
    speaker = text_speech.speaker(text_pdf)

    #play the output
    if args.sum == True:
        speaker.speak()

    #summarize the text into a condences version

    #create condencer object
    condencer = summarizer.condencer(text_pdf)

    #call to summarize the text.
    summed_text = condencer.summarize()

    if args.sum == True:
        print("Summarized Text:")
        print(summed_text)


if __name__ == '__main__':
    main()