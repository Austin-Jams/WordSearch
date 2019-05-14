import unittest
import sys
import os
import Solve

class TestSearch(unittest.TestCase):

    def test_search_right(self):
        same_first_and_last_letter = False
        current_position = (3,1)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "TIN"
        forward = True
        search_direction = "right"
        self.assertTrue(Solve.search_right(current_position, board, word, forward, same_first_and_last_letter, search_direction))
        forward = False
        word = 'NIT'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (3,1)
        self.assertTrue(Solve.search_right(current_position, board, word, forward, same_first_and_last_letter, search_direction))

    def test_search_down(self):
        same_first_and_last_letter = False
        current_position = (0, 1)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "FART"
        forward = True
        search_direction = "down"
        self.assertTrue(Solve.search_down(current_position, board, word, forward, same_first_and_last_letter, search_direction))
        forward = False
        word = 'TRAF'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (0, 1)
        self.assertTrue(Solve.search_down(current_position, board, word, forward, same_first_and_last_letter, search_direction))

    def test_search_down_right(self):
        same_first_and_last_letter = False
        search_direction = "down_right"
        current_position = (0,1)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "FPY"
        forward = True
        self.assertTrue(Solve.search_down_right(current_position, board, word, forward, same_first_and_last_letter, search_direction))
        forward = False
        word = 'YPF'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (0, 1)
        self.assertTrue(Solve.search_down_right(current_position, board, word, forward, same_first_and_last_letter, search_direction))

    def test_search_down_left(self):
        same_first_and_last_letter = False
        search_direction = "down_left"
        current_position = (1,3)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "AAT"
        forward = True
        self.assertTrue(Solve.search_down_left(current_position, board, word, forward, same_first_and_last_letter, search_direction))
        forward = False
        word = 'TAA'
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        current_position = (1,3)
        self.assertTrue(Solve.search_down_left(current_position, board, word, forward, same_first_and_last_letter, search_direction))

