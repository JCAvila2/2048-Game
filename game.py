import random
import keyboard
import os
import math
import copy


grid = [
        [None, None, None, None], 
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None]
    ]


def print_grid(grid):
    for v in range(4):
        actual_horizontal_line = ""
        for h in range(4):
            if grid[v][h] == None:
                actual_horizontal_line += " * "
            else:
                actual_horizontal_line += " " + str(grid[v][h]) + " "
        print(actual_horizontal_line)

  
def generate_random_grid(grid, amount):
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
                        


# methods to move the grid
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
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] != None:
                new_grid[i][j] = math.floor(new_grid[i][j])

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
    for i in range(4):
        for j in range(4):
            if new_grid[i][j] != None:
                new_grid[i][j] = math.floor(new_grid[i][j])

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

    for i in range(4):
        for j in range(4):
            if new_grid[i][j] != None:
                new_grid[i][j] = math.floor(new_grid[i][j])

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

    for i in range(4):
        for j in range(4):
            if new_grid[i][j] != None:
                new_grid[i][j] = math.floor(new_grid[i][j])

    if new_grid == grid:
        return False
    return new_grid



grid = generate_random_grid(grid, 2)


while True:
    #os.system("cls")
    print_grid(grid)
    if move_up(grid) or move_down(grid) or move_left(grid) or move_right(grid):
        user_input = input("Move (a, w, s, d):")
        if user_input == "q":
            print("Bye...")
            break    
        elif user_input == "w":
            new_grid = move_up(grid)
            if new_grid:
                grid = new_grid    
                grid = generate_random_grid(grid, 1)
        
        elif user_input == "s":
            new_grid = move_down(grid)
            if new_grid:
                grid = new_grid    
                grid = generate_random_grid(grid, 1)
        
        elif user_input == "a":
            new_grid = move_left(grid)
            if new_grid:
                grid = new_grid    
                grid = generate_random_grid(grid, 1)
        
        elif user_input == "d":
            new_grid = move_right(grid)
            if new_grid:
                grid = new_grid    
                grid = generate_random_grid(grid, 1)
        
        print("=" * 100)
    else:
        print("Game Over D:")
        break
