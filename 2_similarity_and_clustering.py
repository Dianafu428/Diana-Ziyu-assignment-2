import urllib.request
import string
import random
import nltk
# nltk.download('all')
# nltk.download('vader_lexicon')

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

url_Camille = 'https://dev.gutenberg.org/files/1608/1608-0.txt'
text1 = download_book(url_Camille)
url_Tom = 'https://dev.gutenberg.org/files/74/74-0.txt'
text2 = download_book(url_Tom)
# url_Oliver = 'http://www.gutenberg.org/cache/epub/730/pg730.txt'
# text3 = download_book(url_Oliver)
url_Alice = 'http://www.gutenberg.org/files/11/11-0.txt'
text3 = download_book(url_Alice)
url_Finn = 'http://www.gutenberg.org/files/76/76-0.txt'
text4 = download_book(url_Finn)
url_Pudd = 'http://www.gutenberg.org/files/102/102-0.txt'
text5 = download_book(url_Pudd)
url_Prince = 'http://www.gutenberg.org/files/1837/1837-0.txt'
text6 = download_book(url_Prince)
url_Glass = 'http://www.gutenberg.org/files/12/12-0.txt'
text7 = download_book(url_Glass)

# Program to measure the similarity between two texts using cosine similarity. 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

# tokenization 
text1_list = word_tokenize(text6)  
text2_list = word_tokenize(text7) 

# sw contains the list of stopwords
sw = stopwords.words('english')  
l1 =[]
l2 =[] 

# remove stop words from the string 
text1_set = {w for w in text1_list if not w in sw}  
text2_set = {w for w in text2_list if not w in sw} 

# form a set containing keywords of both strings  
rvector = text1_set.union(text2_set)  
for w in rvector: 
    if w in text1_set: 
        l1.append(1) # create a vector 
    else: 
        l1.append(0) 
    if w in text2_set: 
        l2.append(1) 
    else: 
        l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 

import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray([[1., 0.44466285622087914, 0.4459925331004415, 0.373839884087373, 0.446374418830339, 0.439693491778613, 0.458404637313088],
    [0.44466285622087914, 1., 0.4073419782971952, 0.453664762151034, 0.476688725908798, 0.473917497554727, 0.415425473553053], 
    [0.4459925331004415, 0.4073419782971952, 1, 0.388594248654620, 0.398433457552459, 0.396344271072345, 0.556547187188917],
    [0.373839884087373, 0.453664762151034, 0.388594248654620, 1., 0.407812645850923, 0.372860849117610, 0.400128625380280],
    [0.446374418830339, 0.476688725908798, 0.398433457552459, 0.407812645850923, 1, 0.452992594884041, 0.395325987962274],
    [0.439693491778613, 0.473917497554727, 0.396344271072345, 0.372860849117610, 0.452992594884041, 1, 0.401580397822096], 
    [0.458404637313088, 0.415425473553053, 0.556547187188917, 0.400128625380280, 0.395325987962274, 0.401580397822096, 1]])

# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))


plt.show()