"""
https://leetcode.com/problems/valid-sudoku/?envType=study-plan-v2&envId=top-interview-150


Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


solution 1:
brute force
2 find the number array need to be checked



solution 2" build the storage to store all number sitation

"""


# brutal force
def isValidSudoku(board: list[list[str]])->bool:
    # check row
    for i in range(9):
        tmp = []
        for j in range(9):
            if board[i][j].isdigit():
                if board[i][j] not in tmp:
                    tmp.append(board[i][j])
                else:
                    return False
                
    # check column
    for i in range(9):
        tmp = []
        for j in range(9):
            if board[j][i].isdigit():
                    if board[j][i] not in tmp:
                        tmp.append(board[j][i])
                    else:
                        print(tmp, board[j][i])
                        return False
            
    # check box
    for i in range(3):
        for j in range(3):
            tmp = []
            for m in range(i*3, i*3+3):
                for n in range(j*3, j*3+3):
                    if board[m][n].isdigit():
                        if board[m][n] not in tmp:
                            tmp.append(board[m][n])
                        else:
                            return False
    return True

def isValidSudoku2(board: list[list[str]])->bool:
    #build three array to record the row, col, box
    row = [[False  for _ in range(9)] for _ in range(9)]
    col = [[False  for _ in range(9)] for _ in range(9)]
    box = [[False  for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j].isdigit() :
                num = int(board[i][j]) -1
                if row[i][num] or col[j][num] or box[i//3*3+j//3][num]:
                    return False
                row[i][num] = True
                col[j][num] = True
                box[i//3*3+j//3][num] = True
            
    
    return True


testCases = [[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]], 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]]


print(int('9'))
print([ isValidSudoku(i) for i in testCases])
print([ isValidSudoku2(i) for i in testCases])