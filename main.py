import colorgram
from turtle import Turtle, Screen, colormode
import random

# colors = colorgram.extract('image.jpg',20)
# rgb_color = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_color.append(rgb)
#
# print(rgb_color)
colormode(255)
miya = Turtle()
miya.shape('arrow')
miya.pensize(15)


color_list = [(236, 35, 108), (146, 28, 66), (239, 75, 35), (230, 237, 232), (7, 148, 94), (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79), (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), (205, 56, 35)]

miya.penup()
miya.setheading(225)
miya.forward(250)
miya.setheading(0)

for _ in range(0, 10):
    miya.dot(20, random.choice(color_list))
    miya.penup()
    miya.forward(50)

while True:
    miya.setheading(90)
    miya.forward(50)
    miya.setheading(180)
    miya.forward(500)
    miya.setheading(0)

    for _ in range(0,10):
        miya.dot(20, random.choice(color_list))
        miya.penup()
        miya.forward(50)



screen = Screen()
screen.screensize(canvwidth=100, canvheight=100)
screen.exitonclick()
