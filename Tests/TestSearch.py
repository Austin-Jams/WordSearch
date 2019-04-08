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
        current_position = (3,3)
        self.assertTrue(solve.search_right(current_position, board, word, forward))

    def test_search_up(self):
        return 1

    def test_search_down(self):
        return 1

    def test_search_left(self):
        return 1

    def test_search_up_right(self):
        return 1

    def test_search_down_right(self):
        return 1

    def test_search_down_left(self):
        return 1

    def test_search_up_left(self):
        return 1