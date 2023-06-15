#!/usr/bin/env python3

import pypdf

pdf = "../example/Alice_in_Wonderland.pdf"

def text_extract(pdf):

	"""
	Extract ALL the text from a pdf file. 
	This includes headers and footers as well as the body. 

	Usage: text_extract(/pat/to/file)

	For now the path is hardcoded but this is only for testing purposes
	"""

	with open(pdf, "rb") as file:
		# Create PDF reader object
		reader = pypdf.PdfReader(file)

		page = reader.pages[5]
		
		text = page.extract_text()

	return text

text = text_extract(pdf)
print(text)
