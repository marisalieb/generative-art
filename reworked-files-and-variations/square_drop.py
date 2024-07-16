from turtle import *
from base_file import theme
import random
import math

theme(canvas_width=1800, pen_width=2)

size = 35
noise = 0.0


def compute_distance(x, y, horizontal_scale=1.5, vertical_scale=.9):
    return math.sqrt((x/horizontal_scale)**2 + (y / vertical_scale)**2)


max_distance = math.sqrt(200**2 + 600**2)

for y in range(400, -400, -size):
    for x in range(-800, 800, size):

        # move to location
        penup()
        goto(x, y)
        pendown()

        distance = compute_distance(x, y)
        noise = (max_distance - distance) / 15
        noise = noise if noise > 15 else 0
        angle = random.uniform(-noise, noise)
        right(angle)

        for _ in range(4):
            forward(size)
            right(90)

        # rotate back
        left(angle)

    # add noise
    noise += 5.0

tracer(True)
exitonclick()
