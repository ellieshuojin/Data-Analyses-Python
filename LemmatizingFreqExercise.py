import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


# Loading The Adventures of Sherlock Holmes by Arthur Conan Doyle
# from the Project Gutenberg
from urllib import request
url = "http://www.gutenberg.org/ebooks/1661.txt.utf-8"
response = request.urlopen(url)
rawText = response.read().decode('utf8')


# tokenizing
wordText = nltk.word_tokenize(rawText)

# word frequency before doing fancy text processing stuff
#print('Before text processing')
#wordFreqBefore = nltk.FreqDist(wordText)

wordList = ['think', 'Think', 'thinks', 'Thinks', 'thought', 'Thought', 'thinking', 'Thinking']
wordFrequency = nltk.FreqDist(wordText)

frequency = [wordFrequency[word1] for word1 in wordList]

print('Sum ==', np.sum(frequency))
