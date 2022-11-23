import random
import keyboard
import os
import time


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
    return new_grid


def move_down(grid):
    print("Moving Down")
    new_grid = grid
    for columnas in range(4):
        filas = 3
        columna_completa = False
        while columna_completa == False:
            if new_grid[filas][columnas] == None and new_grid[filas-1][columnas] != None and filas-1 >= 0:
                new_grid[filas][columnas] = new_grid[filas-1][columnas]
                new_grid[filas-1][columnas] = None
            filas -= 1
            if filas == -1:
                columna_completa = True
                for i in range(3):
                    if new_grid[i][columnas] != None and new_grid[i + 1][columnas] == None:
                        columna_completa = False
                        filas = 3
                        break
                    elif new_grid[i][columnas] != None and new_grid[i][columnas] == new_grid[i + 1][columnas]:
                        new_grid[i][columnas] = None
                        new_grid[i + 1][columnas] *= 2
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