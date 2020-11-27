import re
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('wordnet')


def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = re.sub(r'\d', '', text)
    text = text.strip(' ')
    return text


def stem_text(series):
    stemmer = SnowballStemmer(language='english', ignore_stopwords=True)
    tokenized_by_word = word_tokenize(series)
    stop_words = set(stopwords.words('english'))
    stemmed_text = []
    result = ""
    for word in tokenized_by_word:
        if word not in stop_words:
            result += stemmer.stem(word) + " "
    stemmed_text.append(result)
    return stemmed_text
