import unittest
import sys
from search import validate_input_content


class TestValidateInputContent(unittest.TestCase):


    def test_validate_input_content(self):
        self.assertEqual(validate_input_content(open("TestData\goodData1.txt", "r"), True))


if __name__ == "__main__":
    unittest.main()