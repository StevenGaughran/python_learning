# Ignore the colorgram stuff. It was used to pull the colors out of the image.

#Day 18 went pretty well, actually. I liked my solution to the problem better than the teachers, so that's a
#nice feeling. However, I also spent at least 20 minutes longer than I should have solving a problem that didn't really
#exist. So that was fun.


# import colorgram
import random
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.shape("circle")
t.speed(0)
t.pensize(20)
screen.colormode(255)

# rgb_colors = []
#
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
               (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
               (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
               (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
               (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def art():
    t.penup()
    t.goto(-250, -250)
    row = -250
    for i in range(10):
        for y in range(10):
            t.color(random.choice(color_list))
            t.stamp()
            t.penup()
            t.forward(50)
        row += 50
        t.color("white")
        t.setpos(-250, row)


art()

screen.exitonclick()
