from typing import List

def solve(board:List[List[int]]):
    n=len(board)
    if backtrack(n,board):
        return board
    return None
    
    
    
def isValid(row,col,num,board):
        for i in range(len(board)):
            if board[row][i]==num or board[i][col]==num:
                return False
        starRow = 3*(row//3)
        startCol = 3*(col//3)
        for i in range(3):
            for j in range(3):
                if(board[starRow+i][startCol+j]==num):
                    return False
        return True
def backtrack(n,board):
        for row in range(n):
            for col in range(n):
                if board[row][col] == 0:
                    for num in range(1, n + 1):
                        if isValid(row,col,num,board):
                            board[row][col] = num
                            if backtrack(n,board):
                                return True
                            board[row][col] = 0
                    return False
                
        return True

example = [[0,0,0,0,0,0,8,0,0],
           [0,6,0,0,0,0,0,1,2],
           [8,7,1,9,0,2,0,0,0],
           [4,5,0,0,6,0,0,3,9],
           [3,1,6,5,0,0,2,7,0],
           [0,2,0,3,4,0,0,0,0],
           [0,9,0,1,0,5,4,8,3],
           [5,0,0,0,8,0,7,0,1],
           [0,0,0,0,0,0,0,6,0]]
solvedBoard = solve(example)
if solvedBoard!=None:
    for solvedRow in solvedBoard:
        print(solvedRow)
else:
    print("No Solution")