
#make plarye etci
EMPTY = ' '
WHITE_PIECE='w'
WHITE_KING= 'W'
BLACK_PIECE= 'b'
BLACK_KING='B'

def create_board():
    board = [[EMPTY for _ in range(8)] for _ in range(8)]
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 != 0:
                board[row][col] = WHITE_PIECE
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 != 0:
                board[row][col] = BLACK_PIECE
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))
        print('-' * 15)


def main():
    board= create_board()
    print_board(board)


if __name__=="__main__":
    main()
#get list offor valid moves
#player_move
# check for win





