from turtle import Turtle,Screen
from random import random

bobo=Turtle()
screen=Screen()

for _ in range(15):
    bobo.forward(10)
    bobo.penup()
    bobo.forward(10)
    bobo.pendown()

# for _ in range(10):
#     bobo.color("black")
#     bobo.forward(10)

#     bobo.color("white")
#     bobo.forward(10)


screen.exitonclick()