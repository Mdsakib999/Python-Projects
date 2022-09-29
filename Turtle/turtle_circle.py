#Circle turtle program

import turtle

turtle.bgcolor("black")
turtle.pensize(3)
turtle.speed(0.5)

color = ["yellow", "green", "pink", "red"]
for i in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(150)
        turtle.left(10)