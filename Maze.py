from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

r = (0,0,0)
b = (0,250,0)
w = (255,255,255)
x = 1
y = 1

maze = [[b,b,b,b,b,b,b,b],
        [b,r,r,r,r,r,r,b],
        [b,b,b,r,b,r,r,b],
        [b,r,b,r,b,b,b,b],
        [b,r,r,r,r,r,r,b],
        [b,r,b,b,b,b,r,b],
        [b,r,r,b,r,r,r,b],
        [b,b,b,b,b,b,b,b]]


maze[y][x] = w
sense.set_pixels(sum(maze,[]))

