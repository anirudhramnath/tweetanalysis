#! /usr/bin/env python

from bs4 import BeautifulSoup
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import re

def clean_tweets(raw_tweets):
    tweets = []
    for (words, sentiment) in raw_tweets:
        words_filtered = []
        words = strip_html(words)
        #remove URLs
        words = re.sub('https?://[^\s]+', '', words)
        #remove numbers
        words = re.sub('\d+', '', words)

        tokens = tokenizer.tokenize(words)

        for e in tokens:
            e = e.lower()
            if e.startswith('@') or e in stop_words: continue
            clean_word = lemmatize(e)

            if len(clean_word) > 2:
                words_filtered.append(clean_word)

        tweets.append((words_filtered, sentiment))

    return tweets

def clean_test_tweets(raw_tweets):
    tweets = []
    for words in raw_tweets:
        words_filtered = []
        words = strip_html(words)
        #remove URLs
        words = re.sub('https?://[^\s]+', '', words)
        #remove numbers
        words = re.sub('\d+', '', words)

        tokens = tokenizer.tokenize(words)
        for e in tokens:
            e = e.lower()
            if e.startswith('@') or e in stop_words: continue
            clean_word = lemmatize(e)

            if len(clean_word) > 2:
                words_filtered.append(clean_word)

        tweets.append(words_filtered)

    return tweets

def lemmatize(word):
    return porter_stemmer.stem(word)


def strip_html(markup):
    try:
        
        soup = BeautifulSoup(markup, 'html.parser')
    except Exception:
        print markup
    return soup.get_text()

porter_stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+')

stop_words = ['i','me','my','myself','we','our','ours','ourselves','you','your','yours',
                'yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its',
                'itself','they','them','their','theirs','themselves','what','which','who','whom','this',
                'that','these','those','am','is','are','was','were','be','been','being','have','has','had',
                'having','do','does','did','doing','a','an','the','and','but','if','or','because',
                'as','while','of','at','by','for','with','about','between','into',
                'through','during','before','after','above','below','to','from',
                'on','off','over','under','again','further','then','once','here','there','when','where',
                'why','how','all','any','both','each','other','some','such',
                'only','own','same','so','than','too','s','t','can','just',
                'now']

#stop_words = ['nothing here']
