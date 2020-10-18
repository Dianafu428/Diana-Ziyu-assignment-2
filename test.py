import urllib.request
import string
import random
import nltk
# nltk.download('all')
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

url_Camille = 'https://dev.gutenberg.org/files/1608/1608-0.txt'
text1 = download_book(url_Camille)
url_Tom = 'https://dev.gutenberg.org/files/74/74-0.txt'
text2 = download_book(url_Tom)

import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print("Cosine:", cosine)