import random
import string
import urllib.request

# input the url of Camellias
url1 = 'https://dev.gutenberg.org/files/1608/1608-0.txt'
response1 = urllib.request.urlopen(url1)
data1 = response1.read()  # a `bytes` object
text1 = data1.decode('utf-8')
# input the url of The Adventures of Tom Sawyer
url2 = 'https://dev.gutenberg.org/files/74/74-0.txt'
response2 = urllib.request.urlopen(url2)
data2 = response2.read()  # a `bytes` object
text2 = data2.decode('utf-8')


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


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    result = 0
    for v in hist.values():
        result += v
    return result


def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    # create a list
    common_words = []
    # create a stopwords list and a empty dictionary
    stop_words = []
    # store the stop words in stop_words dictionary
    f = open('data/stopwords.txt')
    for line in f:
        line = line.strip()
        stop_words.append(line)
    # get the word, frequency from the dictonary
    # create a tuple (freq, word)
    # append the (freq, word) tuple to the list
    # sort the list
    for word, freq in hist.items():
        if word in stop_words:
            hist[word] = None
        elif word == 'marguerite' or word == 'tom' or word == 'huck':
            hist[word] = None
        else:
            t = (freq, word)
            common_words.append(t)

    common_words.sort(reverse=True)

    return common_words


def print_most_common(hist, num):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:num]:
        print(word, '\t', freq)


# use the subtract to compare two books
def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    # create a new dictionary
    d = {}
    # for key in d1, if key also in d2, return key as None
    for key in d1:
        if key not in d2:
            d[key] = None
    return d


def main():
    hist1 = process_file(text1, skip_header=True)
    hist2 = process_file(text2, skip_header=True)

    # print the result for Camille
    print('Total number of words of Camille :', total_words(hist1))
    print('Number of different words of Camille :',
          different_words(hist1))

    t1 = most_common(hist1, excluding_stopwords=True)
    d1 = {}
    print('The most common words in Camille are:')
    for freq, word in t1[0:10]:
        print(word, '\t', freq)
    
    for freq, word in t1[0:100]:
        d1[word] = d1.get(word, 0) + 1
    
    # print the result for The Adventures of Tom Sawyer
    print('Total number of words of The Adventures of Tom Sawyer:', total_words(hist2))
    print('Number of different words of The Adventures of Tom Sawyer:',
          different_words(hist2))

    t2 = most_common(hist2, excluding_stopwords=True)
    d2 = {}
    print('The most common words in The Adventures of Tom Sawyer are:')
    for freq, word in t2[0:10]:
        d2[word] = d2.get(word, 0) + 1
        print(word, '\t', freq)
    
    for freq, word in t2[0:100]:
        d2[word] = d2.get(word, 0) + 1

    # compare two books' similarity in words
    diff = subtract(d1, d2)
    print("The words in the 100 most common words in Camille that aren't in the 100 most common words in The Adventures of Tom Sawyer are:")
    for word in diff.keys():
        print(word, end=' ')
    print('\n')
    diff = subtract(d2, d1)
    print("The words in the 100 most common words in The Adventures of Tom Sawyer that aren't in the 100 most common words in Camille are:")
    for word in diff.keys():
        print(word, end=' ')


if __name__ == '__main__':
    main()
