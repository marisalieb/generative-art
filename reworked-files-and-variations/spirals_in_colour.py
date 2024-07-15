from turtle import *
from base_file import theme
import random


def euler_curve(step_size, angle_step, number_steps):

    angle = 0
    colormode(255)
    for i in range(number_steps):
        pencolor((i % 255, (i * 2) % 255, (i * 3) % 255))
        right(angle)
        forward(step_size)
        angle += angle_step


def random_euler_curve(number_steps):
    # draw curve with random step sizes and angle steps
    angle = 0
    colormode(255)
    for i in range(number_steps):

        pencolor((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))

        right(angle)
        forward(random.randint(2, 100))  # random step size
        angle += random.uniform(0.5, 2.5)  # random angle step


"""
def draw_patterns():
  
    setup_theme(tracer_value=10)
    euler_curve(7, 0.66, 1000)

    setup_theme(tracer_value=100)
    euler_curve(2, 1.01, 10000)

    setup_theme(tracer_value=100)
    random_euler_curve(1000)
"""


theme(tracer_value=1000)
euler_curve(5, 1.99, 100000)


tracer(True)
exitonclick()
