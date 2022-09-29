import os
import keyboard
import time
import random


# snake class
class Snake:
    def __init__(self):
        self.position = [[5, 5], [5, 6]]
        self.image = "s"
        self.size = 1


# init the snake game
snake = Snake()
winSize = os.get_terminal_size()
running = True
keyPressed = [0, 0, 0, 0]

"""
column: winSize[0]
row: winSize[1]
"""

map2d = [[0 for x in range(winSize[0])] for x in range(winSize[1])]

# add fruit
x = random.randint(1, len(map2d)-1)
y = random.randint(1, len(map2d[0])-1)

map2d[x][y] = "f"

# refresh game
def displayMap():
    global map2d
    for row in map2d:
        line = ""
        for case in row:
            if not case:
                line += " "
            elif case == snake.image:
                line += snake.image
            elif case == "f":
                line += "*"
        print(line)

def updateSnakePosition():
    global map2d

    # clear snake in map
    for y in range(len(map2d)):
        for x in range(len(map2d[y])):
            if map2d[y][x] == snake.image:
                map2d[y][x] = 0
    
    for x in range(len(snake.position[:-1])):
        snake.position[x] = snake.position[x+1]
        map2d[snake.position[x][0]][snake.position[x][1]] = "s"

    map2d[snake.position[-1][0]][snake.position[-1][1]] = snake.image


while running:
    if snake.position[-1][0] == x and snake.position[-1][1] == y:
        x = random.randint(1, len(map2d)-1)
        snake.position.append([snake.position[-1][0], snake.position[-1][1]])
        y = random.randint(1, len(map2d[0])-1)
        map2d[x][y] = "f"        

    if keyboard.is_pressed("q"):
        running = False

    elif keyboard.is_pressed("right"):
        keyPressed = [1, 0, 0, 0]

    elif keyboard.is_pressed("left"):
        keyPressed = [0, 1, 0, 0]

    elif keyboard.is_pressed("up"):
        keyPressed = [0, 0, 1, 0]

    elif keyboard.is_pressed("down"):
        keyPressed = [0, 0, 0, 1]
      
    if keyPressed[0]:
        snake.position[-1][1] += 1

    elif keyPressed[1]:
        snake.position[-1][1] -= 1

    elif keyPressed[2]:
        snake.position[-1][0] -= 1

    elif keyPressed[3]:
        snake.position[-1][0] += 1

    updateSnakePosition()
    
    displayMap()
    time.sleep(0.1)
