from typing import List
import random
import time

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

def generate(n):
    board= [[0 for i in range(n)] for j in range(n)]
    solve(board)
    return board

def empytCells(board):
    n=len(board)
    filled_cells=random.randint(15,20)
    for i in range ((n*n)-filled_cells):
        row = random.randint(0,n-1)
        col = random.randint(0,n-1)
        board[row][col]=0
    return board




board = empytCells(generate(9))
for row in board:
    print(row)
time.sleep(1)
print(" ")
print("Waiting for Solution...")
print(" ")
time.sleep(2)
print("Solution:")
board=solve(board)
for row in board:
    print(row)
