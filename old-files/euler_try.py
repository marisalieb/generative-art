from turtle import *
from base_file import theme
import random


def euler_curve(step_size, angle_step, numbers_steps):
    angle = 0
    colormode(255)  # Use 255 for RGB colors
    for i in range(numbers_steps):
        # Random color or gradient
        pencolor((i % 255, (i * 2) % 255, (i * 3) % 255))

        right(angle)
        forward(step_size)
        angle += angle_step


def random_euler_curve(numbers_steps):
    angle = 0
    colormode(255)  # Use 255 for RGB colors
    for i in range(numbers_steps):
        # Random color
        pencolor((random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255)))

        right(angle)
        forward(random.randint(1, 5))  # Random step size
        angle += random.uniform(0.5, 2.5)  # Random angle step

# Theme settings


def setup_theme(tracer_value, turtle_shape):
    theme(tracer_value=tracer_value, hide_turtle=False)
    shape(turtle_shape)
    speed(0)  # Fastest drawing speed

# Main drawing functions


def draw_patterns():
    setup_theme(tracer_value=10, turtle_shape='turtle')
    euler_curve(7, .66, 1000)

    setup_theme(tracer_value=100, turtle_shape='circle')
    euler_curve(2, 1.01, 10000)

    setup_theme(tracer_value=100, turtle_shape='arrow')
    random_euler_curve(1000)


# Start drawing
setup_theme(tracer_value=100, turtle_shape='classic')
euler_curve(10, 1.99, 100000)

# Additional patterns
draw_patterns()

tracer(True)
exitonclick()
