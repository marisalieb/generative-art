from turtle import *
from base_file import theme


def euler_curve(step_size, angle_step, numbers_steps):
    angle = 0
    for _ in range(numbers_steps):
        right(angle)
        forward(step_size)
        angle += angle_step


"""
theme(tracer_value=1, hide_turtle=False)
euler_curve(10, .1, 600)

theme(tracer_value=10)
euler_curve(7, .66, 10000)

theme(tracer_value=100)
euler_curve(2, 1.01, 100000)
"""

theme(tracer_value=100)
euler_curve(3, 1.99, 100000)


tracer(True)
exitonclick()
