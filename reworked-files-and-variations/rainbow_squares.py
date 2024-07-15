from turtle import *
from base_file import theme
import random
import math

theme(canvas_width=1800, pen_width=2)

size = 30
noise = 0.0
max_distance = math.sqrt(800**2 + 400**2)
min_probability = 0.1
max_probability = 1.0


def compute_probability(distance, max_distance):
    # compute probability of drawing square based on distance from center
    return (distance / max_distance) * (max_probability - min_probability) + min_probability


def compute_distance(x, y, horizontal_scale=1.0, vertical_scale=0.7):
    # compute adjusted distance to create oval shape
    return math.sqrt((x / horizontal_scale)**2 + (y / vertical_scale)**2)


def random_color():
    # generate a random color
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


def draw_square(x, y, size):
    # draw a square centered at (x, y) with random color
    penup()
    goto(x - size / 2, y - size / 2)  # bottom left corner
    pendown()

    # Random color for the square
    fillcolor(random_color())
    begin_fill()
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()


def draw_nested_squares(x, y, size, levels):
    # recursively draw nested squares
    draw_square(x, y, size)
    if levels > 1:
        offset = size / 4
        draw_nested_squares(x - offset, y - offset, size / 2, levels - 1)
        draw_nested_squares(x + offset, y - offset, size / 2, levels - 1)
        draw_nested_squares(x - offset, y + offset, size / 2, levels - 1)
        draw_nested_squares(x + offset, y + offset, size / 2, levels - 1)


for y in range(400, -400, -size):
    for x in range(-800, 800, size):
        # adjust for smaller oval
        distance = compute_distance(
            x, y, horizontal_scale=1.0, vertical_scale=0.8)

        # ensure outer squares are drawn
        if abs(x) >= 770 or abs(y) >= 370:  # edge buffer to ensure outermost squares are included
            probability = 1.0
        else:
            probability = compute_probability(distance, max_distance)

        # skip drawing based on probability
        if random.random() > probability:
            continue

        # draw outer square
        draw_square(x, y, size)

        # draw nested squares
        draw_nested_squares(x, y, size, levels=3)  # adjust levels as needed

    # add noise
    noise += 5.0

tracer(True)
exitonclick()
