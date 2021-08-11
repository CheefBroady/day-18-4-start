import turtle as t
import random

tim = t.Turtle()
rand = random
screen = t.Screen()


########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen", "brown", "coral", "DarkSalmon", "DeepSkyBlue"]

# direction = {1: 'tim.forward(10)', 2: 'tim.left(10)', 3: 'tim.right(10)'}
# variation = [1, 2, 3, 4]
directions = [0, 90, 180, 270]


# def choose_direction(variant, length):
#     if variant == 1:
#         tim.forward(length)
#     elif variant == 2:
#         tim.back(length)
#     elif variant == 3:
#         tim.left(length)
#     else:
#         tim.right(length)


for _ in range(100):
    tim.color(rand.choice(colours))
    tim.pensize(10)
    tim.speed("fastest")
    tim.forward(30)
    tim.setheading(rand.choice(directions))


screen.exitonclick()