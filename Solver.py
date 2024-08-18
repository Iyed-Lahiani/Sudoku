from typing import List
import random

def solve(board):
    n=len(board)
    copy= [row for row in board]
    if backtrack(n,copy):
        return copy
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
                numbers = list(range(1, n + 1))
                random.shuffle(numbers)
                for num in numbers:
                    if isValid(row, col, num, board):
                        board[row][col] = num
                        if backtrack(n, board):
                            return True
                        board[row][col] = 0
                return False
    return True
