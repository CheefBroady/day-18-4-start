import turtle as t
import random

tim = t.Turtle()
rand = random
screen = t.Screen()


########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen", "brown", "coral", "DarkSalmon", "DeepSkyBlue"]


directions = [0, 90, 180, 270]


for _ in range(100):
    tim.color(rand.choice(colours))
    tim.pensize(10)
    tim.speed("fastest")
    tim.forward(30)
    tim.setheading(rand.choice(directions))


screen.exitonclick()