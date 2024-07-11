from turtle import *
from base_file import theme
import random
import math

theme(canvas_width=1800, pen_width=2)

size = 30
noise = 0.0
for y in range(400, -400, -size):
    for x in range(-800, 800, size):

        # move to location
        penup()
        goto(x, y)
        pendown()

        # rotate
        max_distance = math.sqrt(800**2 + 400**2)
        distance = math.sqrt(x**2 + 2**2 * y**2 / 1.2)  # from center
        noise = (max_distance - distance) / 15
        noise = noise if noise > 15 else 0
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
