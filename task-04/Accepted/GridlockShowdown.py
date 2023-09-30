def check_winner(board, symbol):
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or \
           all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def determine_winner(board):
    symbols = ["X", "O", "+"]
    for symbol in symbols:
        if check_winner(board, symbol):
            return symbol
    return "DRAW"

t = int(input())
for _ in range(t):
    board = [list(input().strip()) for _ in range(3)]
    winner = determine_winner(board)
    print(winner)

