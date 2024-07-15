from turtle import *
from base_file import theme
import random


theme(pen_width=1)


def grow(length, decrease_length, angle_split, noise=0):
    if length > 10:
        width(length / 12)
        forward(length)

        new_length = length * decrease_length
        if noise > 0:
            new_length *= random.uniform(0.9, 1.1)

        angle_left = angle_split + random.gauss(0, noise)
        angle_right = angle_split + random.gauss(0, noise)

        left(angle_left)
        grow(new_length, decrease_length, angle_split, noise)
        right(angle_left)

        right(angle_right)
        grow(new_length, decrease_length, angle_split, noise)
        left(angle_right)

        backward(length)


def main():
    number_trees = 3

    # all set to 0, 0; might chagne that later
    positions = [(0, 0) for _ in range(number_trees)]

    for pos in positions:
        penup()
        goto(pos)
        pendown()
        left(360/number_trees)
        grow(100, 0.8, 30, 10)

    tracer(True)
    exitonclick()


if __name__ == "__main__":
    main()
