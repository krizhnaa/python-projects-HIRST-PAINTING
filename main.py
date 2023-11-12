from turtle import Turtle, Screen, colormode
import random

colormode(255)
miya = Turtle()
miya.shape('arrow')
miya.pensize(15)

color_list = [(236, 35, 108), (146, 28, 66), (239, 75, 35), (230, 237, 232), (7, 148, 94), (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79), (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), (205, 56, 35)]

miya.hideturtle()
miya.penup()
miya.setheading(225)
miya.forward(250)
miya.setheading(0)
no_of_dot = 100
miya.speed('fastest')

for dot_count in range(1, no_of_dot+1):
    miya.dot(20, random.choice(color_list))
    miya.penup()
    miya.forward(50)

    if dot_count % 10 == 0:
        miya.setheading(90)
        miya.forward(50)
        miya.setheading(180)
        miya.forward(500)
        miya.setheading(0)

screen = Screen()
screen.screensize(canvwidth=100, canvheight=100)
screen.exitonclick()
