import pygame
import sys
from GUI import*

pygame.init()
font =pygame.font.Font(None,36)
grid=Grid()
screen=pygame.display.set_mode((grid.width,grid.height))
pygame.display.set_caption("Sudoku")
selected_cell=None
won=False
usedSolver=False
gametTime=""
startTime = time.time()
endTime=None
for row in grid.solvedBoard:
    print(row)
while True:
    pos=None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            selected_cell_x=(pos[0])//grid.cellSize
            selected_cell_y=(pos[1])//grid.cellSize
            if 0<=selected_cell_x<9 and 0<=selected_cell_y<9 and grid.cells[selected_cell_y][selected_cell_x].changeable:
                selected_cell = grid.cells[selected_cell_y][selected_cell_x]
                selected_cell.highlightCell(screen,grid.cellSize,BLUE)
        elif event.type == pygame.KEYDOWN and selected_cell is not None:
            if event.unicode.isdigit() and 1<= int(event.unicode) <= 9:
                selected_cell.value=int(event.unicode)
                selected_cell=None
                won = grid.checkWin()
                if won :
                    seconds=endTime%60
                    minutes=endTime//60
                    gametTime = f"{minutes} minutes and {seconds} seconds"
            if event.key == pygame.K_SPACE:
                usedSolver=True

    screen.fill(WHITE)
    grid.drawLines(screen)
    grid.drawNumbers(screen)
    endTime=grid.drawTime(startTime,screen)
    if selected_cell is not None:
        selected_cell.highlightCell(screen,grid.cellSize,BLUE)
    if won:
        grid.displayWin(screen,font,gametTime)
    if usedSolver:
        for row in grid.cells :
            grid.solveWithAnimation(screen,row)
        break
    pygame.display.update()