# Problem disc: https://leetcode.com/problems/valid-sudoku/

def solve(board):
    n = 9
    row = [set() for _ in range(n)]
    colm = [set() for _ in range(n)]
    subBox = [set() for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                indx = (i//3)*3 + (j//3)
                num = board[i][j]
                if num in row[i] or num in colm[j] or num in subBox[indx]:
                    return False
                else:
                    row[i].add(num)
                    colm[j].add(num)
                    subBox[indx].add(num)
    return True

board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'], 
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

print(solve(board))


# Using Bit Manipulation
def solve(board):
    n = 9
    row = [0]*n
    colm = [0]*n
    subBox = [0]*n

    for i in range(n):
        for j in range(n):
            if board[i][j] != '.':
                indx = (i//3)*3 + j//3
                pos = int(board[i][j]) - 1
                if (row[i] & 1 << pos) or (colm[j] & 1 << pos) or (subBox[indx] & 1 << pos):
                    return False
                else:
                    row[i] |= 1 << pos
                    colm[j] |= 1 << pos
                    subBox[indx] |= 1 << pos
    return True

print(solve(board))