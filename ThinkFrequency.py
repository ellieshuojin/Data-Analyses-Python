import nltk
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
print('Before text processing')
wordFreqBefore = nltk.FreqDist(wordText)

# frequencies of the different forms of verb "think"
think = ['think','Think','thinks','Thinks','thought','Thought',
         'thinking','Thinking']
for iThink in think:
    print('%-10s: %4d' % (iThink, wordFreqBefore[iThink]))


# POS tag of the text
wordPOS = nltk.pos_tag(wordText)


# figuring out frequencies of "thought" as nouns or verbs
thought_n = 0
thought_v = 0
for w in wordPOS:
    if w[0] == "thought" and 'NN' in w[1]:
        thought_n += 1
    elif w[0] == "thought" and 'VB' in w[1]:
        thought_v += 1

print('Thought as a verb: %d' % thought_v)
print('Thought as a noun: %d' % thought_n)


# figuring out frequencies of "thinking" as nouns or verbs
thinking_n = 0
thinking_v = 0
for w in wordPOS:
    if w[0] == "thinking" and 'NN' in w[1]:
        thinking_n += 1
    elif w[0] == "thinking" and 'VB' in w[1]:
        thinking_v += 1

print('Thinking as a verb: %d' % thinking_v)
print('Thinking as a noun: %d' % thinking_n)
