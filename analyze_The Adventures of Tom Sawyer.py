import random
import string
import urllib.request

# input the url of The Adventures of Tom Sawyer
url = 'https://dev.gutenberg.org/files/74/74-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
text = data.decode('utf-8')
# print(text) for testing


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
        elif word == 'tom' or word == 'huck':
            hist[word] = None
        else:
            t = (freq, word)
            common_words.append(t)

    common_words.sort(reverse=True)

    return common_words


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist, excluding_stopwords=True)
    print('The most common words are:')
    for freq, word in t[0:num]:
        print(word, '\t', freq)


def main():
    hist = process_file(text, skip_header=True)
    # print(hist)
    print('Total number of words of The Adventures of Tom Sawyer:', total_words(hist))
    print('Number of different words of The Adventures of Tom Sawyer:',
          different_words(hist))

    t = most_common(hist, excluding_stopwords=True)
    print('The most common words in The Adventures of Tom Sawyer are:')
    for freq, word in t[0:10]:
        print(word, '\t', freq)


if __name__ == '__main__':
    main()
