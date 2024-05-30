
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

def get_move_directions(piece):
    if piece in [WHITE_PIECE, BLACK_PIECE]:
        return [(-1, -1), (-1, 1)] if piece == WHITE_PIECE else [(1, -1), (1, 1)]
    elif piece in [WHITE_KING, BLACK_KING]:
        return [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    else:
        return []

def get_normal_moves(board, row, col, directions):
    moves= []
    for delta_row, delta_column in directions:
        new_row, new_col = row + delta_row, col+ delta_column
    if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row][new_col] == EMPTY:
            moves.append((new_row, new_col))
    return moves   

def get_capturing_moves(board, row, col, piece, directions):
    moves = []
    for delta_row, delta_column in directions:
        capture_row, capture_column = delta_row * 2, delta_column * 2
        new_row, new_col = row + capture_row, col + capture_column
        if 0 <= new_row < 8 and 0 <= new_col < 8 and board[new_row][new_col] == EMPTY:
            mid_row, mid_col = row + delta_row, col + delta_column
            if board[mid_row][mid_col] != EMPTY and board[mid_row][mid_col].lower() != piece.lower():
                moves.append((new_row, new_col))
    return moves

def get_valid_moves(board, row, col):
    piece = board[row][col]
    directions = get_move_directions(piece)
    if not directions:
        return []

    normal_moves = get_normal_moves(board, row, col, directions)
    capturing_moves = get_capturing_moves(board, row, col, piece, directions)
    
    return normal_moves + capturing_moves

# def get_valid_moves(board, row, col):
#     moves = []
#     piece = board[row][col]
#     if piece in [WHITE_PIECE, BLACK_PIECE]:
#         directions=[(-1,-1), (-1,1)] if piece == WHITE_PIECE else [(1,-1), (1,1)]
#     elif piece in [WHITE_KING, BLACK_KING]:
#         directions= [(-1,-1), (-1,1),(1,-1,),(1,1)]
#     else: 
#         return moves #emptys space =empty list
        
#     # Normal moves
#     for direction in directions:
#         delta_row, delta_column =direction
#         r, c = row + delta_row , col + delta_column
#         if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == EMPTY:
#             moves.append((r, c))
#     # Captures
#     for direction in directions:
#         delta_row, delta_column = direction[0] * 2, direction[1] *2
#         r, c = row + delta_row, col + delta_column
#         if 0 <= r < 8 and 0 <= c < 8 and board[r][c] == EMPTY:
#             mid_r, mid_c = row + delta_row // 2, col + delta_column // 2
#             if board[mid_r][mid_c] != EMPTY and board[mid_r][mid_c].lower() != piece.lower():
#                 moves.append((r, c))
#     return moves

# def get_all_valid_moves(board, player):
#     valid_moves = {}
#     for row in range(8):
#         for col in range(8):
#             if board[row][col].lower() == player:
#                 moves = get_valid_moves(board, row, col)
#                 if moves:
#                     valid_moves[(row, col)] = moves
#     return valid_moves

# def execute_move(board, start_pos, end_pos):
#     start_row, start_col = start_pos
#     end_row, end_col = end_pos
#     board[end_row][end_col] = board[start_row][start_col]
#     board[start_row][start_col] = EMPTY
#     # Check if a capture was made
#     if abs(end_row - start_row) == 2:
#         mid_row = (start_row + end_row) // 2
#         mid_col = (start_col + end_col) // 2
#         board[mid_row][mid_col] = EMPTY
#     # Promote to king
#     if end_row == 0 and board[end_row][end_col] == WHITE_PIECE:
#         board[end_row][end_col] = WHITE_KING
#     elif end_row == 7 and board[end_row][end_col] == BLACK_PIECE:
#         board[end_row][end_col] = BLACK_KING

# def check_end_game(board):
#     white_pieces = sum(row.count(WHITE_PIECE) + row.count(WHITE_KING) for row in board)
#     black_pieces = sum(row.count(BLACK_PIECE) + row.count(BLACK_KING) for row in board)
#     if white_pieces == 0 or black_pieces == 0:
#         return True
#     for row in range(8):
#         for col in range(8):
#             if board[row][col] != EMPTY and get_valid_moves(board, row, col):
#                 return False
#     return True

# def player_move(board, player):
#     while True:
#         try:
#             start_row = int(input(f"Player {player}, enter start row (0-7): "))
#             start_col = int(input(f"Player {player}, enter start column (0-7): "))
#             end_row = int(input(f"Player {player}, enter end row (0-7): "))
#             end_col = int(input(f"Player {player}, enter end column (0-7): "))
            
#             if (start_row, start_col) in get_all_valid_moves(board, player) and (end_row, end_col) in get_all_valid_moves(board, player)[(start_row, start_col)]:
#                 execute_move(board, (start_row, start_col), (end_row, end_col))
#                 break
#             else:
#                 print("Invalid move. Try again.")
#         except (ValueError, IndexError):
#             print("Invalid input. Please enter numbers between 0 and 7.")

# def main():
#     board = create_board()
#     current_player = WHITE_PIECE
    
#     while True:
#         print_board(board)
#         player_move(board, current_player)
        
#         if check_end_game(board):
#             print_board(board)
#             print(f"Player {current_player.upper()} wins!")
#             break
        
#         current_player = 'b' if current_player == 'w' else 'w'


#tester_main
def main():
    board= create_board()
    print_board(board)


if __name__=="__main__":
    main()
#get list offor valid moves
#player_move
# check for win





