#!/usr/bin/env python3

import PyPDF2

pdf = "../example/Alice_in_Wonderland.pdf"

def text_extract(pdf):
	# Open the pdf file
	with open(pdf, "rb") as file:
		# Create PDF reader object
		reader = PyPDF2.PdfReader(file)

		page = reader.pages[5]
		
		text = page.extract_text()

		print(text)

text_extract(pdf)