from turtle import *
import random

setup(1000, 1000)

# x y where are oyu on screen, so you can reapply tiling on the smaller portion of screen
# size like how large is that section
# level of how deep into recursion are we


def tiling(x, y, size, level, mode='straight'):

    # we have reached final level of recursion and we now draw
    if level == 0:

        if mode == 'straight':

            # vertical line
            if random.random() < 0.5:  # draw random number from 0 to 1 and then 50% of that
                penup()
                goto(x, y-size)
                pendown()
                goto(x, y+size)

            # horizontal line
            else:
                penup()
                goto(x-size, y)
                pendown()
                goto(x+size, y)

        elif mode == 'diagonal':

            # diagonal 1
            if random.random() < 0.5:
                penup()
                goto(x-size, y+size)
                pendown()
                goto(x+size, y-size)

            # diagonal 2
            else:
                penup()
                goto(x-size, y-size)
                pendown()
                goto(x+size, y+size)

    # is level isnt 0
    else:
        size /= 2
        level -= 1
        tiling(x-size, y+size, size, level, mode)
        tiling(x+size, y+size, size, level, mode)
        tiling(x-size, y-size, size, level, mode)
        tiling(x+size, y-size, size, level, mode)


width(3)
hideturtle()
tracer(False)
tiling(0, 0, 400, 3, 'diagonal')
tracer(True)

exitonclick()
