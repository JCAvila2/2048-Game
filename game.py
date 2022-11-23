import random
import keyboard
import os
import time
import math


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

  
def generate_random_grid(grid):
    counter = 0
    while counter < 2:
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
    print("Moving up")
    new_grid = grid
    for columns in range(4):
        rows = 0
        column_ready = False
        while column_ready == False:
            if new_grid[rows][columns] == None and new_grid[rows + 1][columns] != None and rows + 1 <= 3:
                new_grid[rows][columns] = new_grid[rows + 1][columns]
                new_grid[rows + 1][columns] = None
            rows += 1
            if rows == 3:
                column_ready = True
                for j in range(3):
                    if new_grid[j][columns] == None and new_grid[j + 1][columns] != None:
                        column_ready = False
                        rows = 0
                        break
                    elif new_grid[j][columns] != None and new_grid[j][columns] == new_grid[j - 1][columns]:
                        if new_grid[j + 1][columns] != None:
                            new_grid[j][columns] = new_grid[j + 1][columns]
                            new_grid[j + 1][columns] = None
                        else:
                            new_grid[j][columns] = None
                        new_grid[j - 1][columns] *= 2
                        new_grid[j - 1][columns] += 0.1
    for r in range(4):
        for c in range(4):
            if new_grid[r][c] != None:
                new_grid[r][c] = math.floor(new_grid[r][c])

    return new_grid


def move_down(grid):
    print("Moving Down")
    new_grid = grid
    for columns in range(4):
        rows = 3
        column_ready = False
        while column_ready == False:
            if new_grid[rows][columns] == None and new_grid[rows-1][columns] != None and rows-1 >= 0:
                new_grid[rows][columns] = new_grid[rows-1][columns]
                new_grid[rows-1][columns] = None
            rows -= 1
            if rows == -1:
                column_ready = True
                for i in range(3):
                    if new_grid[i][columns] != None and new_grid[i + 1][columns] == None:
                        column_ready = False
                        rows = 3
                        break
                    elif new_grid[i][columns] != None and new_grid[i][columns] == new_grid[i + 1][columns]:
                        new_grid[i][columns] = None
                        new_grid[i + 1][columns] *= 2
                        break
    return new_grid


def move_left(grid):
    print("Moving left")
    return grid


def move_right(grid):
    print("Moving right")
    return grid



grid = generate_random_grid(grid)


while keyboard.is_pressed("q") == False:
    os.system("cls")
    print_grid(grid)

    user_input = input("Move (a, w, s, d):")
    if user_input == "q":
        print("Bye...")
        break
    elif user_input == "w":
        grid = move_up(grid)

    elif user_input == "s":
        grid = move_down(grid)
    
    elif user_input == "a":
        move_left(grid) 
    elif user_input == "d":
        move_right(grid) 
    
    time.sleep(1)