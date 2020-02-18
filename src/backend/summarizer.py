from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

'''
This call will use nltk library reference for start
 https://becominghuman.ai/text-summarization-in-5-steps-using-nltk-65b21e352b65
'''


'''
This class will take in text from a pdf and summarize it to a condenced form.
'''
class condencer():

    def __init__(self, text):
        self.to_sum = text

    def summarize(self):

        #Summarize the text and return the final summarized text.

        summary = ""

        word_freq = create_freqtable()

        sentences = sent_tokenize(self.to_sum)



        return 
    def create_freqtable(self):
        

        #declare dictionary
        table = dict()

        #create stopwords from library
        stop_words = set(stopwords.words("english"))

        #tokenize words
        words = word_tokenize(self.to_sum)

        ps = PorterStemmer()


        #for each word of the file
        for w in words:
            
            w = ps.stem(w)

            if w in stop_words:
                continue
            if w in table:
                table[w] += 1
            else:
                table[w] = 1

        return table

    def score_sentences(self):

        scores = dict()



        return scores

    