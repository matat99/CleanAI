import unittest
from code.main import TextPrepare

class TestTextPrepare(unittest.TestCase):

    def setUp(self):
        self.tp = TextPrepare('dummy.pdf')  # Initialize with dummy PDF. Won't be used for this test.

    def test_expand_contractions(self):
        test_cases = {
            "I'm going to the park.": "I am going to the park.",
            "You're a good person.": "You are a good person.",
            "We've been here before.": "We have been here before.",
            "They'll win the game.": "They will win the game.",
            "Isn't this great?": "Is not this great?",
            "He'd like to go.": "He would like to go.",
            "There's no contraction here.": "There is no contraction here.",
            "I don't think so.": "I do not think so.",
            "It's a great day.": "It is a great day."
        }

        for text, expected_result in test_cases.items():
            # Ensure the function behaves as expected
            self.assertEqual(self.tp.expand_contractions(text), expected_result)

if __name__ == '__main__':
    unittest.main()
