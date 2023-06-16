#!/usr/bin/env python3

import pypdf
import nltk
import string

#This needs to be ran only once to download the 'Punkt' tokenizer
#nltk.download('punkt') # UNCOMMENT THIS WHEN YOU FIRST RUN THE SCRIPT 



pdf = "../example/fomcminutes20230201.pdf"

def text_extract(pdf):

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

		
	text = " ".join(all_text)

	return text

def tokenize(text):
	"""
	This function tokenizes the text extracted from the pdf at the word level. Each word 
	and punctuation will be tokenized. This step is usually done before removing of stop words,
	stemming etc. for ease of processing

	Usage: tokenize(string)
	"""
	return nltk.word_tokenize(text)

def remove_punctuation(tokens):
	"""

	"""
	cleaned_tokens = []

	for token in tokens:

		if token not in string.punctuation:

			if not all(char in ['_', '-', '.'] for char in token):

				cleaned_tokens.append(token)

	return cleaned_tokens


	

text = text_extract(pdf)
tokens = tokenize(text)
clean = remove_punctuation(tokens)
print(clean)


# with open("test.txt", "w") as file:
# 	file.write(text)

