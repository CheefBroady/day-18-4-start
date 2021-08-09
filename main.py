import turtle as t
import random

tim = t.Turtle()
rand = random
screen = t.Screen()
walk = True
counter = 0

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen", "brown", "coral", "DarkSalmon", "DeepSkyBlue"]

direction = [tim.forward(15), tim.left(15), tim.right(15)]


while walk:
    tim.color(colours[rand.randint(0, 10)])
    rand.random(direction)
    # tim.speed(speed="slow")
    # random(direction)
    counter += 1
    if counter == 15:
        walk = False



screen.exitonclick()