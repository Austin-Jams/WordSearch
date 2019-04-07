import unittest
import sys
import os
from search import create_board


class TestBoardCreation(unittest.TestCase):


    def test_board_creation(self):
        path = "TestData\createBoardTest.txt"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file = os.path.join(dir_path, path)
        opened_file = open(file)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        self.assertEqual(board, create_board(opened_file))




if __name__ == '__main__':
    unittest.main()