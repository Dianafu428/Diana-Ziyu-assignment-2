import nltk
nltk.download('vader_lexicon')
import random
import string
import urllib.request

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# sentence = 'Software Design is my favorite class because learning Python is so cool!'
# score = SentimentIntensityAnalyzer().polarity_scores(sentence)
# print(score)



# input the url of Camellias
url1 = 'https://dev.gutenberg.org/files/1608/1608-0.txt'
response1 = urllib.request.urlopen(url1)
data1 = response1.read()  # a `bytes` object
text1 = data1.decode('utf-8')
def process_file(text, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}

    if skip_header:
        skip_gutenberg_header(text)

    strippables = string.punctuation + string.whitespace

    for line in text.split('/n'):
        if line.startswith('*** END OF THIS PROJECT'):
            break

        line = line.replace('-', ' ')

        for word in line.split():
            # word could be 'Sussex.'
            word = word.strip(strippables)
            word = word.lower()

            # update the dictionary
            hist[word] = hist.get(word, 0) + 1

    return hist


def skip_gutenberg_header(text):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in text:
        if line.startswith('*** START OF THIS PROJECT'):
            break

hist1 = process_file(text1, skip_header=True)
str(hist1)
score = SentimentIntensityAnalyzer().polarity_scores(hist1)
print(score)
