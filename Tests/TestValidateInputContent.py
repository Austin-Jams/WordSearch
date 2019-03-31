import unittest
import sys
from search import validate_input_content, validate_key_words


class TestValidateInputContent(unittest.TestCase):


    def test_validate_input_content(self):
        self.assertEqual(validate_input_content(open("TestData\goodData1.txt", "r"), True))


    def test_validate_key_words(self):
        self.assertTrue(validate_key_words("BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA"))


if __name__ == "__main__":
    unittest.main()