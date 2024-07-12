from turtle import *
from base_file import theme
import random

theme(canvas_width=1200,
      canvas_height=800,
      pen_width=3,
      pen_colour='orange')


size = 80
points = 1  # how many point connecting
for y in range(300, -300, -size):

    # different colours per row
    r = random.random()
    g = random.random()
    b = random.random()
    pencolor(r, g, b)

    # or for colour palete play with this value
    prime = random.random()

    for x in range(-500+size, 500, size):

        # different colours per letter
        r = random.random() * prime
        g = random.random() * prime
        b = random.random() * prime
        pencolor(r, g, b)

        # original point
        pointx = x + random.uniform(-size/4, size/4)
        pointy = y + random.uniform(-size/4, size/4)

        # start point to original point
        pointx_start = pointx
        pointy_start = pointy

        # move to start point
        penup()
        goto(pointx_start, pointy_start)
        pendown()

        # draw shape
        for edge in range(points):

            # random end point
            pointx_end = x + random.uniform(-size/4, size/4)
            pointy_end = y + random.uniform(-size/4, size/4)

            # draw connecting line
            goto(pointx_end, pointy_end)

            # reset start for next loop iteration
            pointx_start = pointx_end
            pointy_start = pointy_end

        # go back to original point
        goto(pointx, pointy)

    # increase points
    points += 1


tracer(True)
exitonclick()
