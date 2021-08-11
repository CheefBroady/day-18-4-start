import turtle as t
import random

tim = t.Turtle()
rand = random
screen = t.Screen()


########### Challenge 4 - Random Walk ########
directions = [0, 90, 180, 270]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(50):
    tim.pencolor(random_color())
    tim.pensize(10)
    tim.speed("fastest")
    tim.forward(30)
    tim.setheading(rand.choice(directions))


screen.exitonclick()