# Import Libraries
import re
import string
import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker

# Setup for logging is moved to main.py
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def process_pages(pages):
    page_numbers = []
    pages = [str(page) for page in pages]
    for page_range in pages:
        if "-" in page_range:
            start, end = [int(i) for i in page_range.split("-")]
            page_numbers.extend(list(range(start, end+1)))
        else:
            page_numbers.append(int(page_range))
    return page_numbers


def remove_punctuation(tokens: list) -> list:
    cleaned_tokens = []
    punctuation = string.punctuation + '_' + '-'
    for token in tokens:
        clean_token = ''.join(char for char in token if char not in punctuation)
        if clean_token: 
            cleaned_tokens.append(clean_token)
    return cleaned_tokens


def lowercase(tokens: list) -> list:
    lowercase = [token.lower() for token in tokens]
    return lowercase


def no_stop_words(tokens: list, stop_words_file: str = None) -> list:
    if stop_words_file:
        with open(stop_words_file, 'r') as f:
            stop_words = set(word.strip() for word in f.readlines())
    else:
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens


def stem(tokens: list) -> list:
    stemmer = PorterStemmer()
    stemmed_tokens = []
    for token in tokens:
        stemmed_tokens.append(stemmer.stem(token))
    return stemmed_tokens


def lemmatize(tokens: list)-> list:
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet', quiet=True)
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = []
    for token in tokens:
        lemmatized_tokens.append(lemmatizer.lemmatize(token))
    return lemmatized_tokens


def spell_check(tokens: list) -> list:
    spell = SpellChecker()
    corrected_tokens = [spell.correction(token) if not spell.known([token]) else token for token in tokens]
    return corrected_tokens


def write_to_file(tokens, output_file):
    with open(output_file, 'w') as f:
        f.write(str(tokens))
