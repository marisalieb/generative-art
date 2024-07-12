from turtle import *
from base_file import theme
import random


# helper function to draw a line from (x1, y1) to (x2, y2)
def draw_line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)


# recursively draws a tiling pattern.
def tiling(x, y, size, level, mode='straight'):
    """
    Parameters:
        x, y - x and y-coord of  center of current square
        size - size of  current square.
        level - current recursion level
        mode - straight or diagonal mode of drawing 
    """

    if level == 0:
        if mode == 'straight':
            if random.random() < 0.5:  # so half the time
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


# change parameters in tiling function
def main():
    theme(tracer_value=100)
    tiling(0, 0, 400, 3, 'diagonal')
    tracer(True)
    exitonclick()


if __name__ == "__main__":
    main()
