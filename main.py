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
variation = [1, 2, 3]

while walk:
    tim.color(rand.choice(colours))
    intvariation = rand.choice(variation)
    if intvariation == 1:
        tim.forward(15)
    elif intvariation == 2:
        tim.left(15)
    else:
        tim.right(15)
    # rand.random(direction)
    # tim.speed(speed="slow")
    # random(direction)
    counter += 1
    if counter == 150:
        walk = False

# do anything this evening, 10. August 2021
for n in range(1, 10):
    print(f"Was geht zum {n}ten mal ab?")
    print("und so weiter")
    print("und da geht noch einer....")

print("Do anything")
print("Änderungen im NeuenUniBranch durchgeführt")

screen.exitonclick()