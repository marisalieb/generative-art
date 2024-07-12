from turtle import *
from base_file import theme
import random

# Set up the theme
theme(canvas_width=1200, canvas_height=800, pen_width=3, pen_colour='orange')

size = 80
points = 1  # how many points connecting

for y in range(300, -300, -size):
    # different colours per row
    r = random.random()
    g = random.random()
    b = random.random()

    for x in range(-500 + size, 500, size):
        # different colours per point
        prime = random.random()
        r_point = r * prime
        g_point = g * prime
        b_point = b * prime

        pencolor(r_point, g_point, b_point)

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

            # draw connecting line
            goto(pointx_end, pointy_end)

        # go back to original point
        goto(pointx, pointy)

    # increase points for next row
    points += 1

tracer(True)
exitonclick()
