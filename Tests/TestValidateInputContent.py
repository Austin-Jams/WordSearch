import unittest
import sys
import os
from search import validate_input_content, validate_key_words, validate_board


class TestValidateInputContent(unittest.TestCase):

    def test_validate_board(self):
        path = "TestData\goodData1.txt"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(dir_path, path)
        opened_file = open(file)
        self.assertTrue(validate_board(opened_file), True)
        opened_file.close()


    def test_validate_key_words(self):
        self.assertFalse(validate_key_words(""))
        self.assertFalse(validate_key_words("32424234,sdfdsf,dsfsdf,sdfsf"))
        self.assertFalse(validate_key_words("sdfsdfsdf,fdgfdgfdg,sgfdsgdfg,d"))
        self.assertTrue(validate_key_words("BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA"))


if __name__ == "__main__":
    unittest.main()