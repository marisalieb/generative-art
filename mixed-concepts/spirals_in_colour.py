from turtle import *
from base_file import theme
import random


def euler_curve(step_size, angle_step, num_steps):
    # draw euler curve with given step size and angle step
    angle = 0
    colormode(255)  # use 255 for RGB colors
    for i in range(num_steps):
        # random color or gradient
        pencolor((i % 255, (i * 2) % 255, (i * 3) % 255))
        right(angle)
        forward(step_size)
        angle += angle_step


def random_euler_curve(num_steps):
    # draw random euler curve with random step sizes and angle steps
    angle = 0
    colormode(255)  # use 255 for RGB colors
    for i in range(num_steps):
        # random color
        pencolor((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))
        right(angle)
        forward(random.randint(1, 5))  # random step size
        angle += random.uniform(0.5, 2.5)  # random angle step


def setup_theme(tracer_value, turtle_shape):
    # set up theme settings for turtle graphics
    theme(tracer_value=tracer_value, hide_turtle=False)
    shape(turtle_shape)
    speed(0)  # fastest drawing speed


def draw_patterns():
    # draw various patterns using setup_theme and drawing functions
    setup_theme(tracer_value=10, turtle_shape='turtle')
    euler_curve(7, 0.66, 1000)

    setup_theme(tracer_value=100, turtle_shape='circle')
    euler_curve(2, 1.01, 10000)

    setup_theme(tracer_value=100, turtle_shape='arrow')
    random_euler_curve(1000)


# start drawing
setup_theme(tracer_value=100, turtle_shape='classic')
euler_curve(10, 1.99, 100000)

# draw additional patterns
draw_patterns()

tracer(True)
exitonclick()
