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

        count = 0

        modifier = 1.5

        #create frequency table
        word_freq = self.create_freqtable()

        #tokenize text
        sentences = sent_tokenize(self.to_sum)

        #score sentences
        values =  self.score_sentences(sentences, word_freq)

        #find threshold
        thresh =  self.find_thresh(values)

        #if sentence is above threshold * modifier add it
        for s in sentences:
            if s[:10] in values and values[s[:10]] > (modifier * thresh):
                summary += " " + s
                count += 1


        return summary
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

    def score_sentences(self, sentences, word_freq):

        scores = dict()
        #score each sentence
        for s in sentences:
            #number of words in sentence
            wc_sentence = len(word_tokenize(s))

            for v in word_freq:
                if v in s.lower():
                    if s[:10] in scores:
                        scores[s[:10]] += word_freq[v]
                    else:
                        scores[s[:10]] = word_freq[v]

            scores[s[:10]] = scores[s[:10]] // wc_sentence

        return scores

    def find_thresh(self, values):

        #take average score for all sentences

        sum = 0
        for i in values:
            sum += values[i]

        average = int(sum/len(values))


        return average



    