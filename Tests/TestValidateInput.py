import unittest
import sys
from search import validate_input


class TestValidateInput(unittest.TestCase):

    def test_is_argument_passed(self):
        with self.assertRaises(Exception):
            validate_input()

    def test_input_data_type(self):
        sys.argv.append(7)
        with self.assertRaises(Exception):
            validate_input()

    def test_one_argument_limit(self):
        sys.argv.append("red")
        sys.argv.append("yellow")
        with self.assertRaises(Exception):
            validate_input()


if __name__ == '__main__':
    unittest.main()