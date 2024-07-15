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

    shade = random.uniform(0.4, 0.9)  # adjust the range for different shades
    pencolor(shade, shade, shade)
    fillcolor("white")
    begin_fill()
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()


def tiling(x, y, size, level, mode='straight'):

    if level == 0:
        draw_square(x, y, size)

        if mode == 'straight':
            if random.random() < 0.5:
                draw_line(x, y - size / 2, x, y + size / 2)  # vertical line
            else:
                draw_line(x - size / 2, y, x + size / 2, y)  # horizontal
        elif mode == 'diagonal':
            if random.random() < 0.5:
                draw_line(x - size / 2, y + size / 2, x +
                          size / 2, y - size / 2)  # diagonal 1
            else:
                draw_line(x - size / 2, y - size / 2, x +
                          size / 2, y + size / 2)  # diagonal 2
    else:
        new_size = size / 2
        new_level = level - 1
        tiling(x - new_size, y + new_size, new_size, new_level, mode)
        tiling(x + new_size, y + new_size, new_size, new_level, mode)
        tiling(x - new_size, y - new_size, new_size, new_level, mode)
        tiling(x + new_size, y - new_size, new_size, new_level, mode)


def main():
    theme()
    tiling(0, 0, 400, 4, 'straight')
    tracer(True)
    exitonclick()


if __name__ == "__main__":
    main()
