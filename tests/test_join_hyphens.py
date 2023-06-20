import unittest
from code.main import TextPrepare

class TestTextPrepare(unittest.TestCase):

    def setUp(self):
        self.tp = TextPrepare('dummy.pdf')  # Initialize with dummy PDF. Won't be used for this test.

    def test_join_hyphens(self):
        text = "This is a hyphen- ated word."
        expected_result = "This is a hyphenated word."

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case for hyphen at the end of the line
        text = "This is a hyphen- \n ated word."
        expected_result = "This is a hyphenated word."

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

         # Test case for hyphen at the end of the line
        text = "This is a hyphen-\n ated word."
        expected_result = "This is a hyphenated word."

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case with no hyphen
        text = "This is a word with no hyphen."
        expected_result = "This is a word with no hyphen."

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case with hyphen at the end
        text = "This is a hyphen -ated word"
        expected_result = "This is a hyphenated word"

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case with hyphen seppareted by spaces
        text = "This is a hyphen -\nated word"
        expected_result = "This is a hyphenated word"

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case with hyphen seppareted by spaces
        text = "This is a hyphen - \nated word"
        expected_result = "This is a hyphenated word"

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case with hyphen seppareted by spaces
        text = "This is a hyphen - ated word"
        expected_result = "This is a hyphenated word"

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case for hyphen followed by newline, space and a word
        text = "This is a hyphen-\n ated word."
        expected_result = "This is a hyphenated word."

        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

        # Test case for hyphen between digits
        text = "The score was 4-3."
        expected_result = "The score was 4-3."


        # Ensure the function behaves as expected
        self.assertEqual(self.tp.join_hyphens(text), expected_result)

if __name__ == '__main__':
    unittest.main()