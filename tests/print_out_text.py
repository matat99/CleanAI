from code.main import TextPrepare

def print_extracted_text(pdf_path):
    tp = TextPrepare(pdf_path)
    extracted_text = tp.text_extract()
    print(extracted_text)

if __name__ == "__main__":
    print_extracted_text('../example/fomcminutes20230201.pdf')