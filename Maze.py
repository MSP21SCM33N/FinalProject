#Marble Maze Game

from time import sleep
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

b = (0,0,255)
n = (0,0,0)
g = (0,255,0)
w = (255,255,255)
x = 3
y = 6

board = [
    [b,b,b,b,b,b,b,b],
    [b,n,n,n,b,n,n,b],
    [b,n,b,b,b,b,n,b],
    [b,n,b,n,n,n,n,b],
    [b,n,n,n,b,b,n,b],
    [b,n,b,b,b,g,n,b],
    [b,n,n,n,b,n,n,b],
    [b,b,b,b,b,b,b,b]
    ]
   

game = True

def move_marble(pitch,roll,x,y):
    change_x = x
    change_y = y
    if 10 < pitch < 179 and x != 0:
        change_x -= 1
    elif 181 < pitch < 350 and x != 7:
        change_x += 1
    if 10 < roll < 179 and y != 7:
        change_y += 1
    elif 181 < roll < 350 and y != 0:
        change_y -= 1
    change_x, change_y = check_wall(x,y,change_x,change_y)
    return change_x,change_y

def check_wall(x,y,change_x,change_y):
    if board[change_y][change_x] != b:
        return change_x,change_y
    elif board[change_y][x] != b:
        return x,change_y
    elif board[y][change_x] != b:
        return change_x,y
    else:
        return x,y

while game:
    o = sense.get_orientation()
    pitch = o['pitch']
    roll = o['roll']
    x,y = move_marble(pitch,roll,x,y)
    board[y][x] = w
    sense.set_pixels(sum(board,[]))
    sleep(0.05)
    board[y][x] = n
    if board[y][x] == g:
        game == False
        sense.show_message("You Win!")
    
    

