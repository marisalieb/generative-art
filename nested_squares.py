from turtle import *

import random


def draw_square(x, y, size):  # x y will be centre of quare
    penup()
    goto(x-size/2, y-size/2)  # bottom left corner
    pendown()
    for edge in range(4):
        forward(size)
        left(90)  # left turn 90 degrees


setup(1000, 1000)
width(2)  # stroke width
hideturtle()
tracer(False)

# nested loop over x and y coordinates
size_outer = 100
noise = 5
shrink_inner = 7
# outer loop goes from specified x to y by step of size outer
# if no loop for y then x square would just be in a horizontal line
for x in range(-500+size_outer//2, 500, size_outer):
    for y in range(-500+size_outer//2, 500, size_outer):

        # draw outer squares or the grid
        draw_square(x, y, size_outer)

        # offsets for inner squares
        # betweeen these noise parameters it will draw random number and shift inner quares by that in outer square
        x_offset = random.uniform(-noise, noise)
        y_offset = random.uniform(-noise, noise)

        # draw inner squares
        for i in range(7):
            draw_square(x+i*x_offset, y+i*y_offset, size_outer-i*shrink_inner)


# draw_square(100, -100, 200)

tracer(True)
exitonclick()
