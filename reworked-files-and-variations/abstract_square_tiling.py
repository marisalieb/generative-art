from turtle import *
from base_file import theme
import random


def draw_line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)


def draw_square(x, y, size):
    half_size = size / 2
    penup()
    goto(x - half_size, y - half_size)
    pendown()
    for _ in range(4):
        forward(size)
        right(90)


def tiling(x, y, size, level):

    if level == 0:

        draw_square(x, y, size)

        for i in range(7):

            x_offset = random.uniform(-5, 5)
            y_offset = random.uniform(-5, 5)
            draw_square(x + i * x_offset, y + i * y_offset, size - i * 14)

    else:
        new_size = size / 2
        new_level = level - 1
        tiling(x - new_size, y + new_size, new_size, new_level)
        tiling(x + new_size, y + new_size, new_size, new_level)
        tiling(x - new_size, y - new_size, new_size, new_level)
        tiling(x + new_size, y - new_size, new_size, new_level)


def main():
    theme(tracer_value=100)
    tiling(0, 0, 400, 3)
    tracer(True)
    exitonclick()


if __name__ == "__main__":
    main()
