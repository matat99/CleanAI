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
import json


# Checking if necessary NLTK corpora are available and if not, downloading them
corpora = ['stopwords', 'punkt', 'wordnet']
for corpus in corpora:
	try:
		nltk.data.find(f'corpora/{corpus}')
	except LookupError:
		nltk.download(corpus, quiet=True)


class TextPrepare:
	"""
	Class for preparing text for further processing. It extracts text from a given pdf file, conjoins any hyphenated words and tokenizes it.
	
	Parameters:
	pdf (str): The path of the PDF file to process.

	Methods:
	text_extract(): Extracts all the text from a pdf file. 
	join_hyphens(text): Joins words that have been split with a hyphen.
	tokenize(text): Tokenizes the given text at the word level.
	prepare(): Extracts text from a pdf, conjoins any hyphenated words and tokenizes it.
	"""
	def __init__(self, pdf, pages=None, level='word'):
		self.pdf = pdf 
		self.level = level

		if pages:
			self.pages = process_pages(pages)  
		else:
			self.pages = None

	def text_extract(self, pages=None):

		with open(self.pdf, "rb") as file:
			# Create PDF reader object
			reader = pypdf.PdfReader(file)

			all_text = []
			
			if self.pages:
				pages_to_extract = self.pages
			else:
				pages_to_extract = range(len(reader.pages))

			for i in pages_to_extract:
				page_text = reader.pages[i].extract_text()
				page_text = page_text.replace("\n", " ")
				all_text.append(page_text)

			text = ' '.join(all_text)

			text = re.sub(r"[-_]{3,}", " ", text)


		return text

	def expand_contractions(self, text):
		"""
		Expand contractions in given text.
		
		Parameters:
		text (str): Text to expand.

		Returns:
		str: Text with expanded contractions.
		"""
		with open('./supplementary/contractions.json', 'r') as f:
			contraction_map = json.load(f)

		contractions_pattern = re.compile('({})'.format('|'.join(contraction_map.keys())), flags=re.IGNORECASE|re.DOTALL)

		def expand_match(contraction):
			match = contraction.group(0)
			first_char = match[0]
			expanded_contraction = contraction_map.get(match) if contraction_map.get(match) else contraction_map.get(match.lower())
			expanded_contraction = first_char+expanded_contraction[1:]
			return expanded_contraction

		expanded_text = contractions_pattern.sub(expand_match, text)
		expanded_text = re.sub("'", "", expanded_text)

		return expanded_text



	def join_hyphens(self, text):
		
		pattern = r"(\w)\s*-\s*(\w)"

		def replace(match):

			return match.group(1) + match.group(2)

		return re.sub(pattern, replace, text)


	def tokenize(self, text):
		
		if self.level == 'sentence':
			return nltk.sent_tokenize(text)
		else:
			return nltk.word_tokenize(text)

	def prepare(self):
		text = self.text_extract()
		text_no_hyphen = self.join_hyphens(text)
		text_no_contractions = self.expand_contractions(text_no_hyphen)
		return self.tokenize(text_no_hyphen)




def remove_punctuation(tokens: list) -> list:
	"""
	Remove punctuation from given tokens.
	
	Parameters:
	tokens (list): List of tokens to remove punctuation from.

	Returns:
	list: Tokens without punctuation.
	"""
	cleaned_tokens = []

	punctuation = string.punctuation + '_' + '-'

	for token in tokens:

		clean_token = ''.join(char for char in token if char not in punctuation)

		if clean_token: 

			cleaned_tokens.append(clean_token)

	return cleaned_tokens


def lowercase(tokens: list) -> list:
	"""
	Convert all tokens to lowercase.
	
	Parameters:
	tokens (list): List of tokens to convert.

	Returns:
	list: Tokens in lowercase.
	"""
	lowercase = [token.lower() for token in tokens]

	return lowercase


