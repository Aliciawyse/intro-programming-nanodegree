# Lesson 3.3: Use Classes
# Mini-Project: Draw multiple squares to draw a circle.

import turtle

def draw_square(some_turtle):               #this function helps us get rid of
    for i in range(1,5):                    #repitition required to draw a square
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle Brad to draw a square:
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(7)
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_art()


