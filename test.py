import urllib.request
import string
import random
import nltk
# nltk.download('vader_lexicon')

def download_book(url):
    """
    Download the book from Gutenberg by using the url of the book
    return: a string
    """
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    return text

from nltk.sentiment.vader import SentimentIntensityAnalyzer

url_Camille = 'https://dev.gutenberg.org/files/1608/1608-0.txt'
text1 = download_book(url_Camille)
url_Tom = 'https://dev.gutenberg.org/files/74/74-0.txt'
text2 = download_book(url_Tom)

score1 = SentimentIntensityAnalyzer().polarity_scores(text1)
score2 = SentimentIntensityAnalyzer().polarity_scores(text2)

print(score1)
print(score2)

