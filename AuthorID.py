# ChiaHui Liu, Marguerite Ashby, and Ellie Shuo Jin
# PSY 394U
# 5.3.18
# Hackathon 2

'''The problem: In forensic linguistics, writeprint refers to the identity of an author based on his/her writing. One way to establish someone's writeprint is by examining his/her lexical features, or the vocabulary. The goal of the following program is to writeprint authors based on their writing. The dataset Reuter-50-50 includes 50 writings by 50 authors contributing to Reuter. The following program randomly draws 4 authors from the dataset and contructs a classifier using each author's writings for the training data (under c50train directory). Then, the performance of the classifier is evaluated on a set of testing data from the same authors (under c50test directory).'''

'''The solution: A program that randomly selects 4 authors from the complete dataset, trains, and evaluates the performance of two different classifers (e.g., Naive Bayes and Linear SVM) on the testing data.'''

# import libraries
import os
import glob
import errno
import random
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# pick four random authors from complete author list
def pick_four_authors():
    root = "./C50/C50train/"
    author_list = []
    # obtain complete author list
    for path, subdirs, files in os.walk(root):
        author_path = str(os.path.join(path))
        author_list.append(author_path[15:])
    # randomly select four authors from complete author list
    random_four_authors = random.sample(author_list, 4)
    return random_four_authors

random_four_authors = pick_four_authors()

# obtain texts from each author
def author_list(author, TrainTest):
    path = './C50/'+TrainTest+'/'+author+'/*.txt'
    files = glob.glob(path)
    author_text = []
    for name in files:
        res = []
        try:
            with open(name) as f:
                for line in f:
                    res.append(line)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
        author_text.append(res[0])
    return author_text

# creating training and testing datasets
X_train = []
X_test = []
for each_author in random_four_authors:
    X_train.extend(author_list(each_author, 'C50train'))
    X_test.extend(author_list(each_author, 'C50test'))

Y_train = []
Y_test = []
for each_author in random_four_authors:
    for i in range(50):
        Y_train.append(each_author)
        Y_test.append(each_author)

# word occurrence counts
count_vect = CountVectorizer()
X_train_countVec = count_vect.fit_transform(X_train)

# converting to term frequency
tf_transformer = TfidfTransformer().fit(X_train_countVec)
X_train_tf = tf_transformer.transform(X_train_countVec)

# take naive Bayes as classifier
clf_nb = MultinomialNB().fit(X_train_tf, Y_train)

# converting the testing set to term frequency
X_test_countVec= count_vect.transform(X_test)
X_test_tf = tf_transformer.transform(X_test_countVec)

# predict y
Y_pred_nb = clf_nb.predict(X_test_tf)

# accuracy and performance
print('Accuracy - Naive Bayes: %6.4f' % accuracy_score(Y_test,Y_pred_nb))
print(confusion_matrix(Y_test,Y_pred_nb))
print(classification_report(Y_test,Y_pred_nb))

# now take SVM as classifier (linear kernel)
clf_svm = LinearSVC().fit(X_train_tf, Y_train)

# predict y
Y_pred_svm = clf_svm.predict(X_test_tf)

# accuracy and performance
print('Accuracy - Linear SVM: %6.4f' % accuracy_score(Y_test,Y_pred_nb))
print(confusion_matrix(Y_test,Y_pred_svm))
print(classification_report(Y_test,Y_pred_svm))


'''Bonus: Plotting WordClouds for the authors'''

import nltk
import itertools
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score

# tokenize, lower case, remove punctuation, remove stop words
stop_words = set(stopwords.words('english'))  # stop words in English
ps = PorterStemmer()  # stemmer object
X_proc =[]
for iDoc in X_train:
    # tokenize into words
    wordText = nltk.word_tokenize(iDoc)
    # removing punctuation marks & stop words, making all words lower case,
    wordDePunct = [w.lower() for w in wordText if w.isalpha()]
    wordNoStopwd = [w for w in wordDePunct if w not in stop_words]
    # stemming
    wordStem = [ps.stem(w) for w in wordNoStopwd]
    # putting back into a document
    X_proc.append(' '.join(wordStem))

X_proc = list(filter(None, X_proc))
# converting to frequencies to be used as features
X_countVec = CountVectorizer().fit_transform(X_proc)
#X_countVec = CountVectorizer().fit_transform(addrList)
X_tf = TfidfTransformer().fit_transform(X_countVec)

# K-means clustering
km = KMeans(n_clusters=4)
km.fit(X_tf)  # fitting the principal components
Y_clus = km.labels_   # clustering info resulting from K-means

# generating word cloud for each author
for iClus in range(max(Y_clus)+1):
    # first, concatenating all texts for that author
    allText = ''
    for j,jClus in enumerate(Y_clus):
        if jClus==iClus:  # i.e., text belongs to the author
            allText += X_proc[j]
            #allText += addrList[j]
            allText += ' '

    # generating the word cloud
    wordcloud = WordCloud(max_font_size=80,
                          background_color='white',
                          collocations=False,
                          width=800,
                          height=400).generate(allText)
    # print the most freq 8 elements for each author
    wordcloud_words = wordcloud.words_
    iterator = iter(wordcloud_words.keys())
    print('Author: ' + random_four_authors[(iClus)])
    most_freEelements = list(itertools.islice(iterator, 0, 8))
    for each_element in most_freEelements:
        print(each_element)

    # display the generated image:
    plt.figure(figsize=[10,5])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title('Author: ' + random_four_authors[(iClus)], fontsize=24)
    plt.show()
    print()
