import random
import pygame
import time
from Solver import solve

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
class Cell:
    def __init__(self,value,row,col):
        self.value=value
        self.changeable = self.value==0
        self.row=row
        self.col=col
    
    def setValue(self,value):
        self.value=value

    def highlightCell(self,screen,cellSize,color):
        pygame.draw.rect(screen,color,(self.col*cellSize+25+(cellSize//10),self.row*cellSize+25+(cellSize//10),cellSize-2*(cellSize//10),cellSize-2*(cellSize//10)),2)
    def clearCell(self,screen,cellSize):
        pygame.draw.rect(screen,WHITE,(self.col*cellSize+25+(cellSize//10),self.row*cellSize+25+(cellSize//10),cellSize-2*(cellSize//10),cellSize-2*(cellSize//10)))
class Grid:
    def __init__(self):
        self.board = self.empytCells(self.generate(9))
        self.width = 600
        self.height = 650
        self.usableWidth = 550
        self.usableHeight = 550
        self.cellSize = self.usableWidth//9
        self.offset = self.cellSize//2
        self.cells=[[Cell(self.board[i][j],i,j)for j in range(9)]for i in range(9)]
        self.solvedBoard=solve(self.board)

    def generate(self,n):
        board= [[0 for i in range(n)] for j in range(n)]
        solve(board)
        return board
    
    def empytCells(self,board):
        n=len(board)
        filled_cells=random.randint(15,20)
        for i in range ((n*n)-filled_cells):
            row = random.randint(0,n-1)
            col = random.randint(0,n-1)
            board[row][col]=0
        return board
    
    def drawLines(self,screen):
        color=BLACK
        for i in range(0,10):
            if i%3==0:
                color=BLACK
            else:
                color=GRAY
            if color==BLACK:
                pygame.draw.line(screen,color,(25,i*self.cellSize+25),(self.usableWidth+25,i*self.cellSize+25),2)
                pygame.draw.line(screen,color,(i*self.cellSize+25,25),(i*self.cellSize+25,self.usableHeight+25),2)
            else:
                pygame.draw.line(screen,color,(25,i*self.cellSize+25),(self.usableWidth+25,i*self.cellSize+25))
                pygame.draw.line(screen,color,(i*self.cellSize+25,25),(i*self.cellSize+25,self.usableHeight+25))

    def drawNumbers(self,screen):
        font =pygame.font.Font(None,42)
        for i in range(9):
            for j in range(9):
                if self.cells[i][j].value!=0:
                    if self.cells[i][j].changeable==True:
                        color = GRAY
                    else:
                        color= BLACK
                    num = font.render(str(self.cells[i][j].value),True,color)
                    cell_center_x=j*self.cellSize+self.offset+25
                    cell_center_y=i*self.cellSize+self.offset+25
                    num_rect=num.get_rect(center=(cell_center_x,cell_center_y))
                    screen.blit(num,num_rect.topleft)
    def drawChangedNumber(self,screen,cell):
        font =pygame.font.Font(None,42)
        num = font.render(str(cell.value),True,GRAY)
        cell_center_x=cell.col*self.cellSize+self.offset+25
        cell_center_y=cell.row*self.cellSize+self.offset+25
        num_rect=num.get_rect(center=(cell_center_x,cell_center_y))
        screen.blit(num,num_rect.topleft)

    def drawTime(self,startTime,screen):
        font =pygame.font.Font(None,42)
        elapsedTime=int(time.time()-startTime)
        minutes = elapsedTime // 60
        seconds = elapsedTime%60
        text = font.render("{:02d}:{:02d}".format(minutes,seconds),True,BLACK)
        textRect=text.get_rect(center=(self.width//2,(self.height+(self.usableHeight+25))//2))
        screen.blit(text,textRect.topleft)
        return elapsedTime



    def checkWin(self):
        playerBoard = [[cell.value for cell in row] for row in self.cells]
        return playerBoard == self.solvedBoard
    
    def solveWithAnimation(self,screen,row):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        clock = pygame.time.Clock()
        for cell in row:
                if cell.changeable:
                    if cell.value == self.solvedBoard[cell.row][cell.col]:
                        cell.highlightCell(screen,self.cellSize,GREEN)
                    else:
                        cell.highlightCell(screen,self.cellSize,RED)
                        pygame.display.update()
                        pygame.time.wait(800)
                        cell.clearCell(screen,self.cellSize)
                        cell.value= self.solvedBoard[cell.row][cell.col]
                        self.drawChangedNumber(screen,cell)
                        cell.highlightCell(screen,self.cellSize,GREEN)
                pygame.display.update()
                clock.tick(2)
    def displayWin(self,screen,font,gameTime):
        screen.fill(WHITE)
        winMessage="You Won!"
        timeMessage="You completed the game in: "
        winText=font.render(winMessage,True,BLACK)
        completeText=font.render(timeMessage,True,BLACK)
        timeText=font.render(gameTime,True,BLACK)
        completeRect=completeText.get_rect(center=(self.width//2,(self.height//2)))
        winRect=winText.get_rect(center=(self.width//2,(self.height//2)-completeRect.height))
        timeRect=timeText.get_rect(center=(self.width//2,(self.height//2)+completeRect.height))
        screen.blit(winText,winRect.topleft)
        screen.blit(completeText,completeRect.topleft)
        screen.blit(timeText,timeRect.topleft)