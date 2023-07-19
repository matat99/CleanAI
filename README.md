# CleanAI

CleanAI is a Python-based, open-source tool that simplifies and automates the data preprocessing steps in Natural Language Processing (NLP) and Machine Learning (ML) workflows. From extracting text from PDF files to tokenizing, normalizing, and lemmatizing text, CleanAI aims to streamline the often-tedious task of data cleaning, enabling users to focus on building and refining their models. With an emphasis on user-friendliness and versatility, CleanAI is designed to support a wide range of NLP and ML applications, regardless of the user's level of technical expertise.

**The Project is in very early stages at the moment**

- [Motivation](#motivation)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
  - [Virtual Environment (Optional)](#virtual-environment-optional)
- [Usage](#usage)
- [To Do (short-term)](#to-do-short-term)
- [To Do (long-term)](#to-do-long-term)
- [License](#license)


### Motivation

The goal is to make AI training more accessible. It is important that everyone who is interested in the topic gets to utilise it to its full potential. Especially in a time where interest in AI technologies and capabilities is at an all time high. This tool can also be used by professionals who want to simplify and streamline the process of data cleaning for their models.

For now this is only a personal project but I will continue to make improvements to the code to the best of my abilities whenever I have time. I'm in no way a professional when it comes to coding or machine learning! (which is one of the reasons I decided to pick up this project) So if you have any recommendations for cleaner code or better optimisation, please feel free to fork this repository and I'll try to review any pull request.
## Installation
#### Prerequisites

- **Python 3**: CleanAI requires Python 3.6 or newer. You can check your Python version by running `python --version` in your terminal/command prompt. If you don't have Python installed or have an older version, you can download the latest version from the official Python website.
- **pip**: The Python package installer pip is usually installed with Python. You can check its availability by running `pip --version` in your terminal/command prompt. If pip is not installed, follow the instructions on pip's installation page.

#### Steps

1. Clone the repository:
        Open your terminal/command prompt and navigate to the directory where you want to store the project. Then, clone the repository with the following command:
        `git clone https://github.com/matat99/CleanAI`
2. Navigate to the cloned directory:
        Change your current directory to the CleanAI directory:
        `cd CleanAI`
3. Install necessary packages:
        CleanAI requires several Python libraries. These libraries are listed in the requirements.txt file. You can install them all at once using pip:
        `pip3 install -r requirements.txt`
        if you encounter permission errors, try using the --user flag:
        `pip3 install --user -r requirements.txt.txt`

Now, CleanAI should be ready to use!

#### If you prefer to keep your workspace clean, consider using a virtual environment.

### Virtual Environment (Optional)

If you want to keep CleanAI and its dependencies separate from your other Python projects, you can create a virtual environment. Here's how to do it:

1. Install the virtualenv package:
    `pip3 install virtualenv`
2. Create a virtual environment in your project directory:
    `cd CleanAI`
    `virtualenv venv`
3. Activate your environment:
    - On Unix:
        `source venv/bin/activate`
    -On Windows:
        `.\venv\Scripts\activate`
4. Now you can install the requirements as before:
    `pip3 install -r requirements.txt`

To exit the virtual environment when you're done, just type `deactivate` in your terminal/command prompt.
## Usage

#### Basic usage: 
After completing the installation steps, you can run CleanAI from your terminal/command prompt with the following syntax:

`python main.py -f <pdf_path> -o <operations> -l <level of tokenization>-out <output_file>`

<pdf_path> should be replaced with the path to the PDF file you want to process.
<operations> should be replaced with the operations you want to apply to the text. You can list multiple operations in the order they should be applied.
<output_file> should be replaced with the name of the file you want to output the results to. If not provided, 'output.txt' will be used by default.
<level of tokenization> you can choose between two values: `word` and `sentence` to set a level of tokenization for your text. **The Value is 'word' by default**

#### Operations: 
You can choose from the following operations:

    rm: Remove punctuation.
    l: Convert text to lowercase.
    ns: Remove stop words.
    lemm: Lemmatize text.
    stem: Apply stemming.

**Operations should be provided in the order you want them to be applied, separated by spaces. For example, to remove punctuation, convert to lowercase, and then remove stop words, you would use: -o rm l ns.**

#### Example usage: 
The following command will process the file 'sample.pdf', remove punctuation, convert to lowercase, remove stop words, and output the result to 'output.txt':

`python main.py -f sample.pdf -o rm l ns -out output.txt`

For further details, you can always use the --help option to display information about how to use CleanAI.

## To Do (short-term)

<details>
    <summary>Completed</summary>

- [x] Make sure the text is stored appropriately for further cleaning.
- [x] Tokenization of the text.
- [x] Removal of punctuation.
- [x] Normalization (lowercase) of the text.
- [x] Stop Word Removal.
- [x] Join Hyphens.
- [x] Stemming/Lemmatization.
- [x] Ability to select which pdf pages you want to use
- [x] Make the README nicer.
- [x] CLI flags.
- [x] Add unit tests.
- [x] Choose your own level of tokenization (word or sentence).
- [x] Expand contractions.
- [x] Load NLTK when neaded within the function not at the start of the script.
- [x] logging.
- [x] Configurable stop-words.
- [x] Add support for HTML files
- [x] Spell Check.
- [x] Adapt for large-scale document processing by processing page by page to reduce memory usage
</details>
<details>
    <summary>To-Do</summary>

- [ ] N-gram support
- [ ] Training and test sets division.
- [ ] Comprehensive error handling.
- [ ] Support for additional file formats
- [ ] Unit Test for every function:
    - [ ] process pages
    - [ ] remove punctuation
    - [ ] lowercase
    - [ ] no_stop_words
    - [ ] stem
    - [ ] lemmatize
    - [ ] spell_check
    - [ ] write_to_file
    - [ ] expand contractions
- [ ] Expand Scope of input files 
    - [ ] CSV
    - [ ] txt
    - [ ] direct input strings
- [ ] Text Analysis
- [ ] Enhance Spellchecking
- [ ] Handling of numbers
    - [ ] ...

</details>

## To Do (long-term)

- [ ] Handling of emojis
- [ ] Text Encoding.
- [ ] Look into a more efficient stemmer (SnowballStemmer for example)
- [ ] Add a GUI or a Web Interface.
- [ ] Template a flow of cleaning steps for most common NLP models.
- [ ] Multithreading.
- [ ] Implement Docker.
- [ ] Support for additional file formats
- [ ] ...

## License

Distributed under the MIT License. See 'LICENSE' for more information.