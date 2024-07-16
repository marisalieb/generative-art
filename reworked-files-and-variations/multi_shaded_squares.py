from turtle import *
from base_file import theme
import random
import math

theme(canvas_width=1800, pen_width=1)

#  base colour like blue
base_r = 0.2
base_g = 0.4
base_b = 0.8


def colour_variation(base_r, base_g, base_b, variation):
    # variation of  base colour
    r = min(max(base_r + random.uniform(-variation, variation), 0), 1)
    g = min(max(base_g + random.uniform(-variation, variation), 0), 1)
    b = min(max(base_b + random.uniform(-variation, variation), 0), 1)
    return r, g, b


size = 80
max_distance = math.sqrt(800**2 + 400**2)
min_probability = 0.1
max_probability = 1.0


def compute_probability(distance, max_distance):
    return (distance / max_distance) * (max_probability - min_probability) + min_probability


def compute_distance(x, y, horizontal_scale, vertical_scale):
    return math.sqrt((x / horizontal_scale)**2 + (y / vertical_scale)**2)


def draw_square(x, y, size):

    penup()
    goto(x - size / 2, y - size / 2)
    pendown()

    # no fill colour like in rainbow squares but pen colour
    # rainbow:
    # pencolor(random.random(), random.random(), random.random())

    colour = colour_variation(base_r, base_g, base_b, variation=0.25)
    # shade instead of rainbpw:
    pencolor(colour)

    for _ in range(4):
        forward(size)
        right(90)


# similar to nested squares
def draw_more_squares(x, y, size, levels):

    draw_square(x, y, size)
    if levels > 1:
        offset = size / 2  # change value 2 for diff results
        draw_more_squares(x - offset, y - offset, size / 2, levels - 1)
        draw_more_squares(x + offset, y - offset, size / 2, levels - 1)
        draw_more_squares(x - offset, y + offset, size / 2, levels - 1)
        draw_more_squares(x + offset, y + offset, size / 2, levels - 1)


for y in range(400, -400, -size):
    for x in range(-800, 800, size):

        distance = compute_distance(
            x, y, horizontal_scale=1.5, vertical_scale=0.8)

        # ensure outer shapes are drawn
        if abs(x) >= 800-size or abs(y) >= 400-size:
            probability = 1.0
        else:
            probability = compute_probability(distance, max_distance)

        # skip drawing some squares
        if random.random() > probability:
            continue

        # change level for diff results
        draw_more_squares(x, y, size, levels=4)


tracer(True)
exitonclick()