def no_stop_words(tokens: list) -> list:
	"""
	Remove stop words from given tokens.
	
	Parameters:
	tokens (list): List of tokens to filter stop words from.

	Returns:
	list: Tokens without stop words.
	"""
	stop_words = set(stopwords.words('english'))

	filtered_tokens = []

	for word in tokens:
		if word not in stop_words:
			filtered_tokens.append(word)

	return filtered_tokens

def stem(tokens: list) -> list:
	"""
	Stem given tokens using PorterStemmer.
	
	Parameters:
	tokens (list): List of tokens to stem.

	Returns:
	list: Stemmed tokens.
	"""
	stemmer = PorterStemmer()

	stemmed_tokens = []

	for token in tokens:
		stemmed_tokens.append(stemmer.stem(token))

	return stemmed_tokens

def lemmatize(tokens: list)-> list:
	"""
	Lemmatize given tokens using WordNetLemmatizer.
	
	Parameters:
	tokens (list): List of tokens to lemmatize.

	Returns:
	list: Lemmatized tokens.
	"""
	lemmatizer = WordNetLemmatizer()

	lemmatized_tokens = []

	for token in tokens:
		lemmatized_tokens.append(lemmatizer.lemmatize(token))

	return lemmatized_tokens

def write_to_file(tokens, output_file):
	"""
	Write given tokens to a file.
	
	Parameters:
	tokens (list): List of tokens to write.
	output_file (str): The name of the file to write the tokens to.
	"""
	with open(output_file, 'w') as f:
		f.write(str(tokens))

def process_pages(pages):
	"""
	Process a list of page ranges into a list of page numbers.

	Parameters:
	pages (list): List of strings representing page ranges (e.g. ["1", "3-5"]).

	Returns:
	list: List of page numbers to process (e.g. [1, 3, 4, 5]).
	"""
	page_numbers = []

	pages = [str(page) for page in pages] # for some reason argparse was passing pages as integers which it is not even supposed to do tf?
		
	for page_range in pages:
		if "-" in page_range:
			start, end = [int(i) for i in page_range.split("-")]
			page_numbers.extend(list(range(start, end+1)))
		else:
			page_numbers.append(int(page_range))
	return page_numbers

def main(args):
	"""
	Main function to process and clean text from a given pdf file.
	
	Parameters:
	args (Namespace): The arguments parsed from command line.
	"""
	pages = process_pages(args.pages) if args.pages else None

	text_prep = TextPrepare(args.f, pages, args.level)

	tokens = text_prep.prepare()


	operations = {
		'remove_punc': remove_punctuation,
		'rp': remove_punctuation,
		'no_stop_words': no_stop_words,
		'remove_stop': no_stop_words,
		'rs': no_stop_words,
		'lemmatize': lemmatize,
		'lemm': lemmatize,
		'stem': stem,
		'lowercase': lowercase,
		'l': lowercase,

	}

	for operation in args.operations:
		if operation not in operations:
			raise ValueError(f"Invalid operation: {operation}")
		tokens = operations[operation](tokens)


	write_to_file(tokens, args.output)


if __name__ == "__main__":

	parser = argparse.ArgumentParser(description='Process and clean PDF text',  
									 usage='%(prog)s -f <pdf_path> -o [operations] -out <output_file>\nExample: %(prog)s -f /path/to/your/pdf -o rm l ns -out output.txt')
	parser.add_argument('-f', type=str, required=True, help='PDF file path.')
	parser.add_argument('-o', '--operations', type=str, nargs='+', required=True, 
						help='Operations: rp (remove punctuation), l (lowercase), rs (remove stop words), lemm (lemmatize), stem (apply stemming). Apply in the order provided.')
	parser.add_argument('-out', '--output', type=str, default='output.txt', help='Output file name.')
	parser.add_argument('-p', '--pages', type=str, nargs='+', help='Pages to extract. Can be single numbers or ranges (e.g. 0-3). If omitted, all pages will be processed.)')
	parser.add_argument('-l', '--level', type=str, default='word', help='Level of tokenization: "word" or "sentence". If omitted, word level tokenization will be applied.')


	args = parser.parse_args()

	if not args.f or not args.operations:
		parser.print_usage()
	else:
		main(args)







