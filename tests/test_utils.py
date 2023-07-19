# tests/test_utils.py

import sys
sys.path.append("..")  # Adds the project directory (one level up) to the python path

import pytest
from CleanAI.code import utils

# def test_remove_punctuation_no_punctuation():
#     text = "Hello World"
#     expected = "Hello World"
#     assert utils.remove_punctuation(text) == expected

def test_remove_punctuation_all_punctuation():
    text = "!!@@##$$%%^^&&**()__++==--'';;::,,..//??<<>>``~~||"
    expected = ''
    assert utils.remove_punctuation(text) == expected

# def test_remove_punctuation_mixed():
#     text = "Hello, World! How's it going?"
#     expected = "Hello World How s it going"
#     assert utils.remove_punctuation(text) == expected

# def test_remove_punctuation_empty_string():
#     text = ""
#     expected = ""
#     assert utils.remove_punctuation(text) == expected
