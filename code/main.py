#!/usr/bin/env python3

import pypdf
import nltk
import string
from nltk.corpus import stopwords


try:
	nltk.data.find('corpora/stopwords')
	nltk.data.find('tokenizers/punkt')
except LookupError:
	print("Downloading required NLTK data...")
	nltk.download('stopwords')
	nltk.download('punkt')
    

pdf = "./example/fomcminutes20230201.pdf"

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
		return self.tokenize(text)




def remove_punctuation(tokens: list) -> list:
	"""

	"""
	cleaned_tokens = []

	for token in tokens:

		if token not in string.punctuation:

			if not all(char in ['_', '-', '.'] for char in token):

				cleaned_tokens.append(token)

	return cleaned_tokens


def lowercase(no_punc: list) -> list:
	lowercase = [token.lower() for token in no_punc]

	return lowercase


def no_stop_words(lower):
	stop_words = set(stopwords.words('english'))

	filtered_tokens = []
	for word in lower:
		if word not in stop_words:
			filtered_tokens.append(word)

	return filtered_tokens



text_prep = TextPrepare(pdf)
tokens = text_prep.prepare()
no_punc = remove_punctuation(tokens)
lower = lowercase(no_punc)
no_stop = no_stop_words(lower)
print(len(lower))
print(len(no_stop))