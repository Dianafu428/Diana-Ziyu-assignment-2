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

# print(score1)
# print(score2)

def sentiment_analysis(d):
    '''
    Takes in an argument: d: a dictionary that contains pos, neg, neu, and compound scores 
    Prints the sentiment analysis result
    '''
    print("Overall sentiment dictionary is : ", d) 
    print("sentence was rated as ", d['neg']*100, "% Negative") 
    print("sentence was rated as ", d['neu']*100, "% Neutral") 
    print("sentence was rated as ", d['pos']*100, "% Positive") 

    print("Sentence Overall Rated As", end = " ") 
    
    # decide overall sentiment as positive, negative and neutral by using the value of compound
    if d['compound'] >= 0.05 : 
        print("Positive") 
    
    elif d['compound'] <= - 0.05 : 
        print("Negative") 
    
    else : 
        print("Neutral")

sentiment_analysis(score1)
sentiment_analysis(score2)
