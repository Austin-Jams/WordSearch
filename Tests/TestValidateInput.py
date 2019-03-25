import unittest
from search import validate_input


class TestValidateInput(unittest.TestCase):

    def test_is_argument_passed(self):
        with self.assertRaises(Exception):
            validate_input()


if __name__ == '__main__':
    unittest.main()