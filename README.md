# CleanAI

CleanAI is a Python-based, open-source tool that simplifies and automates the data preprocessing steps in Natural Language Processing (NLP) and Machine Learning (ML) workflows. From extracting text from PDF files to tokenizing, normalizing, and lemmatizing text, CleanAI aims to streamline the often-tedious task of data cleaning, enabling users to focus on building and refining their models. With an emphasis on user-friendliness and versatility, CleanAI is designed to support a wide range of NLP and ML applications, regardless of the user's level of technical expertise.

**The Project is in very early stages at the moment**

****
## Motivation

The goal is to make AI training more accessible. It is important that everyone
who is interested in the topic gets to utilise it to its full potential. Especially in a time where interest in AI technologies and capabilities is at an all time high. This tool can also be used by professionals who want to simplify and streamline the process of data cleaning for their models.

For now this is only a personal project but I will continue to make improvments to the code
to the best of my abilities whenever I have time. **I'm in no way a professional when it comes to coding or machine learning!** (which is one of the reasons I decided to pick up this project) So if you have any recomendations for cleaner code or better optimisation please feel free to fork this repository and I'll try to review any pull request.

****
# Installation 

### Prerequisites

- Python 3: CleanAI requires Python 3.6 or newer. You can check your Python version by running `python --version` in your terminal/command prompt. If you don't have Python installed or have an older version, you can download the latest version from the official Python website.
- pip: The Python package installer pip is usually installed with Python. You can check its availability by running `pip --version` in your terminal/command prompt. If pip is not installed, follow the instructions on pip's installation page.

### Steps
1. Clone the repository: 
    Open your terminal/command prompt and navigate to the directory where you want to store the project. Then, clone the repository with the following command:
    `git clone https://github.com/matat99/CleanAI`
2. Navigate to the cloned directory:
    Change your current directory to the CleanAI directory:
    `cd CleanAI`
3. Install necessary packages:
    CleanAI requires several Python libraries. These libraries are listed in the `requirements.txt` file. You can install them all at once using `pip`:
    `pip3 install -r requirements.txt`
    if you encounter permission errors, try using the `--user` flag:
    `pip3 install --user -r requirements.txt.txt`

If you prefer to keep your workspace clean, consider using a virtual environment.

Now, CleanAI should be ready to use!

### Virtual Environment (Optional)
If you want to keep CleanAI and its dependencies separate from your other Python projects, you can create a virtual environment. Here's how to do it:
1. Install the `virtualenv` package:
    `pip3 install virtualenv`
2. Create a virtual environment in your project directory:
   `cd CleanAI`
    `virtualenv venv`
3. Activate your environment:
    - On Unix:
    `source venv/bin/activate`
    - On Windows:
    `.\venv\Scripts\activate`
4. Now you can install the requirements as before:
    `pip3 install -r requirements.txt`

**To exit the virtual environment when you're done, just type deactivate in your terminal/command prompt.**
***

# To Do (short-term)

 - [x] make sure the text is stored appropriately for further cleaning. 
 - [x] Tokenazation of the text
 - [x] Removal of punctuation
 - [x] Normalization (lowercase) of the text
 - [x] Stop Word Removal
 - [x] Join Hyphens
 - [x] Stemming/Lemmatization
 - [ ] Spell Check
 - [ ] Text Encoding 
 - [ ] Training and test sets division
 - [ ] Make the README nicer
 - [ ] Add different flags for each cleaning function for a better CLI experience and terminal interactivity
 - [ ] ...

 # To Do (long-term)

 - [ ] Add a GUI
 - [ ] Template a flow of cleaning steps for most common NLP models
 - [ ] Multithreading
 - [ ] ...

## License 

Distributed under the MIT License. See 'LICENSE' for more information.