import unittest 
from checkers import create_board, EMPTY, WHITE_PIECE, BLACK_PIECE

class TestCheckers(unittest.TestCase):
    
    def test_board_dimensions(self):
        board=create_board()
        self.assertEqual(len(board), 8)
        self.assertTrue(all(len(row) == 8 for row in board))
               
        #test initial position of white pieces
    def test_white_initial_positions(self):
        board=create_board()
        #white pieces
        for row in range(3):
            for col in range(8):
                if(row +col) % 2 !=0:
                    self.assertEqual(board[row][col], WHITE_PIECE)
                else:
                    self.assertEqual(board[row][col], EMPTY)
        #black pieces
    def test_black_initial_positions(self):
        board = create_board()
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 != 0:  # Check if sum of row and col is odd
                    self.assertEqual(board[row][col], BLACK_PIECE)
                else:
                    self.assertEqual(board[row][col], EMPTY)
    #     #middle pieces
    def test_middle_rows_empty(self):
        board = create_board()
        # Test middle rows are empty
        for row in range(3, 5):
            for col in range(8):
                self.assertEqual(board[row][col], EMPTY)

if __name__ == '__main__':
    unittest.main()
        
        