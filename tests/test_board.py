import unittest
from random import randint
from model.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(8)

    def test_get_cell(self):
        row = randint(0, 7)
        col = randint(0, 7)
        self.assertEqual(self.board.get_cell(row, col), Board.EMPTY_CELL)