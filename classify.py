from pickle import  dump, load 
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from sklearn.svm import LinearSVC
from nltk.classify.scikitlearn import SklearnClassifier


import nltk
from dataclean import clean_tweets
from dataclean import clean_test_tweets
from pprint import pprint
import openpyxl

class_value_mapping={
1:"positive",
-1:"negative",
0:"neutral"
}

def get_features_from_tweets(tweets):
    features = []
    for (words, sentiment) in tweets:
        features.extend(words)
    return features


def get_unique_features(feature_list):
    feature_frequency_distribution = nltk.FreqDist(feature_list)
    unique_features = feature_frequency_distribution.keys()
    return unique_features


def get_feature_mapping(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


classifier_dict = load(open('classifier.pyc', 'w'))
classifier = classifier_dict['classifier']
word_feature = classifier_dict['feature_list']
#classifier = SklearnClassifier(LinearSVC()).train(training_set)
#classifier = nltk.NaiveBayesClassifier.train(training_set)
    
correct, total = 0., 0.
no_class_pos = 0.
no_class_neg = 0.
no_class_neu = 0.
no_result_pos = 0.
no_result_neg = 0.
no_result_neu = 0.
true_pos = 0.
true_neg = 0.
true_neu = 0.
correct_class_pos = 0.
correct_class_neg = 0.
correct_class_neu = 0.
list_of_input = range(2, 720)
test_tweet_list = []
for i in list_of_input:
    try:
        original_tweet_string = str(sheet_obama.cell(row=i,column=4).value)
        tweet_class = class_value_mapping[int(sheet_obama.cell(row=i,column=5).value)]
        tweet_string = clean_test_tweets([original_tweet_string])[0]
        test_tweet_list.append((tweet_string, tweet_class, original_tweet_string))
    except Exception:
        pass
for (tweet, class_type, original_tweet_string) in test_tweet_list:
    result = classifier.classify(get_feature_mapping(tweet))
    total += 1
    if class_type == result: correct += 1
    if class_type == 'positive':
        no_class_pos += 1
        if result == 'positive':
            correct_class_pos += 1;
    if result == 'positive':
        no_result_pos += 1
        if class_type == 'positive':
            true_pos += 1
    if class_type == 'negative':
        no_class_neg += 1
        if result == 'negative':
            correct_class_neg += 1;
    if result == 'negative':
        no_result_neg += 1
        if class_type == 'negative':
            true_neg += 1
    if class_type == 'neutral':
        no_class_neu += 1
        if result == 'neutral':
            correct_class_neu += 1;
    if result == 'neutral':
        no_result_neu += 1
        if class_type == 'neutral':
            true_neu += 1
print 'For fold'+str(fold)
print 'accuracy: '+str(correct * 100/total)
accuracy_list.append(correct * 100/total)
print 'Precision for pos:' + str(true_pos*100/no_result_pos)
pos_precision_list.append(true_pos*100/no_result_pos)
print 'Precision for neg:' + str(true_neg*100/no_result_neg)
neg_precision_list.append(true_neg*100/no_result_neg)
print 'Precision for neu:' + str(true_pos*100/no_result_neu)
neu_precision_list.append(true_neu*100/no_result_neu)
print 'Recall for pos:' + str(correct_class_pos*100/no_class_pos)
pos_recall_list.append(correct_class_pos*100/no_class_pos)
print 'Recall for neg:' + str(correct_class_neg*100/no_class_neg)
neg_recall_list.append(correct_class_neg*100/no_class_neg)
print 'Recall for neu:' + str(correct_class_neu*100/no_class_neu)
neu_recall_list.append(correct_class_neu*100/no_class_neu)
print '\n'
