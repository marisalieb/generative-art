import random
from turtle import *

# Base theme settings


def theme(canvas_width=1200, canvas_height=800, pen_width=3, pen_colour='orange'):
    setup(width=canvas_width, height=canvas_height)
    pensize(pen_width)
    pencolor(pen_colour)
    bgcolor('black')
    speed('fastest')
    tracer(0, 0)


class GenerativeArt:
    def __init__(self, size=80, max_points=10):
        self.size = size
        self.max_points = max_points

    def random_color(self):
        """Generate a random base color."""
        r = random.random()
        g = random.random()
        b = random.random()
        return r, g, b

    def color_variation(self, base_color, variation_factor=0.1):
        """Create a variation of a base color."""
        r, g, b = base_color
        r = min(max(r + random.uniform(-variation_factor, variation_factor), 0), 1)
        g = min(max(g + random.uniform(-variation_factor, variation_factor), 0), 1)
        b = min(max(b + random.uniform(-variation_factor, variation_factor), 0), 1)
        return r, g, b

    def draw_shape(self, x, y, points, base_color):
        """Draw a random shape at a given position with a specified number of points and base color."""
        # Choose a variation of the base color
        # Increase variation_factor for more variation
        pencolor(self.color_variation(base_color, variation_factor=0.3))

        # Original point
        pointx = x + random.uniform(-self.size / 4, self.size / 4)
        pointy = y + random.uniform(-self.size / 4, self.size / 4)

        # Move to start point
        penup()
        goto(pointx, pointy)
        pendown()

        # Draw shape
        for edge in range(points):
            # Random end point
            pointx_end = x + random.uniform(-self.size / 4, self.size / 4)
            pointy_end = y + random.uniform(-self.size / 4, self.size / 4)

            # Draw connecting line
            goto(pointx_end, pointy_end)

            # Reset start for next loop iteration
            pointx = pointx_end
            pointy = pointy_end

        # Go back to original point
        goto(pointx, pointy)

    def generate_art(self):
        """Generate the entire artwork."""
        points = 1
        for y in range(300, -300, -self.size):
            base_color = self.random_color()  # Generate a base color for each row
            for x in range(-500 + self.size, 500, self.size):
                self.draw_shape(x, y, points, base_color)
            points = (points % self.max_points) + 1


if __name__ == "__main__":
    theme()
    art = GenerativeArt(size=80, max_points=10)
    art.generate_art()
    update()
    exitonclick()
