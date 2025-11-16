import turtle as t
import random

tim = t.Turtle()
tim.width(4)
t.colormode(255)


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")


########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r,g,b)


for _ in range(200):
    tim.pencolor(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
