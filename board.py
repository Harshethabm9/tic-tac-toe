#creating a board on console to play
def printBoard(board):
    horizontal_line = "+---+---+---+"
    for i, row in enumerate(board):
        print(horizontal_line)
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
    print(horizontal_line)

def createBoard():
    return [[" " for _ in range(3)] for _ in range(3)]

def checkWinner(board, player):
    # Checking rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def isBoardFull(board):
    # Checking if the board is full or not
    return all(board[i][j] != " " for i in range(3) for j in range(3))
