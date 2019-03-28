import unittest
import sys
from search import validate_input, is_text_file, does_path_exist


class TestValidateInput(unittest.TestCase):

    def test_is_argument_passed(self):
        sys.argv[1] = "TestData/goodData1.txt"
        with self.assertRaises(Exception):
            validate_input()

    def test_input_data_type(self):
        sys.argv.append(7)
        with self.assertRaises(Exception):
            validate_input()

    def test_is_txt_file(self):
        path = "TestData/goodData1.txt"
        self.assertTrue(is_text_file(path))
        path = "ksdbfkdsj.com"
        with self.assertRaises(Exception):
            is_text_file(path)

    def test_to_see_if_the_path_exists(self):
        path = "TestData/goodData1.txt"
        self.assertTrue(does_path_exist(path))
        path = "TestData/badData22.txt"
        with self.assertRaises(Exception):
            does_path_exist(path)



if __name__ == '__main__':
    unittest.main()
