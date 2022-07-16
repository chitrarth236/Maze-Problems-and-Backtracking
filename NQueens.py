def create_board(n):
    board = []
    for i in range(n):
        s = ''
        for x in range(n):
            s =  s + '.'
        board.append(s)
    return board

def display(board):
    for row in board:
        print(row)

def isSafe(board, row, col):

    #check vertically
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    #check left diag
    for i in range(1, min(row,col) + 1):
        if board[row - i][col - i] == 'Q':
            return False

    #check right diag
    for i in range(1, min(row, len(board) - col - 1) + 1):
        if board[row - i][col + i] == 'Q':
            return False

    return True

def helper(board, row):
    #base condition
    if row == len(board):
        display(board)
        print()
        return

    #new recusive calls
    for col in range(len(board)):
        if isSafe(board, row, col):
            board[row] = board[row][0:col] + 'Q' + board[row][col+1:]
            helper(board, row + 1)
            board[row] = board[row][0:col] + '.' + board[row][col+1:]

def nQueens(n):
    board = create_board(n)
    helper(board,0)

nQueens(4)