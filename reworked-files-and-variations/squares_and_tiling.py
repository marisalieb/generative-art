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
    goto(x - half_size, y - 1.5*half_size)
    pendown()
    for _ in range(4):
        forward(size / 1.5)
        right(90)


def tiling(x, y, size, level, mode='straight'):

    if level == 0:

        draw_square(x, y, size)

        #  lines based on mode
        if mode == 'straight':
            if random.random() < 0.5:
                draw_line(x, y - size, x, y + size)  # vertical line
            else:
                draw_line(x - size, y, x + size, y)  # horizontal line
        elif mode == 'diagonal':
            if random.random() < 0.5:
                draw_line(x - size, y + size, x + size, y - size)  # diagonal 1
            else:
                draw_line(x - size, y - size, x + size, y + size)  # diagonal 2
    else:
        new_size = size / 2
        new_level = level - 1
        tiling(x - new_size, y + new_size, new_size, new_level, mode)
        tiling(x + new_size, y + new_size, new_size, new_level, mode)
        tiling(x - new_size, y - new_size, new_size, new_level, mode)
        tiling(x + new_size, y - new_size, new_size, new_level, mode)


def main():
    theme(tracer_value=100)
    tiling(0, 0, 400, 3, 'diagonal')
    tracer(True)
    exitonclick()


if __name__ == "__main__":
    main()
