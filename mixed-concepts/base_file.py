from turtle import *


def theme(canvas_width=1000,
          canvas_height=1000,
          canvas_colour=(140/255, 160/255, 95/255),
          # sahara canvas_colour=(194/255, 187/255, 169/255)
          pen_colour=(80/255, 57/255, 49/255),
          #   canvas_colour=(130/255, 110/255, 100/255),
          #   pen_colour=(100/255, 50/255, 100/255),
          pen_width=2,
          pen_speed=0,  # (0 is fastest)
          tracer_value=False,  # if False, drawing will be animated
          hide_turtle=True):

    setup(canvas_width, canvas_height)
    bgcolor(canvas_colour)
    color(pen_colour)
    width(pen_width)
    speed(pen_speed)
    tracer(tracer_value)
    if hide_turtle:
        hideturtle()
