import unittest
import sys
import os
from solve import search_down,search_down_left,search_left,search_up,search_down_right,search_right,search_up_left,search_up_right
class TestSearch(unittest.TestCase):

    def test_search_right(self):
        current_position = (3,1)
        board = [['D', 'F', 'G', 'R'], ['L', 'A', 'P', 'A'], ['O', 'R', 'A', 'Y'], ['R', 'T', 'I', 'N']]
        word = "TIN"
        forward = True
        self.assertTrue(search_right(current_position,board,word,forward))

    def test_search_up(self):

    def test_search_down(self):

    def test_search_left(self):

    def test_search_up_right(self):

    def test_search_down_right(self):

    def test_search_down_left(self):

    def test_search_up_left(self):