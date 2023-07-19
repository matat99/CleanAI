#!/usr/bin/env python3


# Import Libraries
import argparse
import logging
import text_prepare
import utils

# Set up logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def main(args):
    """
    Main function to process and clean text from a given pdf file.
    
    Parameters:
    args (Namespace): The arguments parsed from command line.
    """
    logging.info("Starting main function.")

    text_prep = text_prepare.PDFPrepare(args.f, args.pages, args.level) if args.f.split('.')[-1] == 'pdf' else text_prepare.HTMLPrepare(args.f, args.pages, args.level)
    tokens = text_prep.prepare()

    operations = {
        'rp': utils.remove_punctuation,
        'rs': utils.no_stop_words,
        'lemmatize': utils.lemmatize,
        'lemm': utils.lemmatize,
        'stem': utils.stem,
        'lowercase': utils.lowercase,
        'l': utils.lowercase,
        'spellcheck': utils.spell_check,
    }

    for operation in args.operations:
        if operation not in operations:
            raise ValueError(f"Invalid operation: {operation}")
        tokens = operations[operation](tokens, args.stop_words) if operation == 'rs' else operations[operation](tokens)

    if args.spellcheck:
        tokens = utils.spell_check(tokens)

    utils.write_to_file(tokens, args.output)
    logging.info("Finished writing to output file.")



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Process and clean PDF text',  
                                     usage='%(prog)s -f <pdf_path> -o [operations] -out <output_file>\nExample: %(prog)s -f /path/to/your/pdf -o rm l ns -out output.txt')
    parser.add_argument('-f', type=str, required=True, help='PDF file path.')
    parser.add_argument('-o', '--operations', type=str, nargs='+', required=True, 
                        help='Operations: rp (remove punctuation), l (lowercase), rs (remove stop words), lemm (lemmatize), stem (apply stemming). Apply in the order provided.')
    parser.add_argument('-out', '--output', type=str, default='output.txt', help='Output file name.')
    parser.add_argument('-p', '--pages', type=str, nargs='+', help='Pages to extract. Can be single numbers or ranges (e.g. 0-3). If omitted, all pages will be processed.)')
    parser.add_argument('-l', '--level', type=str, default='word', choices=['word', 'sentence'], help='Level of tokenization: "word" or "sentence". If omitted, word level tokenization will be applied.')
    parser.add_argument('--stop-words', type=str , help="File path for custom stop words. If omitted, nltk stop words will be used.")
    parser.add_argument('--spellcheck', action='store_true', help="Enable spell checking. WARNING: This is a computationally intesive process and might take a while. Generally there is no need for spellchecking anyway.")
    parser.add_argument('--verbosity', type=int, default=1, choices=[1, 2, 3], help='Verbosity level for text extraction from HTML')

    args = parser.parse_args()

    if not args.f or not args.operations:
        parser.print_usage()
    else:
        logging.info("Starting Program...")
        main(args)



