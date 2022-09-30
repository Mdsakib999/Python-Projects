#Simple polygon 

import turtle

t = turtle.Turtle()

side_bar = 15 #int(input("Enter the number of size: "))

length = 50 #int(input("Enter the length of side bar: "))


for i in range(side_bar):
    turtle.forward(length)
    turtle.right(360 / side_bar)