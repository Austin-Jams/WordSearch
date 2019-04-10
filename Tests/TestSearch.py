import unittest
import sys
import os
import solve

class TestSearch(unittest.TestCase):

    def test_search_right(self):
        current_position = (3,1)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "TIN"
        forward = True
        self.assertTrue(solve.search_right(current_position, board, word, forward))
        forward = False
        word = 'NIT'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (3,1)
        self.assertTrue(solve.search_right(current_position, board, word, forward))

    def test_search_down(self):
        current_position = (0, 1)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "FART"
        forward = True
        self.assertTrue(solve.search_down(current_position, board, word, forward))
        forward = False
        word = 'TRAF'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (0, 1)
        self.assertTrue(solve.search_down(current_position, board, word, forward))

    def test_search_down_right(self):
        current_position = (0,1)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "FPY"
        forward = True
        self.assertTrue(solve.search_down_right(current_position, board, word, forward))
        forward = False
        word = 'YPF'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (0, 1)
        self.assertTrue(solve.search_down_right(current_position, board, word, forward))

    def test_search_down_left(self):
        current_position = (1,3)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "AAT"
        forward = True
        self.assertTrue(solve.search_down_left(current_position, board, word, forward))
        forward = False
        word = 'TAA'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (1,3)
        self.assertTrue(solve.search_down_left(current_position, board, word, forward))

