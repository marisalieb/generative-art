import random
from turtle import *
from base_file import theme

# variation of the alien alphabet file but with the use of a class
# and each row of 'letters' has kind of its own shade


class GenerativeArt:
    def __init__(self, size=80, max_points=10):
        self.size = size
        self.max_points = max_points

    def random_colour(self):
        # random base colour
        r = random.random()
        g = random.random()
        b = random.random()
        return r, g, b

    def colour_variation(self, base_colour, variation_factor=.01):
        # variation of  base colour
        r, g, b = base_colour
        r = min(max(r + random.uniform(-variation_factor, variation_factor), 0), 1)
        g = min(max(g + random.uniform(-variation_factor, variation_factor), 0), 1)
        b = min(max(b + random.uniform(-variation_factor, variation_factor), 0), 1)
        return r, g, b

    def draw_shape(self, x, y, points, base_colour):
        # draw a random shape at given position

        pencolor(self.colour_variation(base_colour, variation_factor=0.2))

        # original point
        pointx = x + random.uniform(-self.size / 4, self.size / 4)
        pointy = y + random.uniform(-self.size / 4, self.size / 4)

        # move to start point
        penup()
        goto(pointx, pointy)
        pendown()

        # draw shape
        for edge in range(points):

            pointx_end = x + random.uniform(-self.size / 4, self.size / 4)
            pointy_end = y + random.uniform(-self.size / 4, self.size / 4)

            #  connecting line
            goto(pointx_end, pointy_end)

            # Reset start
            pointx = pointx_end
            pointy = pointy_end

        # back to original point
        goto(pointx, pointy)

    def generate_art(self):
        points = 1
        for y in range(300, -300, -self.size):
            base_colour = self.random_colour()  # base colour for each row
            for x in range(-500 + self.size, 500, self.size):
                self.draw_shape(x, y, points, base_colour)
            points = (points % self.max_points) + 1


if __name__ == "__main__":
    theme(canvas_width=1200, canvas_height=800, pen_width=3)
    art = GenerativeArt(size=80, max_points=10)
    art.generate_art()
    update()
    exitonclick()
