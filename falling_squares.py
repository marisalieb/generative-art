from turtle import *
from base_file import theme
import random

theme(canvas_width=700, pen_width=1)


size = 60
noise = 0.0
for y in range(400, -400, -size):
    for x in range(-250, 250, size):

        # move to location
        penup()
        goto(x, y)
        pendown()

        # rotate
        angle = random.uniform(-noise, noise)
        right(angle)

        # draw square
        for edge in range(4):
            forward(size)
            right(90)

        # rotate back
        left(angle)

    # add noise
    noise += 5.0


tracer(True)
exitonclick()
