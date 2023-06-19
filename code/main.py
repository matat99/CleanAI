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
	def __init__(self, pdf):
		self.pdf = pdf 

	def text_extract(self):

		with open(self.pdf, "rb") as file:
			# Create PDF reader object
			reader = pypdf.PdfReader(file)

			all_text = []

			for page in reader.pages:
				all_text.append(page.extract_text())

			
		return " ".join(all_text)

	def join_hyphens(self, text):
		
		return re.sub(r'(\w+)\s*-\s*(\w+)', r'\1\2', text)



	def tokenize(self, text):
		
		return nltk.word_tokenize(text)

	def prepare(self):
		text = self.text_extract()
		text_no_hyphen = self.join_hyphens(text)
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

	for token in tokens:

		if token.isalnum():

			cleaned_tokens.append(token)

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

def main(args):
	"""
    Main function to process and clean text from a given pdf file.
    
    Parameters:
    args (Namespace): The arguments parsed from command line.
    """
	text_prep = TextPrepare(args.f)

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
			print(f"WARNING: '{operation}' is not a valid opperation.")
			return

	for operation in args.operations:
		tokens = operations[operation](tokens)

	write_to_file(tokens, args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process and clean PDF text',  
                                     usage='%(prog)s -f <pdf_path> -o [operations] -out <output_file>\nExample: %(prog)s -f /path/to/your/pdf -o rm l ns -out output.txt')
    parser.add_argument('-f', type=str, required=True, help='PDF file path.')
    parser.add_argument('-o', '--operations', type=str, nargs='+', required=True, 
                        help='Operations: rp (remove punctuation), l (lowercase), rs (remove stop words), lemm (lemmatize), stem (apply stemming). Apply in the order provided.')
    parser.add_argument('-out', '--output', type=str, default='output.txt', help='Output file name.')

    args = parser.parse_args()

    if not args.f or not args.operations:
        parser.print_usage()
    else:
        main(args)







