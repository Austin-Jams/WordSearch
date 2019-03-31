import unittest
import sys
from search import validate_input_content, validate_key_words


class TestValidateInputContent(unittest.TestCase):


    def test_validate_key_words(self):
        self.assertFalse(validate_key_words(""))
        self.assertFalse(validate_key_words("32424234,sdfdsf,dsfsdf,sdfsf"))
        self.assertFalse(validate_key_words("sdfsdfsdf,fdgfdgfdg,sgfdsgdfg,d"))
        self.assertTrue(validate_key_words("BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA"))


if __name__ == "__main__":
    unittest.main()