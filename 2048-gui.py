import pygame
import math
import random
import copy
import time


# Window variables
WIDTH = 800
HEIGHT = 600
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("2048")
font = pygame.font.Font('freesansbold.ttf', 32)



# Colors variables
WHITE = (255, 255, 255)
ORANGE = (185, 75, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

COLOR_EMPTY = (204, 192, 179)
COLOR_2 = (238, 228, 218)
COLOR_4 = (237, 224, 200)
COLOR_8 = (242, 177, 121)
COLOR_16 = (245, 149, 99)
COLOR_32 = (246, 124, 95)
COLOR_64 = (246, 94, 59)
COLOR_128 = (237, 207, 114)
COLOR_256 = (237, 204, 97)
COLOR_512 = (237, 200, 80)
COLOR_1024 = (237, 197, 63)
COLOR_2048 = (237, 194, 46)
   


# Initial Grid
grid = [
        [None, None, None, None], 
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]



# Make changes to the grid
def add_to_grid(grid, amount):
    counter = 0
    while counter < amount:
        counter += 1
        options = [2, 4]
        value = options[random.randint(0, 1)]
        v = random.randint(0, 3)
        h = random.randint(0, 3)
        if grid[v][h] == None:
            grid[v][h] = value
        else:
            counter -= 1
    return grid


def floor_grid(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c] != None:
                grid[r][c] = math.floor(grid[r][c])

    return grid



# Methods to move the grid
def move_up(grid):
    new_grid = copy.deepcopy(grid)
    for columns in range(4):
        rows = 0
        column_ready = False
        number_added_already = 0.01
        while column_ready == False:
            if new_grid[rows][columns] == None and new_grid[rows + 1][columns] != None and rows + 1 <= 3:
                new_grid[rows][columns] = new_grid[rows + 1][columns]
                new_grid[rows + 1][columns] = None
            rows += 1
            if rows == 3:
                column_ready = True
                for r in range(3):
                    if new_grid[r][columns] == None and new_grid[r + 1][columns] != None:
                        column_ready = False
                        rows = 0
                        break 
                    if new_grid[r][columns] != None and new_grid[r][columns] == new_grid[r + 1][columns]:
                        new_grid[r][columns] *= 2
                        new_grid[r][columns] += number_added_already
                        number_added_already += 0.01
                        new_grid[r + 1][columns] = None
                        column_ready = False
                        rows = 0
    """
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] != None:
                new_grid[i][j] = math.floor(new_grid[i][j])
    """
    new_grid = floor_grid(new_grid)
                
    if new_grid == grid:
        return False
    return new_grid


def move_down(grid):
    new_grid = copy.deepcopy(grid)
    for columns in range(4):
        rows = 3
        column_ready = False
        number_added_already = 0.01
        while column_ready == False:
            if new_grid[rows][columns] == None and new_grid[rows - 1][columns] != None and rows - 1 >= 0:
                new_grid[rows][columns] = new_grid[rows - 1][columns]
                new_grid[rows - 1][columns] = None
            rows -= 1
            if rows == -1:
                column_ready = True
                for k in range(3, 0, -1):
                    if new_grid[k][columns] == None and new_grid[k - 1][columns] != None:
                        column_ready = False
                        rows = 3
                        break
                    if new_grid[k][columns] != None and new_grid[k][columns] == new_grid[k - 1][columns]:
                        new_grid[k][columns] *= 2
                        new_grid[k][columns] += number_added_already
                        number_added_already += 0.01
                        new_grid[k - 1][columns] = None
                        column_ready = False
                        rows = 3    

    # floor loops
    new_grid = floor_grid(new_grid)
    
    if new_grid == grid:
        return False
    return new_grid


def move_left(grid):
    new_grid = copy.deepcopy(grid)
    for rows in range(4):
        columns = 0
        row_ready = False
        number_added_already = 0.01
        while row_ready == False:
            if new_grid[rows][columns] == None and new_grid[rows][columns + 1] != None and columns + 1 <= 3:
                new_grid[rows][columns] = new_grid[rows][columns + 1]
                new_grid[rows][columns + 1] = None
            columns += 1
            if columns == 3:
                row_ready = True
                for c in range(3):
                    if new_grid[rows][c] == None and new_grid[rows][c + 1] != None:
                        row_ready = False
                        columns = 0
                        break
                    if new_grid[rows][c] != None and new_grid[rows][c] == new_grid[rows][c + 1]:
                        new_grid[rows][c] *= 2
                        new_grid[rows][c] += number_added_already
                        number_added_already += 0.01
                        new_grid[rows][c + 1] = None

                        row_ready = False
                        columns = 0

    # floor loops
    new_grid = floor_grid(new_grid)

    if new_grid == grid:
        return False
    return new_grid


def move_right(grid):
    new_grid = copy.deepcopy(grid)
    for rows in range(4):
        columns = 3
        row_ready = False
        number_added_already = 0.01
        while row_ready == False:
            if (new_grid[rows][columns] == None) and (new_grid[rows][columns - 1] != None) and columns - 1 >= 0:
                new_grid[rows][columns] = new_grid[rows][columns - 1]
                new_grid[rows][columns - 1] = None
            columns -= 1
            if columns == 0:
                row_ready = True
                for c in range(3, 0, -1):
                    if new_grid[rows][c] == None and new_grid[rows][c - 1] != None:
                        row_ready = False
                        columns = 3
                        break
                    if new_grid[rows][c] != None and new_grid[rows][c] == new_grid[rows][c - 1]:
                        new_grid[rows][c] *= 2
                        new_grid[rows][c] += number_added_already
                        number_added_already += 0.01
                        new_grid[rows][c - 1] = None

                        row_ready = False
                        columns = 3      

    # floor loops
    new_grid = floor_grid(new_grid)

    if new_grid == grid:
        return False
    return new_grid



# Draw the board
def draw_board(grid):
    window.fill(WHITE)
    x = 45
    y = 45
    pygame.draw.rect(window, (187, 173, 160), pygame.Rect(30, 30, 500, 500))
    
    for r in range(4):
        for c in range(4):
            # Draw the number on each box
            if grid[r][c] != None:
                # Choose the background color based on the number in the space
                if grid[r][c] == 2:
                    pygame.draw.rect(window, COLOR_2, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 4:
                    pygame.draw.rect(window, COLOR_4, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 8:
                    pygame.draw.rect(window, COLOR_8, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 16:
                    pygame.draw.rect(window, COLOR_16, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 32:
                    pygame.draw.rect(window, COLOR_32, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 64:
                    pygame.draw.rect(window, COLOR_64, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 128:
                    pygame.draw.rect(window, COLOR_128, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 256:
                    pygame.draw.rect(window, COLOR_256, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 512:
                    pygame.draw.rect(window, COLOR_512, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 1024:
                    pygame.draw.rect(window, COLOR_1024, pygame.Rect(x, y, 100, 100))
                elif grid[r][c] == 2048:
                    pygame.draw.rect(window, COLOR_2048, pygame.Rect(x, y, 100, 100))
                else:
                    pygame.draw.rect(window, (0, 0, 255), pygame.Rect(x, y, 100, 100))
                text = font.render(str(grid[r][c]), True, BLACK)
            else:
                pygame.draw.rect(window, COLOR_EMPTY, pygame.Rect(x, y, 100, 100))
                text = font.render("", True, BLACK)

            textRect = text.get_rect()
            textRect.center = (x + 100 // 2, y + 100 // 2)
            window.blit(text, textRect)
            
            x += 120
        y += 120
        x = 45



grid = add_to_grid(grid, 2)
run = True
while run:
    draw_board(grid)

    if move_up(grid) == False and move_down(grid) == False and move_left(grid) == False and move_right(grid) == False:
        print("Game Over D:")
        time.sleep(1)
        window.fill(RED)
        pygame.display.update()
        time.sleep(3)
        run = False
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_grid = move_up(grid)
                if new_grid:
                    print("Moving UP")
                    grid = new_grid    
                    grid = add_to_grid(grid, 1)

            if event.key == pygame.K_DOWN:
                new_grid = move_down(grid)
                if new_grid:
                    print("Moving Down")
                    grid = new_grid    
                    grid = add_to_grid(grid, 1)
                    
            if event.key == pygame.K_LEFT:
                new_grid = move_left(grid)
                if new_grid:
                    print("Moving Left")
                    grid = new_grid    
                    grid = add_to_grid(grid, 1)

            if event.key == pygame.K_RIGHT:
                new_grid = move_right(grid)
                if new_grid:
                    print("Moving Right")
                    grid = new_grid    
                    grid = add_to_grid(grid, 1)

    pygame.display.update()
    clock.tick(60)
        
pygame.quit()
quit()
