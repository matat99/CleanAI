from contractions import expand_contractions
import pypdf
from bs4 import BeautifulSoup
import utils
import logging
import re
import string
import nltk
import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from spellchecker import SpellChecker

class TextPrepareBase:
    def __init__(self, path, pages=None, level='word', verbosity=1):
        self.path = path
        self.level = level
        self.verbosity = verbosity

        self.pages = process_pages(pages) if pages else None


    def text_extract(self):
        raise NotImplementedError("Each Subclass should implement this method")


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
            try:
                nltk.data.find('tokenizers/punkt')
            except LookupError:
                nltk.download('punkt', quiet=True)

            if self.level == 'sentence':
                return nltk.sent_tokenize(text)
            else:
                return nltk.word_tokenize(text)

    def prepare(self):
        logging.info("Preparing text for processing.")
        text = self.text_extract()
        text_no_hyphen = self.join_hyphens(text)
        text_no_contractions = self.expand_contractions(text_no_hyphen)
        return self.tokenize(text_no_contractions)

class HTMLPrepare(TextPrepareBase):
    """
    Class for preparing text for further prorcessing. It extracts text from It extracts text from a given HTML file, conjoins any hyphenated words, expands contractions, and tokenizes it
    """
    def __init__(self, path, pages=None, level='word', verbosity=1):
        super().__init__(path, pages, level, verbosity)

    def text_extract(self):
        logging.info("Starting to extract text from file")

        if not (self.path.endswith(".html") or self.path.endswith(".htm")):
            raise ValueError(f"File {self.path} is not an HTML or HTM file")

        with open(self.path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Define the tags we want to extract text from based on verbosity
        if self.verbosity == 1:
            tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ol', 'ul']
        elif self.verbosity == 2:
            tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'ol', 'ul', 
                    'td', 'th', 'caption', 'blockquote']
        else:  # verbosity == 3
            tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'li', 'ol', 'ul', 
                    'td', 'th', 'caption', 'blockquote', 'div', 'span', 'pre', 'figure', 
                    'figcaption', 'summary', 'details']

        # Extract the text from the specified tags and join them together
        text = ' '.join([t.get_text() for t in soup.find_all(tags)])

        return text

class PDFPrepare(TextPrepareBase):
    """
    Class for preparing text for further processing. It extracts text from a given pdf file, conjoins any hyphenated words, expands contractions, and tokenizes it.
    
    Parameters:
    pdf (str): The path of the PDF file to process.
    pages (list, optional): List of pages or page ranges to process. For example, ["1", "3-5"] will process pages 1, 3, 4, and 5. If omitted, all pages in the PDF will be processed.
    level (str, optional): Level of tokenization. Can be "word" or "sentence". If omitted, word level tokenization will be applied.

    Methods:
    text_extract(): Extracts all the text from a pdf file. 
    expand_contractions(text): Expands contractions in a given text.
    join_hyphens(text): Joins words that have been split with a hyphen.
    tokenize(text): Tokenizes the given text at the word level.
    prepare(): Extracts text from a pdf, conjoins any hyphenated words, expands contractions, and tokenizes it.
    """
    def __init__(self, path, pages=None, level='word'):
        super().__init__(path, pages, level)

    def text_extract(self):
        logging.info("Starting text extraction from file")


        with open(self.path, "rb") as file:
            # Create PDF reader object
            reader = pypdf.PdfReader(file)

            all_text = []

            if self.pages:
                pages_to_extract = self.pages
            else:
                pages_to_extract = range(len(reader.pages))

            for i in pages_to_extract:
                try:
                    # Load page individually
                    page = reader.pages[i]
                    page_text = page.extract_text()
                    page_text = page_text.replace("\n", " ")
                    all_text.append(page_text)

                    # Remove reference to page and text to allow it to be garbage collected
                    del page
                    del page_text

                except Exception as e:
                    logging.error(f"Failed to extract text from the page {i}: {e}")

            text = ' '.join(all_text)

            text = re.sub(r"[-_]{3,}", " ", text)

        return text