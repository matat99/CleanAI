#!/usr/bin/env python3

import re
import pypdf
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


try:
	nltk.data.find('corpora/stopwords')
	nltk.data.find('tokenizers/punkt')
	nltk.data.find('corpora/wordnet')
except LookupError:
	print("Downloading required NLTK data...")
	nltk.download('stopwords')
	nltk.download('punkt')
	nltk.download('wordnet')
    

pdf = "../example/fomcminutes20230201.pdf"

class TextPrepare:
	def __init__(self, pdf):
		self.pdf = pdf 

	def text_extract(self):

		"""
		Extract ALL the text from a pdf file. 
		This includes headers and footers as well as the body. 

		Usage: text_extract(file)

		For now the path is hardcoded but this is only for testing purposes
		"""

		with open(pdf, "rb") as file:
			# Create PDF reader object
			reader = pypdf.PdfReader(file)

			all_text = []

			for page in reader.pages:
				all_text.append(page.extract_text())

			
		return " ".join(all_text)

	def join_hyphens(self, text):
		"""
		Join words that have been split with a hyphen (for example where a word that's too long has been 
		split to a new line witha hyphen) 
		"""
		return re.sub(r'(\w+)-\s*(\w+)', r'\1\2', text)



	def tokenize(self, text):
		"""
		This function tokenizes the text extracted from the pdf at the word level. Each word 
		and punctuation will be tokenized. This step is usually done before removing of stop words,
		stemming etc. for ease of processing

		Usage: tokenize(string)
		"""
		return nltk.word_tokenize(text)

	def prepare(self):
		text = self.text_extract()
		text_no_hyphen = self.join_hyphens(text)
		return self.tokenize(text_no_hyphen)




def remove_punctuation(tokens: list) -> list:
	"""
	Remove punctuation, lone double quotes, bullet points, and backticks
	"""
	cleaned_tokens = []

	for token in tokens:

		if token.isalnum():

			cleaned_tokens.append(token)

	return cleaned_tokens


def lowercase(tokens: list) -> list:
	lowercase = [token.lower() for token in tokens]

	return lowercase


def no_stop_words(tokens):
	stop_words = set(stopwords.words('english'))

	filtered_tokens = []
	for word in tokens:
		if word not in stop_words:
			filtered_tokens.append(word)

	return filtered_tokens

def stem(tokens):
	stemmer = PorterStemmer()

	stemmed_tokens = []

	for token in tokens:
		stemmed_tokens.append(stemmer.stem(token))

	return stemmed_tokens

def lemmatize(tokens):
	lemmatizer = WordNetLemmatizer()

	lemmatized_tokens = []

	for token in tokens:
		lemmatized_tokens.append(lemmatizer.lemmatize(token))

	return lemmatized_tokens




text_prep = TextPrepare(pdf)
tokens = text_prep.prepare()
no_punc = remove_punctuation(tokens)
lower = lowercase(no_punc)
no_stop = no_stop_words(lower)
#stemmed = stem(no_stop)
lemmat = lemmatize(no_stop)

print(lemmat)
