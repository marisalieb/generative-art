from turtle import *
from base_file import theme
import random

# Helper function to draw a line from (x1, y1) to (x2, y2)


def draw_line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# Helper function to draw a square centered at (x, y) with a given size


def draw_square(x, y, size):
    half_size = size / 2
    penup()
    goto(x - half_size, y - 1.5*half_size)
    pendown()
    for _ in range(4):
        forward(size / 1.5)
        right(90)


# Recursively draws a tiling pattern
def tiling(x, y, size, level, mode='straight'):
    """
    Parameters:
        x, y - x and y-coord of center of current square
        size - size of current square.
        level - current recursion level
        mode - straight or diagonal mode of drawing 
    """

    if level == 0:
        # Draw a square at the center of the smallest squares
        draw_square(x, y, size)

        # Draw lines based on mode
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


# Change parameters in tiling function
def main():
    theme(tracer_value=100)
    tiling(0, 0, 400, 3, 'diagonal')
    tracer(True)
    exitonclick()


if __name__ == "__main__":
    main()
