from turtle import *
from base_file import theme
import random


def draw_square(x, y, size):
    # draw a square centered at x, y with given size
    penup()
    goto(x - size / 2, y - size / 2)
    pendown()
    for _ in range(4):
        forward(size)
        left(90)


# draw a grid of squares with inner squares that are randomly offset
def draw_grid_with_inner_squares(size_outer=200, noise=5, shrink_inner=14):

    # calculate the range of x, y coords for grid
    x_range = range(-500 + size_outer // 2, 500, size_outer)
    y_range = range(-500 + size_outer // 2, 500, size_outer)

    for x in x_range:
        for y in y_range:
            # draw  outer square
            draw_square(x, y, size_outer)

            # random offsets for inner squares
            x_offset = random.uniform(-noise, noise)
            y_offset = random.uniform(-noise, noise)

            # draw inner squares with decreasing size
            for i in range(7):
                draw_square(x + i * x_offset, y + i * y_offset,
                            size_outer - i * shrink_inner)


def main():
    theme()
    draw_grid_with_inner_squares()
    tracer(True)
    exitonclick()


if __name__ == "__main__":
    main()
