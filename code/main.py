#!/usr/bin/env python3

# Importing Required Libraries
import re
import pypdf
import nltk
import string
import argparse
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


# Checking if necessary NLTK corpora are available and if not, downloading them
try:
	nltk.data.find('corpora/stopwords')
	nltk.data.find('tokenizers/punkt')
	nltk.data.find('corpora/wordnet')
except LookupError:
	print("Downloading required NLTK data...")
	nltk.download('stopwords')
	nltk.download('punkt')
	nltk.download('wordnet')
    

class TextPrepare:
	"""
	Class that will do the basic text preparation for further cleaning. This class will extract 
	the text from a pdf, conjoin any hyphenated words, and finally tokenize it. This standardizes the process
	and makes sure each file has gone through basic cleaning.

	"""
	def __init__(self, pdf):
		self.pdf = pdf 

	def text_extract(self):

		"""
		Extract ALL the text from a pdf file. 
		This includes headers and footers as well as the body. 

		Usage: text_extract(file)

		For now the path is hardcoded but this is only for testing purposes
		"""

		with open(self.pdf, "rb") as file:
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
	"""
	Converts all tokens into lowercase
	"""
	lowercase = [token.lower() for token in tokens]

	return lowercase


def no_stop_words(tokens):
	"""
	Removes stop words from tokens like 'and', 'the' etc.
	"""
	stop_words = set(stopwords.words('english'))

	filtered_tokens = []
	for word in tokens:
		if word not in stop_words:
			filtered_tokens.append(word)

	return filtered_tokens

def stem(tokens):
	"""
	Stems tokens 
	"""
	stemmer = PorterStemmer()

	stemmed_tokens = []

	for token in tokens:
		stemmed_tokens.append(stemmer.stem(token))

	return stemmed_tokens

def lemmatize(tokens):
	"""
	lemmatizes tokens
	"""
	lemmatizer = WordNetLemmatizer()

	lemmatized_tokens = []

	for token in tokens:
		lemmatized_tokens.append(lemmatizer.lemmatize(token))

	return lemmatized_tokens

def write_to_file(tokens, output_file):
	with open(output_file, 'w') as f:
		f.write(','.join(tokens))

def main(args):
	# Instance of TextPrepare 
	text_prep = TextPrepare(args.f)

	tokens = text_prep.prepare()


	operations = {
		'remove_punc': remove_punctuation,
		'rm': remove_punctuation,
		'no_stop_words': no_stop_words,
		'no_stop': no_stop_words,
		'ns': no_stop_words,
		'lemmatize': lemmatize,
		'lemm': lemmatize,
		'stem': stem,
		'lowercase': lowercase,
		'l': lowercase,

	}

	for operation in args.operations:
		if operation in operations:
			tokens = operations[operation](tokens)
		else:
			print(f"WARNING: '{operation}' is not a valid opperation.")

	write_to_file(tokens, args.out)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Process and clean PDF text')
	parser.add_argument('-f', type=str, help='Path to the PDF file to process.')
	parser.add_argument('-o', '--operations', type=str, nargs='+', help='List of operations to apply to the text in the order provided. Options: remove_punc, lowercase, no_stop_words, lemmatize, stem.')
	parser.add_argument('-out', '-output', type=str, default='output.txt', help='provide a name for the file you want the tokens to be outputted to.')

	args = parser.parse_args()
	main(args)





# this is where I make sure all the code runs as intended and play around with the flow 
# of all the functions. This will not be in the final version of the code.

# text_prep = TextPrepare(pdf)
# tokens = text_prep.prepare()
# no_punc = remove_punctuation(tokens)
# lower = lowercase(no_punc)
# no_stop = no_stop_words(lower)
# #stemmed = stem(no_stop)
# lemmat = lemmatize(no_stop)

# print(lemmat)
