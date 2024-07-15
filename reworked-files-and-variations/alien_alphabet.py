from turtle import *
from base_file import theme
import random

# Set up the theme
theme(canvas_width=1200, canvas_height=800, pen_width=3)

size = 80
points = 1  # so how many points connecting

for y in range(300, -300, -size):
    # different colours per row
    r = random.random()
    g = random.random()
    b = random.random()
    pencolor(r, g, b)

    for x in range(-500 + size, 500, size):

        # original point
        pointx = x + random.uniform(-size/4, size/4)
        pointy = y + random.uniform(-size/4, size/4)

        # move to start point
        penup()
        goto(pointx, pointy)
        pendown()

        # draw shape
        for _ in range(points):
            # random end point
            pointx_end = x + random.uniform(-size/4, size/4)
            pointy_end = y + random.uniform(-size/4, size/4)

            #  connecting line
            goto(pointx_end, pointy_end)

        # back to original point
        goto(pointx, pointy)

    # increase points for next row
    points += 1

tracer(True)
exitonclick()
