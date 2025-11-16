# Draw a square 

from turtle import Turtle, Screen

gogo_the_turtle=Turtle()
gogo_the_turtle.color("red")

def move():
    gogo_the_turtle.forward(100)
    gogo_the_turtle.left(90)

for _ in range(4):
    move()

screen=Screen()
screen.exitonclick()
