

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 5)



def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    
    return False

def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("Cell already taken, choose another one.")
        except (ValueError, IndexError):
            print("Invalid input, please enter numbers between 0 and 2.")


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()