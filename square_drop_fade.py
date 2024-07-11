from turtle import *
from base_file import theme
import random
import math

theme(canvas_width=1800, pen_width=2)

size = 30
noise = 0.0
max_distance = math.sqrt(800**2 + 400**2)
min_probability = 0.1
max_probability = 1.0


def compute_probability(distance, max_distance):
    """Compute the probability of drawing a square based on the distance from the center."""
    return (distance / max_distance) * (max_probability - min_probability) + min_probability


def compute_distance(x, y, horizontal_scale=1.0, vertical_scale=.7):
    """Compute an adjusted distance to create an oval shape."""
    return math.sqrt((x / horizontal_scale)**2 + (y / vertical_scale)**2)


for y in range(400, -400, -size):
    for x in range(-800, 800, size):
        # Adjust these values for a smaller oval
        distance = compute_distance(
            x, y, horizontal_scale=1.0, vertical_scale=0.8)

        # Ensure outer squares are drawn
        if abs(x) >= 770 or abs(y) >= 370:  # Edge buffer to ensure outermost squares are included
            probability = 1.0
        else:
            probability = compute_probability(distance, max_distance)

        # Skip drawing based on probability
        if random.random() > probability:
            continue

        # Move to location
        penup()
        goto(x, y)
        pendown()

        # Rotate only if y is not near the top, bottom, or outermost edges
        if abs(y) < 350 and abs(x) < 770:  # Adjust this threshold as needed
            noise = (max_distance - distance) / 15
            noise = noise if noise > 15 else 0
            angle = random.uniform(-noise, noise)
            right(angle)

        # Draw square
        for edge in range(4):
            forward(size)
            right(90)

        # Rotate back only if y is not near the top, bottom, or outermost edges
        if abs(y) < 350 and abs(x) < 770:
            left(angle)

    # Add noise
    noise += 5.0

tracer(True)
exitonclick()
