from turtle import *

# basic set up for all project files


def theme(canvas_width=1000,
          canvas_height=1000,
          canvas_colour=(40/255, 40/255, 40/255),
          pen_colour=(70/255, 70/255, 70/255),
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


# COLOURS:
# sahara (194/255, 187/255, 169/255)
# light green (140/255, 160/255, 95/255)
# lilac (186/255, 163/255, 215/255)
# light orange (255/255, 178/255, 102/255)
# light blue (153/255, 204/255, 255/255)
# pink (255/255, 102/255, 178/255)
# dark grey (70/255, 70/255, 70/255)
# dark dark grey (40/255, 40/255, 40/255)
# light grey (224/255, 224/255, 224/255)
# dark beige (130/255, 110/255, 100/255)
# bright purple (100/255, 50/255, 100/255)
